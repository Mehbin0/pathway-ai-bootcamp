#YouTube Video Chatbot

This project implements an interactive chatbot that can answer queries based on the content of a YouTube video. It uses Pathway for data processing, OpenAI for natural language processing, and the YouTube Data API for fetching video information.

## Prerequisites

- Python 3.9+
- OpenAI API key
- YouTube Data API key

## Installation

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your `.env` file with your API keys

## Usage

1. Run the chatbot: `python main.py`
2. When prompted, enter the URL of the YouTube video you want to analyze.
3. Ask questions about the video content. Type 'quit' to exit the chatbot.

## Docker

To run using Docker:

1. Build the image: `docker-compose build`
2. Run the container: `docker-compose up`
