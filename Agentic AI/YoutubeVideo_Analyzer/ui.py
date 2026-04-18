import streamlit as st
from youtube_analyzer import build_youtube_agent

st.set_page_config(page_title="Youtube Video Analyzer")

st.title("🎥 AI Youtube Video Analyzer")

st.write("App started successfully ✅")

video_url = st.text_input("Enter Youtube Video Link")

if st.button("Analyze Video"):
    st.write("Creating agent...")
    agent = build_youtube_agent()

    st.write("Running analysis...")
    response = agent.run(f"Summarize this video briefly: {video_url}")

    st.write(response.content)