import streamlit as st

from pdf_parser import extract_text
from gemini_analyzer import analyze_resume

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖"
)

st.title("🤖 AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("Resume Uploaded Successfully!")

    resume_text = extract_text(uploaded_file)

    st.subheader("Resume Text")

    st.write(resume_text)

    with st.spinner("AI is analyzing your resume..."):

        result = analyze_resume(resume_text)

    st.subheader("AI Analysis")

    st.write(result)