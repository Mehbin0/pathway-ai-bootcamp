# YouTube Chatbot

## Introduction
This project implements a chatbot that can answer queries based on the content of a YouTube video. The chatbot uses data from the video provided in the link and utilizes advanced natural language processing techniques to provide accurate responses to user queries.

## Features
- Utilizes OpenAI API for text embedding and model completion.
- Integrates with the YouTube API to fetch video data.
- Provides real-time responses to user queries.

## Demo
[Add a GIF or video demonstrating the chatbot in action]

## Prerequisites
Before running this project, ensure you have the following installed:
- Python 3.x
- Pip (Python package manager)
- OpenAI API key
- YouTube Data API key

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/youtube-chatbot.git
```
2. Navigate to the project directory:
```bash
cd youtube-chatbot
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Set up environment variables by creating a `.env` file in the root directory and filling it with your API keys and other configurations. Use the provided `.env.example` as a template.

## Usage
1. Start the Flask API:
```bash
python main.py
```
2. Run the Streamlit UI:
```bash
streamlit run ui.py
```
3. Access the UI in your browser at http://localhost:8501 and start asking questions about the YouTube video.

## Configuration
You can customize the behavior of the chatbot by modifying the environment variables in the `.env` file.

## Contributing
Contributions are welcome! Feel free to submit pull requests or open issues for any improvements or bug fixes.

## License
[Include license information]
