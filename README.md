# Small YouTube Player

A simple Streamlit app to play YouTube videos by entering the URL or selecting from top viewed videos.

## Features

- Play videos by URL
- List and play top 10 most popular videos in Korea (requires YouTube API key)

## Setup YouTube API

1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select existing.
3. Enable the YouTube Data API v3.
4. Create credentials: API key.
5. Copy the API key.

## How to Run Locally

1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `streamlit run app.py`
3. Enter your YouTube API key in the app.

## Deployment

This app is deployed on Streamlit Cloud. To deploy your own version:

1. Push this repository to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account.
4. Select this repository and the main file (app.py).
5. In the advanced settings, add your YouTube API key as a secret named `YOUTUBE_API_KEY`.
6. Update the code to use `st.secrets["YOUTUBE_API_KEY"]` instead of text input.
7. Deploy!