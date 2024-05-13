import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

# Load environment variables
load_dotenv()

# Get the YouTube Data API key from environment variable
youtube_api_key = os.environ.get("YOUTUBE_DATA_API_KEY")

# Function to fetch video data from YouTube API
def fetch_video_data(video_id):
    youtube = build('youtube', 'v3', developerKey=youtube_api_key)
    request = youtube.videos().list(part='snippet', id=video_id)
    response = request.execute()
    return response

# Example usage
video_id = "your_youtube_video_id"
video_data = fetch_video_data(video_id)
print(video_data)
