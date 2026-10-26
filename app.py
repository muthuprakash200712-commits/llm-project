import streamlit as st
import time
from src.rag_pipeline import ask_question

# =========================
# PAGE CONFIGURATION
# =========================

st.set_page_config(
    page_title="LLM Document Q&A",
    page_icon="🤖",
    layout="wide"
)

# =========================
# LOAD CUSTOM CSS
# =========================

try:
    with open("assets/styles.css", "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
except FileNotFoundError:
    st.warning("styles.css not found in assets folder.")

# =========================
# TITLE
# =========================

st.title("🤖 LLM Document Q&A System")

st.markdown("""
Upload a PDF document and ask questions from it.

The system will:
- Search the document
- Retrieve relevant information
- Generate an answer using Gemini
""")

# =========================
# FILE UPLOADER
# =========================

uploaded_file = st.file_uploader(
    "📄 Upload PDF Document",
    type=["pdf"]
)

# =========================
# QUESTION INPUT
# =========================

question = st.text_input(
    "❓ Ask a question from the document:"
)

# =========================
# GET ANSWER BUTTON
# =========================

if st.button("🚀 Get Answer"):

    if uploaded_file is None:
        st.warning("Please upload a PDF document first.")

    elif not question.strip():
        st.warning("Please enter a question.")

    else:
        try:

            with st.spinner("🔍 Searching document and generating answer..."):

                start_time = time.time()

                answer = ask_question(question)

                end_time = time.time()

            response_time = round(
                end_time - start_time,
                2
            )

            st.success("✅ Answer Found")

            st.markdown("### 📌 Answer")

            st.write(answer)

            st.info(
                f"⏱ Response Time: {response_time} seconds"
            )

        except Exception as e:

            st.error(
                f"❌ Error: {str(e)}"
            )

# =========================
# FOOTER
# =========================

st.markdown("---")
st.caption("Powered by RAG + FAISS + Gemini AI")
    
    