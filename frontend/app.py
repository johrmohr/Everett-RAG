"""
Streamlit frontend for Everett RAG system
A conversational interface to explore Hugh Everett's manuscripts
"""
import os
import streamlit as st
import requests
from pathlib import Path
from typing import List, Dict, Any

# Page configuration
st.set_page_config(
    page_title="Everett Manuscripts Explorer",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide sidebar completely
st.markdown("""
<style>
    [data-testid="stSidebar"] {display: none;}
    [data-testid="stSidebarNav"] {display: none;}
    .stSidebar {display: none;}
    section[data-testid="stSidebar"] {display: none !important;}
</style>
""", unsafe_allow_html=True)

# Paths
MANUSCRIPTS_DIR = Path(__file__).parent.parent / "transcribed_everett_manuscripts"

# Custom CSS - Black Theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Crimson+Pro:ital,wght@0,400;0,600;1,400&family=JetBrains+Mono:wght@400;500&display=swap');
    
    /* Hide Streamlit elements */
    #MainMenu, footer, header, .stDeployButton { visibility: hidden; display: none; }
    
    .stApp {
        background: #2a2a2a;
    }
    
    .block-container {
        padding-top: 0 !important;
        max-width: 1200px !important;
    }
    
    /* ===== HEADER ===== */
    .site-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1.25rem 2rem;
        background: #2a2a2a;
        border-bottom: 1px solid #4a4a4a;
        margin: -1rem -1rem 2rem -1rem;
    }
    
    .logo {
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }
    
    .logo-icon {
        width: 36px;
        height: 36px;
        background: #d4c4a8;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.1rem;
    }
    
    .logo-text {
        font-family: 'Inter', sans-serif;
        font-size: 1.4rem;
        font-weight: 600;
        color: #ffffff;
        letter-spacing: -0.02em;
    }
    
    .header-spacer {
        width: 120px;
    }
    
    /* Radio navigation styling */
    div[data-testid="stRadio"] > div {
        gap: 2.5rem !important;
        background: transparent !important;
        justify-content: center !important;
        flex-wrap: nowrap !important;
    }
    
    div[data-testid="stRadio"] > div > label {
        background: transparent !important;
        border: none !important;
        padding: 0.5rem 0 !important;
        margin: 0 !important;
    }
    
    div[data-testid="stRadio"] > div > label > div:first-child {
        display: none !important;
    }
    
    div[data-testid="stRadio"] > div > label > div:last-child {
        font-family: 'Inter', sans-serif !important;
        font-size: 0.95rem !important;
        font-weight: 500 !important;
        color: #888888 !important;
    }
    
    div[data-testid="stRadio"] > div > label:hover > div:last-child {
        color: #ffffff !important;
    }
    
    div[data-testid="stRadio"] > div > label[data-checked="true"] > div:last-child {
        color: #ffffff !important;
    }
    
    /* Primary buttons */
    .stButton > button[kind="primary"] {
        background: #d4c4a8 !important;
        color: #1a1a1a !important;
        font-weight: 600 !important;
    }
    
    .stButton > button[kind="secondary"] {
        background: #d4c4a8 !important;
        color: #1a1a1a !important;
        font-weight: 600 !important;
    }
    
    /* ===== MAIN CONTENT ===== */
    .main-title {
        font-family: 'Crimson Pro', Georgia, serif;
        font-size: 2.8rem;
        font-weight: 600;
        color: #ffffff;
        text-align: center;
        margin: 2rem 0 0.5rem 0;
    }
    
    .sub-title {
        font-family: 'Crimson Pro', Georgia, serif;
        font-size: 1.15rem;
        color: #888888;
        text-align: center;
        font-style: italic;
        margin-bottom: 2.5rem;
    }
    
    /* ===== CHAT ===== */
    .user-msg {
        background: #3a3a3a;
        border-left: 3px solid #4a9eff;
        padding: 1rem 1.25rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
        font-family: 'Crimson Pro', Georgia, serif;
        font-size: 1.05rem;
        color: #ffffff;
    }

    .assistant-msg {
        background: #333333;
        border-left: 3px solid #d4c4a8;
        padding: 1.25rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
        font-family: 'Crimson Pro', Georgia, serif;
        font-size: 1.05rem;
        line-height: 1.8;
        color: #ffffff;
    }
    
    .stTextInput > div > div > input {
        background: #3a3a3a !important;
        border: 1px solid #4a4a4a !important;
        color: #ffffff !important;
        border-radius: 8px !important;
        font-family: 'Crimson Pro', Georgia, serif !important;
    }
    
    .stButton > button {
        background: #d4c4a8 !important;
        color: #000000 !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    .stButton > button:hover {
        background: #c4b494 !important;
    }
    
    /* ===== CARDS ===== */
    .insight-card {
        background: #3a3a3a;
        border: 1px solid #4a4a4a;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    .insight-question {
        font-family: 'Crimson Pro', Georgia, serif;
        font-size: 1.25rem;
        font-weight: 600;
        color: #d4c4a8;
        margin-bottom: 0.75rem;
    }
    
    .insight-answer {
        font-family: 'Crimson Pro', Georgia, serif;
        font-size: 1.05rem;
        line-height: 1.8;
        color: #ffffff;
    }
    
    /* ===== DOCUMENT VIEWER ===== */
    .doc-content {
        background: #3a3a3a;
        border: 1px solid #4a4a4a;
        border-radius: 8px;
        padding: 1.5rem;
        font-family: 'Crimson Pro', Georgia, serif;
        font-size: 1rem;
        line-height: 1.9;
        color: #ffffff;
        max-height: 60vh;
        overflow-y: auto;
    }
    
    /* ===== STATS ===== */
    .stat-box {
        background: #3a3a3a;
        border: 1px solid #4a4a4a;
        border-radius: 8px;
        padding: 1.25rem;
        text-align: center;
    }
    
    .stat-number {
        font-family: 'JetBrains Mono', monospace;
        font-size: 1.75rem;
        font-weight: 600;
        color: #d4c4a8;
    }
    
    .stat-label {
        font-family: 'Inter', sans-serif;
        font-size: 0.8rem;
        color: #666666;
        margin-top: 0.25rem;
    }
    
    /* ===== SECTION HEADERS ===== */
    .section-header {
        font-family: 'Crimson Pro', Georgia, serif;
        font-size: 1.5rem;
        font-weight: 600;
        color: #d4c4a8;
        margin: 2rem 0 1rem 0;
    }
    
    .section-text {
        font-family: 'Crimson Pro', Georgia, serif;
        font-size: 1.05rem;
        line-height: 1.9;
        color: #ffffff;
        margin-bottom: 1rem;
    }
    
    .highlight-box {
        background: rgba(200, 230, 80, 0.12);
        border-left: 3px solid #d4c4a8;
        padding: 1rem 1.25rem;
        margin: 1rem 0;
        border-radius: 0 8px 8px 0;
    }

    .highlight-box p {
        font-family: 'Crimson Pro', Georgia, serif;
        font-size: 1.05rem;
        line-height: 1.8;
        color: #ffffff;
        margin: 0;
    }
    
    .quote-block {
        border-left: 3px solid #8b5cf6;
        padding-left: 1.25rem;
        margin: 1.5rem 0;
        font-family: 'Crimson Pro', Georgia, serif;
        font-style: italic;
        font-size: 1.1rem;
        color: #ffffff;
    }
    
    .tech-badge {
        display: inline-block;
        background: #3a3a3a;
        border: 1px solid #4a4a4a;
        border-radius: 6px;
        padding: 0.4rem 0.8rem;
        margin: 0.2rem;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.8rem;
        color: #4a9eff;
    }
    
    .timeline-row {
        display: flex;
        gap: 1.5rem;
        padding: 0.75rem 0;
        border-left: 2px solid #4a4a4a;
        padding-left: 1rem;
        margin-left: 0.5rem;
    }

    .timeline-year {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.9rem;
        color: #d4c4a8;
        min-width: 60px;
    }

    .timeline-text {
        font-family: 'Crimson Pro', Georgia, serif;
        font-size: 1rem;
        color: #ffffff;
    }
    
    /* Dividers */
    hr {
        border: none;
        border-top: 1px solid #4a4a4a;
        margin: 2rem 0;
    }

    /* Footer */
    .footer-quote {
        text-align: center;
        padding: 2rem;
        border-top: 1px solid #4a4a4a;
        margin-top: 3rem;
    }

    .footer-quote p {
        font-family: 'Crimson Pro', Georgia, serif;
        font-style: italic;
        color: #cccccc;
        font-size: 1.1rem;
    }
    
    .footer-attr {
        color: #d4c4a8;
        font-size: 0.95rem;
        margin-top: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# API configuration
# API URL - configurable via environment variable for deployment
API_URL = os.getenv("API_URL", "http://localhost:8000")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "sources" not in st.session_state:
    st.session_state.sources = {}
if "current_view" not in st.session_state:
    st.session_state.current_view = "chat"


def query_rag(message: str) -> Dict[str, Any]:
    """Send a query to the RAG API."""
    try:
        response = requests.post(
            f"{API_URL}/chat",
            json={"message": message, "include_sources": True},
            timeout=60
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        return {"error": "Cannot connect to the RAG API. Make sure the server is running."}
    except Exception as e:
        return {"error": str(e)}


def clear_conversation():
    st.session_state.messages = []
    st.session_state.sources = {}
    try:
        requests.post(f"{API_URL}/conversation/clear", timeout=10)
    except:
        pass


def get_manuscripts() -> List[Dict[str, str]]:
    manuscripts = []
    if MANUSCRIPTS_DIR.exists():
        for f in sorted(MANUSCRIPTS_DIR.glob("*.md")):
            name = f.stem
            doc_type = "Other"
            if "Handwritten" in name:
                doc_type = "Handwritten"
            elif " to " in name:
                doc_type = "Letter"
            elif "thesis" in name.lower():
                doc_type = "Thesis"
            
            year = "—"
            for y in range(1950, 1990):
                if str(y) in name:
                    year = str(y)
                    break
            
            manuscripts.append({
                "filename": f.name,
                "title": name,
                "type": doc_type,
                "year": year,
                "path": str(f)
            })
    return manuscripts


# ===== HEADER =====
# Map view keys to labels
view_map = {"Chat": "chat", "Insights": "insights", "Archive": "docs", "About": "about"}
reverse_map = {v: k for k, v in view_map.items()}
current_label = reverse_map.get(st.session_state.current_view, "Chat")

# Header row - logo left, nav centered
col_logo, col_nav, col_space = st.columns([2.5, 3, 2.5])

with col_logo:
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 0.75rem; padding: 0.5rem 0;">
        <div style="width: 36px; height: 36px; background: #d4c4a8; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 1.1rem;">⚛</div>
        <span style="font-family: 'Inter', sans-serif; font-size: 1.4rem; font-weight: 600; color: #ffffff; letter-spacing: -0.02em;">Everett.</span>
    </div>
    """, unsafe_allow_html=True)

with col_nav:
    selected = st.radio(
        "nav",
        options=list(view_map.keys()),
        index=list(view_map.keys()).index(current_label),
        horizontal=True,
        label_visibility="collapsed"
    )

# Update view if changed
if view_map[selected] != st.session_state.current_view:
    st.session_state.current_view = view_map[selected]
    st.rerun()

st.markdown('<hr style="border: none; border-top: 1px solid #4a4a4a; margin: 0 0 2rem 0;">', unsafe_allow_html=True)


# ===== CHAT VIEW =====
def render_chat():
    st.markdown('<h1 class="main-title">Explore the Everett Archives</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">"The theory is in full accord with experience..." — Hugh Everett III, 1957</p>', unsafe_allow_html=True)
    
    for i, msg in enumerate(st.session_state.messages):
        if msg["role"] == "user":
            st.markdown(f'<div class="user-msg">{msg["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="assistant-msg">{msg["content"]}</div>', unsafe_allow_html=True)
            if i in st.session_state.sources and st.session_state.sources[i]:
                with st.expander(f"📚 View {len(st.session_state.sources[i])} sources"):
                    for source in st.session_state.sources[i]:
                        st.markdown(f"**{source['title']}** — Relevance: {source['relevance']:.2f}")
                        st.caption(f"_{source['excerpt'][:200]}..._")
    
    col1, col2 = st.columns([6, 1])
    with col1:
        user_input = st.text_input(
            "Ask about Everett's manuscripts...",
            placeholder="e.g., How did Everett explain wave function collapse?",
            key="user_input",
            label_visibility="collapsed"
        )
    with col2:
        send = st.button("Send", use_container_width=True)
    
    if send and user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.spinner("Searching manuscripts..."):
            result = query_rag(user_input)
        if "error" in result:
            st.session_state.messages.append({"role": "assistant", "content": f"⚠️ {result['error']}"})
        else:
            st.session_state.messages.append({"role": "assistant", "content": result["answer"]})
            st.session_state.sources[len(st.session_state.messages) - 1] = result.get("sources", [])
        st.rerun()
    
    if not st.session_state.messages:
        st.markdown("### 💡 Try asking:")
        examples = [
            "What was Everett's key insight about measurement?",
            "How did Wheeler respond to Everett's thesis?",
            "What is the 'relative state' formulation?",
            "What criticisms did Everett's theory face?",
        ]
        cols = st.columns(2)
        for i, q in enumerate(examples):
            with cols[i % 2]:
                if st.button(q, key=f"ex_{i}", use_container_width=True):
                    st.session_state.messages.append({"role": "user", "content": q})
                    with st.spinner("Searching..."):
                        result = query_rag(q)
                    if "error" not in result:
                        st.session_state.messages.append({"role": "assistant", "content": result["answer"]})
                        st.session_state.sources[len(st.session_state.messages) - 1] = result.get("sources", [])
                    st.rerun()
        
        st.markdown("---")
        if st.button("🗑️ Clear Conversation"):
            clear_conversation()
            st.rerun()


# ===== INSIGHTS VIEW =====
def render_insights():
    st.markdown('<h1 class="main-title">Insights from the Archive</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Key findings extracted from 224 primary source documents</p>', unsafe_allow_html=True)
    
    insights = [
        {
            "q": "What happened to the original 137-page thesis?",
            "a": "Wheeler felt the original wording could lead to 'misunderstandings' and urged Everett to condense it. The full version wasn't published until DeWitt's 1973 anthology."
        },
        {
            "q": "What was Wheeler doing behind the scenes?",
            "a": "Wheeler paid from his own research budget to send Everett to Copenhagen to 'struggle it out in person with Bohr.' He later insisted it be called the 'Everett interpretation,' not the 'Everett-Wheeler' interpretation."
        },
        {
            "q": "What did Everett believe about consciousness?",
            "a": "Everett used 'observer' and 'automaton' interchangeably. He saw no distinction between 'consciousness' and 'the contents of a memory bank' — a remarkably modern, computational view of mind."
        },
        {
            "q": "What was DeWitt's famous objection?",
            "a": "DeWitt wrote an eleven-page letter 'alternately praising and damning' Everett, insisting 'I do not feel myself split.' He would later become the interpretation's greatest champion."
        },
    ]
    
    for item in insights:
        st.markdown(f"""
        <div class="insight-card">
            <div class="insight-question">❓ {item['q']}</div>
            <div class="insight-answer">{item['a']}</div>
        </div>
        """, unsafe_allow_html=True)


# ===== DOCUMENTS VIEW =====
def render_documents():
    st.markdown('<h1 class="main-title">Document Archive</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Browse the full collection of 224 transcribed manuscripts</p>', unsafe_allow_html=True)
    
    manuscripts = get_manuscripts()
    if not manuscripts:
        st.error("No manuscripts found.")
        return
    
    col1, col2, col3 = st.columns([2, 2, 3])
    with col1:
        types = ["All"] + sorted(set(m["type"] for m in manuscripts))
        selected_type = st.selectbox("Type", types)
    with col2:
        years = ["All"] + sorted(set(m["year"] for m in manuscripts if m["year"] != "—"))
        selected_year = st.selectbox("Year", years)
    with col3:
        search = st.text_input("Search", placeholder="Search titles...")
    
    filtered = [
        m for m in manuscripts
        if (selected_type == "All" or m["type"] == selected_type)
        and (selected_year == "All" or m["year"] == selected_year)
        and (not search or search.lower() in m["title"].lower())
    ]
    
    st.caption(f"Showing {len(filtered)} of {len(manuscripts)} documents")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        for doc in filtered[:50]:
            if st.button(f"{doc['title'][:40]}...", key=doc['filename'], use_container_width=True):
                st.session_state.selected_doc = doc
    
    with col2:
        if hasattr(st.session_state, 'selected_doc') and st.session_state.selected_doc:
            doc = st.session_state.selected_doc
        elif filtered:
            doc = filtered[0]
        else:
            doc = None
        
        if doc:
            st.markdown(f"### {doc['title']}")
            st.caption(f"**Type:** {doc['type']} | **Year:** {doc['year']}")
            
            try:
                with open(doc['path'], 'r', encoding='utf-8') as f:
                    content = f.read()
                st.markdown(f'<div class="doc-content">{content[:5000]}{"..." if len(content) > 5000 else ""}</div>', unsafe_allow_html=True)
                st.download_button("Download", content, doc['filename'], "text/markdown")
            except Exception as e:
                st.error(f"Error: {e}")


# ===== ABOUT VIEW =====
def render_about():
    st.markdown('<h1 class="main-title">About This Project</h1>', unsafe_allow_html=True)

    st.markdown("""
    <p class="section-text">
    This project is designed to explore the intellectual history of <strong>Hugh Everett III</strong>, the physicist who fundamentally changed our understanding of reality. By combining modern OCR technology with Retrieval-Augmented Generation (RAG), this system allows researchers and enthusiasts to converse with Everett's private manuscripts, drafts, and personal correspondence.
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<h2 class="section-header">Hugh Everett III & the Many-Worlds Interpretation</h2>', unsafe_allow_html=True)
    st.markdown("""
    <p class="section-text">
    <strong>Hugh Everett III</strong> (1930–1982) was an American physicist who, as a graduate student at Princeton in 1956, proposed the Relative State formulation of quantum mechanics.
    </p>
    <p class="section-text">
    In an era dominated by the Copenhagen Interpretation, which argued that the act of observation "collapses" a quantum wave into a single reality, Everett proposed something radical: the wave function never collapses. Instead, it continues to evolve, and every possible outcome of a quantum event occurs in a branching series of relative states.
    </p>
    <p class="section-text">
    While his theory was largely ignored or ridiculed during his life, leading him to leave academia for a career in military defense analysis, it was later popularized as the <strong>Many-Worlds Interpretation (MWI)</strong>. Today, it is considered one of the most important and controversial pillars of modern physics.
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<h2 class="section-header">The Archive</h2>', unsafe_allow_html=True)
    st.markdown("""
    <p class="section-text">
    For decades, many of Everett's original thoughts were hidden from the public. In 2007, investigative journalist <a href="https://www.peterbyrne.info" target="_blank" style="color: #4a9eff;"><strong>Peter Byrne</strong></a> discovered a trove of documents in the Los Feliz basement of Everett's son, Mark Oliver Everett (the lead singer of the band Eels).
    </p>
    <p class="section-text">
    These documents were preserved, digitized, and organized through a collaborative effort led by <a href="https://faculty.sites.uci.edu/jeffreybarrett/" target="_blank" style="color: #4a9eff;"><strong>Jeffrey A. Barrett</strong></a> (UC Irvine), alongside Peter Byrne, <a href="https://jamesowenweatherall.com" target="_blank" style="color: #4a9eff;"><strong>James O. Weatherall</strong></a> (UC Irvine), and <a href="https://samuelcfletcher.com" target="_blank" style="color: #4a9eff;"><strong>Samuel C. Fletcher</strong></a> (University of Minnesota). This archival project was supported by the University of California and the National Science Foundation. The digital collection includes:
    </p>
    <ul class="section-text" style="margin-left: 1.5rem; color: #b0b0b0;">
        <li><strong>The Long Thesis:</strong> The original, 137-page unedited draft of Everett's work, which contains philosophical metaphors and mathematical proofs that were sanitized or removed for his final 1957 publication.</li>
        <li><strong>Handwritten minipapers:</strong> Early, raw notes where Everett first wrestled with the problem of probability and observers.</li>
        <li><strong>Correspondence:</strong> Private letters between Everett, his advisor John Wheeler, and other physicists like Niels Bohr and Bryce DeWitt.</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown('<h2 class="section-header">What is this RAG System?</h2>', unsafe_allow_html=True)
    st.markdown("""
    <p class="section-text">
    <strong>Retrieval-Augmented Generation (RAG)</strong> is an AI architecture that gives a Large Language Model (LLM) a long term memory composed of specific documents: in this case, the Everett Manuscripts.
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<h2 class="section-header">DeepSeek-OCR</h2>', unsafe_allow_html=True)
    st.markdown("""
    <p class="section-text">
    The primary challenge of this project was the nature of the source material: 1950s-era handwritten notes, faded typewritten drafts, and complex mathematical notation. Traditional OCR tools often fail on these documents due to noise, low contrast, and non-standard layouts.
    </p>
    <p class="section-text">
    To solve this, I utilized <a href="https://huggingface.co/deepseek-ai/DeepSeek-OCR" target="_blank" style="color: #4a9eff;"><strong>DeepSeek-OCR</strong></a>, a cutting-edge Vision-Language Model (VLM). Unlike standard OCR, DeepSeek-OCR treats the entire page as a visual context, allowing it to "read" Everett's unique cursive and technical shorthand with high fidelity. It was specifically chosen for its ability to recognize and format scientific notation (LaTeX), ensuring that Everett's crucial derivations for the "Universal Wavefunction" remained intact during transcription. The model outputs Markdown, preserving the logical structure of the manuscripts including headers, bullet points, and equations, which is essential for the RAG system to understand the relationship between different ideas.
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<h2 class="section-header">Google Colab for Students</h2>', unsafe_allow_html=True)
    st.markdown("""
    <p class="section-text">
    This project would not have been possible without Google Colab for compute to process over 5,000 pages of high-resolution manuscript images. To keep the project accessible and cost-efficient, the pipeline was built and executed using their free compute available for students. For more information, see <a href="https://blog.google/outreach-initiatives/education/colab-higher-education/?s=09" target="_blank" style="color: #4a9eff;"><strong>here</strong></a>.
    </p>
    """, unsafe_allow_html=True)


# ===== RENDER =====
if st.session_state.current_view == "chat":
    render_chat()
elif st.session_state.current_view == "insights":
    render_insights()
elif st.session_state.current_view == "about":
    render_about()
else:
    render_documents()
