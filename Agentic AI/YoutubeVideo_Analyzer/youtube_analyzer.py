from groq import Groq
from youtube_transcript_api import YouTubeTranscriptApi
import streamlit as st
import re

def extract_video_id(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    if "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    return url

def analyze_video(url):
    video_id = extract_video_id(url)

    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    text = " ".join([item["text"] for item in transcript[:200]])

    client = Groq(api_key=st.secrets["GROQ_API_KEY"])

    prompt = f"""
    Analyze this YouTube video transcript.

    Give:
    1. Summary
    2. Key points
    3. Important learnings
    4. Final verdict

    Transcript:
    {text}
    """

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content