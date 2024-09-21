import os
from dotenv import load_dotenv

load_dotenv()

def get_openai_api_key():
    return os.getenv("OPENAI_API_KEY")

def get_youtube_api_key():
    return os.getenv("YOUTUBE_API_KEY")
