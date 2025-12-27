import streamlit as st

st.title("Small YouTube Player")
st.button("Play YouTube Video", key="play_button")
url = st.text_input("Enter YouTube URL")

if url:
    st.video(url)