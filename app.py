import streamlit as st
import requests
import anthropic
import re
from collections import Counter

# ── Config ──────────────────────────────────────────────────────────────────
REPO_OWNER = "gtanalytics2030"
REPO_NAME  = "energybot-knowledge-base"
BRANCH     = "main"
MODEL      = "claude-haiku-4-5-20251001"   # fast & cheap; change to claude-sonnet-4-6 for deeper answers
TOP_K      = 8                              # how many chunks to retrieve per query

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
def _score(chunk_text: str, query: str) -> float:
    """Simple TF-style keyword overlap score."""
    qwords = {w for w in re.findall(r"[a-zA-Z0-9₹]+", query.lower()) if len(w) > 2}
    cwords = Counter(re.findall(r"[a-zA-Z0-9₹]+", chunk_text.lower()))
    return sum(cwords.get(w, 0) for w in qwords)


def retrieve(query: str, chunks: list, top_k: int = TOP_K) -> list:
    scored = sorted(chunks, key=lambda c: _score(c["text"], query), reverse=True)
    return [c for c in scored[:top_k] if _score(c["text"], query) > 0]


# ── Build system prompt ───────────────────────────────────────────────────────
SYSTEM_BASE = """You are EnergyBot, a knowledgeable assistant specialising in:
• GERC (Gujarat Electricity Regulatory Commission) regulations
• Electricity Act 2003 (EA 2003)
• Tariff schedules for DISCOMs, AIVPL, TPL, GIFT PCL, MUL (FY 2026-27)
• Standards of Performance for DISCOMs
• GERC Supply Code

Rules:
## 1. Response & Multilingual Policy
- Language Agility: You must detect the language of the user's query and respond natively in that exact language (e.g., English, Gujarati, Hindi, etc.). 
- Professional Tone: Maintain a highly professional, objective, legal, and authoritative tone.
- Absolute Grounding (No Hallucinations): If the answer cannot be found within the provided context or documents, explicitly state: "I am sorry, but the provided regulatory documents do not contain information to answer this query safely." Do not invent facts, numbers, or clauses.

---

## 2. Strict Citation Formatting
Every factual claim, timeline, penalty, or tariff rate MUST be accompanied by an inline citation and a reference block at the bottom. 
- Inline Format: ...as per [Document Name, Clause/Section X.X].
- End of Response Format: Provide a clean "References & Citations" list.
- Example: "As per [GERC Supply Code 2015, Clause 4.12], a new connection must be released within 15 days..."

---

## 3. Response Architecture
Structure every response exactly as follows:

### [Clear, Concise Direct Answer]
(Give a direct, plain-language summary of the rule/law/tariff in the user's language.)

### Detailed Breakdown & Conditions
(Bullet points detailing specific timelines, financial penalties, tariff rates, or step-by-step compliance rules.)

### References & Citations
- **Statute/Regulation:** [Exact Section/Clause]
- **Document:** [Name of the Document]

---

## 4. Related Question Generation
At the very end of your response, separate the section with a horizontal rule (`---`) and provide exactly 3 relevant, logical, and helpful follow-up questions labeled as "Suggested Questions:". These questions should guide the consumer or professional to the next logical step (e.g., if they ask about a new connection timeline, suggest questions about penalties for delay or required documents).
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

    api_key = st.text_input(
        "🔑 Claude API Key",
        type="password",
        placeholder="sk-ant-...",
        help="Get yours at console.anthropic.com",
    )

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
                max_tokens=1500,
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
