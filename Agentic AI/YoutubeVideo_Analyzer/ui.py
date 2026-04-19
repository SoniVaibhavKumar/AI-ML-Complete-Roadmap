import streamlit as st
from youtube_analyzer import analyze_video

st.set_page_config(page_title="YouTube Analyzer")

st.title("🎥 AI YouTube Video Analyzer")

url = st.text_input("Enter YouTube URL")

if st.button("Analyze Video"):
    if url:
        with st.spinner("Analyzing..."):
            result = analyze_video(url)
            st.markdown(result)