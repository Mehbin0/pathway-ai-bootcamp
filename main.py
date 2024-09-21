import pathway as pw
from pathway.stdlib.ml.index import KNNIndex
import openai
from googleapiclient.discovery import build
from urllib.parse import urlparse, parse_qs
from common.embedder import create_embeddings
from common.openaiapi_helper import get_openai_api_key, get_youtube_api_key
from common.prompt import SYSTEM_PROMPT, generate_user_prompt

def get_user_input():
    video_url = input("Please enter the YouTube video URL: ")
    
    # Extract video ID from URL
    parsed_url = urlparse(video_url)
    video_id = parse_qs(parsed_url.query).get('v', [None])[0]
    if not video_id:
        print("Invalid YouTube URL. Please provide a valid URL.")
        exit(1)
    
    return video_id

def setup_apis():
    openai.api_key = get_openai_api_key()
    youtube = build("youtube", "v3", developerKey=get_youtube_api_key())
    return youtube

def get_video_transcript(youtube, video_id):
    try:
        request = youtube.videos().list(part="snippet", id=video_id)
        response = request.execute()
        return response['items'][0]['snippet']['description']
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def generate_response(query, context):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": generate_user_prompt(context, query)}
        ]
    )
    return response.choices[0].message['content']

def process_video(youtube, video_id):
    transcript = get_video_transcript(youtube, video_id)
    if not transcript:
        return pw.Table.empty()

    chunks = [transcript[i:i+100] for i in range(0, len(transcript), 100)]
    table = pw.Table.from_pylist([{"chunk": chunk} for chunk in chunks])
    table += table.select(embedding=pw.apply(create_embeddings, pw.this.chunk))
    index = KNNIndex(table.embedding)
    return table, index

def answer_query(query, index):
    query_embedding = create_embeddings(query)
    similar_chunks = index.query(query_embedding, k=3)
    context = " ".join([chunk.chunk for chunk in similar_chunks])
    response = generate_response(query, context)
    return response

def chatbot(youtube, video_id):
    table, index = process_video(youtube, video_id)

    while True:
        user_query = input("Enter your question (or 'quit' to exit): ")
        if user_query.lower() == 'quit':
            break

        response = answer_query(user_query, index)
        print(f"Response: {response}\n")

def main():
    video_id = get_user_input()
    youtube = setup_apis()
    chatbot(youtube, video_id)

if __name__ == "__main__":
    main()
