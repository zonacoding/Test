import streamlit as st
from googleapiclient.discovery import build

st.title("Small YouTube Player")

api_key = st.text_input("Enter YouTube API Key", type="password")

if api_key:
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    def get_top_videos():
        request = youtube.search().list(
            part='snippet',
            order='viewCount',
            type='video',
            maxResults=10
        )
        response = request.execute()
        videos = []
        for item in response['items']:
            title = item['snippet']['title']
            video_id = item['id']['videoId']
            url = f"https://www.youtube.com/watch?v={video_id}"
            videos.append((title, url))
        return videos
    
    if st.button("Get Top 10 Most Viewed Videos"):
        videos = get_top_videos()
        video_options = [title for title, url in videos]
        selected_video = st.selectbox("Select a video to play", video_options)
        if selected_video:
            for title, url in videos:
                if title == selected_video:
                    st.video(url)
                    break

url = st.text_input("Or Enter YouTube URL directly")

if url:
    st.video(url)