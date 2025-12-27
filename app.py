import streamlit as st
from googleapiclient.discovery import build

st.title("TOP 10 Player")

api_key = "AIzaSyDFizCwEES-oJ7IvxgYIwFrKzWroNxRrJY"

def get_embed_url(url):
    if 'youtube.com/watch?v=' in url:
        video_id = url.split('v=')[1].split('&')[0]
        return f"https://www.youtube.com/embed/{video_id}?autoplay=1"
    return url

if 'videos' not in st.session_state:
    st.session_state.videos = []

if api_key:
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    def get_top_videos():
        try:
            request = youtube.videos().list(
                part='snippet',
                chart='mostPopular',
                regionCode='KR',
                maxResults=10
            )
            response = request.execute()
            videos = []
            for item in response['items']:
                title = item['snippet']['title']
                video_id = item['id']
                url = f"https://www.youtube.com/embed/{video_id}?autoplay=1"
                videos.append((title, url))
            return videos
        except Exception as e:
            st.error(f"Error fetching videos: {e}")
            return []
    

    videos = get_top_videos()
    st.session_state.videos = videos
    
    if st.session_state.videos:
        video_options = [title for title, url in st.session_state.videos]
        selected_video = st.selectbox("Select a video to play", video_options)
        for title, url in st.session_state.videos:
            if title == selected_video:
                st.video(url)
                print(url)
                break

url = st.text_input("Or Enter YouTube URL directly")

if url:
    st.video(get_embed_url(url))