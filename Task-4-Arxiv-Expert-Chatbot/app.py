import streamlit as st
from arxiv_loader import load_arxiv_data
from chatbot import ArxivChatbot

# --------------------
# PAGE SETTINGS
# --------------------

st.set_page_config(
    page_title="Arxiv Expert Chatbot",
    page_icon="📚",
    layout="wide"
)

# --------------------
# TITLE
# --------------------

st.title("📚 Arxiv Expert Chatbot")
st.markdown(
    "Search and explore Computer Science research papers from arXiv."
)

# --------------------
# SESSION HISTORY
# --------------------

if "history" not in st.session_state:
    st.session_state.history = []

# --------------------
# LOAD DATA
# --------------------

@st.cache_data
def get_data():

    return load_arxiv_data(
        "dataset/arxiv-metadata-oai-snapshot.json"
    )

df = get_data()

# --------------------
# CHATBOT
# --------------------

bot = ArxivChatbot(df)

# --------------------
# SIDEBAR
# --------------------

st.sidebar.title("📜 Search History")

for item in st.session_state.history:
    st.sidebar.write("• " + item)

# --------------------
# SEARCH BOX
# --------------------

query = st.text_input(
    "🔍 Ask a Research Question",
    placeholder="machine learning, neural networks, computer vision..."
)

# --------------------
# SUMMARY FUNCTION
# --------------------

def summarize(text):

    if not text:
        return ""

    sentences = text.split(".")

    return ".".join(sentences[:3]) + "."

# --------------------
# SEARCH RESULTS
# --------------------

if query:

    st.session_state.history.append(query)

    results = bot.search(query)

    st.success(
        f"Found {len(results)} Relevant Papers"
    )

    for i, (_, paper) in enumerate(
        results.iterrows(),
        start=1
    ):

        with st.expander(
            f"📄 Paper {i}: {paper['title']}"
        ):

            st.subheader("👨‍🔬 Authors")
            st.write(paper["authors"])

            st.subheader("🏷 Categories")
            st.write(paper["categories"])

            st.subheader("📝 Quick Summary")
            st.info(
                summarize(
                    paper["abstract"]
                )
            )

            st.subheader("📚 Full Abstract")
            st.write(
                paper["abstract"]
            )