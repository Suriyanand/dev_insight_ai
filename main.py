import streamlit as st
from analyzer import analyze_repo
from llm_module import get_llm_feedback

st.title("🔍 DevInsight AI – GitHub Repository Analyzer")

repo_url = st.text_input("Enter GitHub Repository URL")

if st.button("Analyze"):
    if "github.com" not in repo_url:
        st.error("Please enter a valid GitHub URL.")
    else:
        with st.spinner("Analyzing repository..."):
            repo_data = analyze_repo(repo_url)
            feedback = get_llm_feedback(repo_data)
        
        st.subheader("📦 Repo Summary")
        st.json(repo_data)

        st.subheader("🧠 LLM Insights")
        st.markdown(feedback)
