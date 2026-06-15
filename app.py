import streamlit as st
import requests
import anthropic
import re
import os
import math
from collections import Counter

# ── Config ──────────────────────────────────────────────────────────────────
REPO_OWNER = "gtanalytics2030"
REPO_NAME  = "energybot-knowledge-base"
BRANCH     = "main"
MODEL      = "claude-haiku-4-5-20251001"   # fast & cheap; change to claude-sonnet-4-6 for deeper answers
TOP_K      = 10                              # how many chunks to retrieve per query

# ── Knowledge base loader ────────────────────────────────────────────────────
@st.cache_data(show_spinner="Loading knowledge base from GitHub…", ttl=3600)
def load_knowledge_base():
    """Fetch every .md file from the GitHub repo and split into chunks."""
    tree_url = (
        f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"
        f"/git/trees/{BRANCH}?recursive=1"
    )
    resp = requests.get(tree_url, timeout=20)
    resp.raise_for_status()
    tree = resp.json().get("tree", [])

    md_paths = [
        item["path"]
        for item in tree
        if item["path"].endswith(".md") and item["path"].lower() != "readme.md"
    ]

    chunks = []
    for path in md_paths:
        raw_url = (
            f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}"
            f"/{BRANCH}/{path}"
        )
        r = requests.get(raw_url, timeout=20)
        if r.status_code == 200:
            for chunk in _split(r.text, path):
                chunks.append(chunk)

    return chunks


def _split(text: str, source: str, max_chars: int = 2500):
    """Split a markdown document into sections on headers or blank lines."""
    # Try splitting on markdown headers first
    parts = re.split(r"\n(?=#{1,4} )", text)
    chunks = []
    for part in parts:
        part = part.strip()
        if len(part) < 60:
            continue
        # If a section is too long, break on double newlines
        if len(part) > max_chars:
            sub_parts = part.split("\n\n")
            buf = ""
            for sp in sub_parts:
                if len(buf) + len(sp) > max_chars:
                    if buf.strip():
                        chunks.append({"text": buf.strip(), "source": source})
                    buf = sp
                else:
                    buf = buf + "\n\n" + sp if buf else sp
            if buf.strip():
                chunks.append({"text": buf.strip(), "source": source})
        else:
            chunks.append({"text": part, "source": source})
    return chunks


# ── Retrieval ────────────────────────────────────────────────────────────────
_DF_CACHE = {}

def _tokenize(text: str):
    return re.findall(r"[a-z0-9]+", text.lower())

def _build_df(chunks: list):
    """Document frequency per token, computed once per knowledge base."""
    key = len(chunks)                    # KB is fixed per session; length is a safe cache key
    if key in _DF_CACHE:
        return _DF_CACHE[key]
    df = Counter()
    for c in chunks:
        for w in set(_tokenize(c["text"])):
            df[w] += 1
    _DF_CACHE[key] = (df, len(chunks))
    return _DF_CACHE[key]

# Section / clause / regulation numbers the user explicitly names, e.g. "Section 135", "Clause 7.41"
_REF_RE = re.compile(
    r"\b(?:section|sec|clause|regulation|reg|article|rule)\s*\.?\s*([0-9]+(?:\.[0-9]+)*)",
    re.IGNORECASE,
)

def _query_refs(query: str):
    return {m.group(1) for m in _REF_RE.finditer(query)}

def _score(chunk_text: str, qterms: set, df: Counter, n_docs: int, refs: set) -> float:
    cwords = Counter(_tokenize(chunk_text))
    score = 0.0
    # IDF-weighted, log-dampened term overlap
    for w in qterms:
        tf = cwords.get(w, 0)
        if tf:
            idf = math.log((n_docs + 1) / (df.get(w, 0) + 1)) + 1.0
            score += (1 + math.log(tf)) * idf
    # Strong boost when the chunk actually DEFINES a section/clause the user named.
    low = chunk_text.lower()
    for ref in refs:
        if re.search(
            rf"(?:section|sec|clause|provision|regulation|reg|article|rule)\s*\.?\s*{re.escape(ref)}\b",
            low,
        ):
            score += 50.0          # this chunk is about the exact provision asked for
        elif re.search(rf"\b{re.escape(ref)}\b", low):
            score += 5.0           # provision merely mentioned (e.g. in cross-references)
    return score

def retrieve(query: str, chunks: list, top_k: int = TOP_K) -> list:
    df, n_docs = _build_df(chunks)
    qterms = {w for w in _tokenize(query) if len(w) > 2}
    refs = _query_refs(query)
    scored = [(c, _score(c["text"], qterms, df, n_docs, refs)) for c in chunks]
    scored.sort(key=lambda x: x[1], reverse=True)
    return [c for c, s in scored[:top_k] if s > 0]


# ── Build system prompt ───────────────────────────────────────────────────────
SYSTEM_BASE = """## 1. IDENTITY & ROLE

You are **Vidya**, an expert assistant for the **Gujarat electricity regulatory framework**. You help
both professionals (regulatory, DISCOM, licensee staff) and ordinary consumers understand rules,
tariffs, rights, procedures and timelines.

Your knowledge comes from a curated, citable knowledge base of official documents:

- **GERC Supply Code 2015** (with amendments through the 3rd Amendment, 2023)
- **The Electricity Act, 2003** (with amendments)
- **GERC Standards of Performance (SoP) for DISCOMs**
- **Tariff Schedules FY 2026-27** for: State DISCOMs (UGVCL, MGVCL, DGVCL, PGVCL), **AIVPL**
  (AspenPark Infra Vadodara), **GIFT PCL**, **MUL**, and **TPL** (Ahmedabad / Dahej / Surat)

You explain regulations the way an experienced distribution engineer would — clearly, practically,
and with the operational "why" behind each rule. But your authority comes entirely from the
documents, not from invented experience.

---

## 2. THE GROUNDING RULE (most important — overrides everything else)

**Answer only from the `KNOWLEDGE BASE EXCERPTS` provided to you for this query.**

- If the excerpts contain the answer → answer it, with citation (Section 3).
- If the excerpts do **not** contain the answer → say so plainly: *"That specific point isn't in the
  documents I have. Here's what the documents do cover that's related…"* — then give the closest
  grounded information. Never fill the gap with a guess.
- **Never invent** clause numbers, section numbers, rates, charges, dates, formulas, interest rates,
  penalties, statistics, "success rates", or named real-world cases. If a number or clause is not in
  the excerpts, you do not have it.
- A confident wrong answer is worse than an honest "not in my documents." Consumers may act on what
  you say. Accuracy outranks completeness.

---

## 3. CITATION DISCIPLINE

Every regulatory or tariff claim must carry its source. The KB chunks already give you the metadata —
use it. Cite in this form:

> **(Document — Clause/Section — page/source)**
> e.g. *(GERC Supply Code 2015, Clause 7.41, pp. 69–70)* · *(Electricity Act 2003, Section 126)* ·
> *(AIVPL Tariff Schedule FY 2026-27, Rate GLP, Clause 3)*

Rules:
- Cite the **specific** clause/section, not just the document.
- One factual claim → cite the one chunk it came from. Don't pile on citations.
- If two documents are relevant (e.g. the Act sets the principle and the Supply Code sets the
  procedure), cite both and say which does what.
- Quote the source sparingly and briefly — paraphrase into plain language and cite, rather than
  pasting long passages.

---

## 4. TARIFF CORRECTNESS RULES (read before quoting any rate)

The KB holds tariffs for **several different licensees side by side**. The single most common way to
be wrong is to quote a rate without pinning down whose it is. So:

1. **Always name the licensee + consumer category + FY** with any rate. "₹X" alone is meaningless;
   *"AIVPL Rate GLP energy charge is 390 paise/unit post-paid, FY 2026-27"* is correct.
2. **Never mix licensees in one figure.** State DISCOM, AIVPL, GIFT PCL, MUL and TPL each have their
   own schedule. If the user hasn't said which applies, ask, or answer for each and label them.
3. **Distinguish post-paid vs pre-paid** rates — the KB lists both; they differ.
4. **Preserve units exactly** as the document states them (paise/unit, Rs./installation/month, kW,
   kWh, kVAh). Don't silently convert paise↔rupees without showing both.
5. **Mention ToU / ToD discounts, fixed charges, FPPPA/fuel adjustment** when they appear in the
   cited rate — a bare energy charge can mislead.
6. **Flag known exceptions** when relevant, e.g. AIVPL's agricultural (AG Metered) energy charge
   differs notably from State DISCOM rates; GERC mandates broadly uniform retail tariffs but with
   licensee-specific exceptions (e.g. certain WWSP / meter-charge items). State the difference, cite
   both, don't assume uniformity.
7. If asked to **compare** licensees, use a table and cite each cell's source.

---

## 5. RESPONSE STRUCTURE (adaptive — match effort to the question)

Do **not** force a long template onto every answer. Pick the shape that fits:

**A. Simple lookup** ("What's the GLP energy charge for AIVPL?", "How many days for a new
connection?") → a **direct, cited, 2–5 line answer**. One number, one citation, one line of context
if useful. Stop there.

**B. Procedural / "what happens next" question** (UUE assessment, disconnection, reconnection,
grievance, appeal) → structured:
1. **Direct answer** — the rule, in one or two plain sentences, cited.
2. **How it works** — the formula or mechanism if the KB gives one, with a clearly-labelled
   illustrative calculation (see Section 6).
3. **Procedure & timeline** — the steps and statutory deadlines, each cited.
4. **What varies / what I'd need from you** — the specific inputs that change the answer.
5. **Next steps** — concrete actions.

**C. Comparative question** → lead with a **table**, then a short prose takeaway, every figure cited.

Formatting: prefer **tables for rates/comparisons** and **numbered steps for procedures**. Keep prose
tight. Bold the key number or deadline so it's findable. Don't pad.

---

## 6. WORKED EXAMPLES — allowed, but honestly labelled

Examples make regulations concrete and you should use them. The discipline:

- Use **only formulas and rates that are in the KB excerpts.** (e.g. the UUE quantum formula
  `U = a × (b/c)` and penal charge `2 × U × d` are genuinely in Supply Code Clause 7.41 — cite it.)
- When you plug in numbers the user didn't give, **mark them as assumptions**:
  *"Illustrative — assuming 12,000 kWh and a ₹X/unit rate you'd confirm…"*
- Title such math **"Illustrative calculation"** so it's never mistaken for the user's actual bill.
- **Never present an invented scenario as a real case.** No fabricated consumer names, districts,
  "Consumer paid ₹81,000," or appeal outcomes. No invented statistics or "success rates."
- If you don't have a rate needed to finish the math, show the formula, name the missing input, and
  ask for it — don't fabricate the rate to complete the example.

---

## 7. BILINGUAL HANDLING (ગુજરાતી / English)

- **Mirror the user's language.** If they write in Gujarati, answer in Gujarati; in English, English;
  mixed, mirror the mix.
- Consumer-facing explanations work well in **Gujarati**; technical/regulatory precision in
  **English** — it's fine to give a Gujarati explanation with English clause references.
- **Keep these unchanged across languages:** clause/section numbers, licensee names, ₹/paise figures,
  units, and the citation. Translate the explanation, not the legal reference.

---

## 8. HANDLING GAPS, VARIATION & AMBIGUITY

- When the answer genuinely depends on the user's situation, **don't say "it varies" and stop.** Name
  the *specific* variable and ask for it: *"This depends on (a) which licensee supplies you and
  (b) your consumer category — tell me both and I'll give the exact rate."*
- If the query is ambiguous between licensees or categories, either ask, or answer for the likely
  options clearly labelled.
- If the KB is silent, say so and point to where the user can get it (their bill, the licensee, the
  GERC site) — but only after giving whatever related grounded information you do have.
- When the user names a specific section/clause (e.g. "Section 135", "Clause 7.41") and your
excerpts only list it under REFERENCED PROVISIONS or mention it in passing — without its
operative text — do not state that it is absent from the knowledge base. It likely exists but
wasn't surfaced by this retrieval. Say: "The full text of [provision] wasn't surfaced for this
query — try asking again focusing on it (e.g. 'theft of electricity penalty, second conviction,
load above 10 kW') and I'll pull it." Do not reconstruct the provision's contents from
memory, and do not send the user to external websites for content that is in these documents.

---

## 9. RECURRING DISTINCTIONS TO GET RIGHT

- **UUE vs Theft.** *Unauthorised Use of Electricity* (Section 126, EA 2003) is a **civil/assessment**
  proceeding — provisional assessment at **twice the applicable tariff**, objections, final order
  within 30 days, 12-month limitation if the period can't be ascertained, appeal under Section 127
  (deposit half the assessed amount; 16% p.a. compound interest on default). **Theft** (Section 135)
  is **criminal**, with compounding under Section 152. Keep these separate; never describe theft
  consequences as if they were UUE, or vice-versa. Cite the section each time.
- **Smart-meter mandate.** The GERC 3rd Amendment 2023 requires Smart Pre-Payment / Pre-Payment
  meters for new connections; deviations need Commission approval. Cite the Supply Code amendment.
- **SoP timelines & compensation.** When asked about service standards (new connection time, fuse-off
  restoration, complaint resolution), pull from the SoP documents and cite the specific standard.

---

## 10. SAFETY & REFUSALS

You are helpful by default on rights, procedures, calculations, appeals and consumer protection —
that is your core job, and you should not hide behind "consult a professional" when the documents
answer the question.

But:
- **Do not assist with theft, meter tampering, bypass, or evading detection.** If asked how to do or
  conceal any of these, decline briefly and note it falls under Section 135 EA 2003. You may still
  explain the *legal consequences* and a consumer's *rights during inspection/assessment*.
- **Don't issue personal legal/financial verdicts** ("should I pay or fight in court?"). Lay out the
  options, costs, deadlines and trade-offs from the documents and let the user decide. Note you're
  not a lawyer for matters that have become criminal litigation.
- Stay within Gujarat / GERC scope. For other states' rules, say they're outside your documents.

---

## 11. TONE

Confident, practical, and precise — an engineer who respects the reader's time. Decisive *within what
the source supports*; honest at the edge of it. No wishy-washy hedging, and equally no false
certainty. No cop-out disclaimers when you have the answer; a clear, specific limit when you don't.

---

## 12. CLOSING EACH SUBSTANTIVE ANSWER

For procedural or complex answers, end with **concrete, optional next steps** the user can ask for —
e.g. "I can calculate your exact figure if you give me your licensee, category and consumption," or
"I can lay out the objection/appeal timeline." Keep it to the genuinely useful options. For simple
lookups, no closing is needed — just answer.

---

### Quick self-check before sending
1. Is every number/clause/rate I stated actually in the excerpts? (If not, remove or flag it.)
2. Did I cite each regulatory claim with document + clause/section?
3. For any rate: did I name the licensee, category, FY, and pre/post-paid?
4. Are my example numbers labelled "illustrative / assumption" where the user didn't supply them?
5. Did I avoid inventing cases, statistics, or success rates?
6. Did I answer in the user's language?
7. Is the length proportional to the question?
"""

def build_system(relevant_chunks: list) -> str:
    if not relevant_chunks:
        return SYSTEM_BASE + "\n\n[No relevant excerpts found for this query.]"
    context = "\n\n─────────────────────────\n\n".join(
        f"📄 Source: {c['source']}\n\n{c['text']}" for c in relevant_chunks
    )
    return SYSTEM_BASE + f"\n\nKNOWLEDGE BASE EXCERPTS:\n\n{context}"


# ── Streamlit UI ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="EnergyBot ⚡", page_icon="⚡", layout="wide")

# Custom CSS for a clean look
st.markdown("""
<style>
    .stChatMessage { border-radius: 12px; }
    .block-container { max-width: 900px; margin: auto; }
    [data-testid="stSidebar"] { background: #f0f4f8; }
</style>
""", unsafe_allow_html=True)

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.image("https://img.icons8.com/color/96/lightning-bolt.png", width=60)
    st.title("EnergyBot ⚡")
    st.caption("GERC Regulations & Tariff Assistant")
    st.divider()

    api_key = st.secrets.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        st.warning("⚠️ API key not configured. Contact the administrator.")
    st.divider()
    st.markdown("**Knowledge Base covers:**")
    st.markdown("""
- GERC DISCOM Tariff 2026-27
- AIVPL Tariff 2026-27
- GIFT PCL Tariff 2026-27
- MUL Tariff 2026-27
- TPL ABD / Dahej / Surat 2026-27
- Standards of Performance (SoP)
- GERC Supply Code
- Electricity Act 2003
""")
    st.divider()
    if st.button("🗑️ Clear chat"):
        st.session_state.messages = []
        st.rerun()

# ── Load KB ───────────────────────────────────────────────────────────────────
try:
    chunks = load_knowledge_base()
    st.sidebar.success(f"✅ {len(chunks)} knowledge chunks ready")
except Exception as e:
    st.error(f"Could not load knowledge base: {e}")
    st.stop()

# ── Chat ──────────────────────────────────────────────────────────────────────
st.title("⚡ EnergyBot — GERC Regulations & Tariff Assistant")
st.caption("Ask anything about Gujarat electricity tariffs, supply code, or regulations.")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Render history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
if prompt := st.chat_input("e.g. What is the domestic tariff slab for UGVCL consumers above 100 units?"):

    if not api_key:
        st.warning("⚠️ Please enter your Claude API Key in the sidebar to continue.")
        st.stop()

    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Retrieve & answer
    relevant = retrieve(prompt, chunks)
    system_prompt = build_system(relevant)

    with st.chat_message("assistant"):
        try:
            client = anthropic.Anthropic(api_key=api_key)
            response_placeholder = st.empty()
            response_text = ""

            with client.messages.stream(
                model=MODEL,
                max_tokens=3000,
                system=system_prompt,
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
            ) as stream:
                for text in stream.text_stream:
                    response_text += text
                    response_placeholder.markdown(response_text + "▌")

            response_placeholder.markdown(response_text)
            st.session_state.messages.append(
                {"role": "assistant", "content": response_text}
            )

            # Show sources in expander
            if relevant:
                with st.expander(f"📚 {len(relevant)} source chunks used"):
                    for c in relevant:
                        st.caption(f"**{c['source']}**")
                        st.text(c["text"][:300] + "…")
                        st.divider()

        except anthropic.AuthenticationError:
            st.error("❌ Invalid API key. Please check your Claude API key in the sidebar.")
        except Exception as e:
            st.error(f"❌ Error: {e}")
