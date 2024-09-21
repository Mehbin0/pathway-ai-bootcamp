import pathway as pw
from pathway.stdlib.ml.index import KNNIndex
import openai
from googleapiclient.discovery import build
from common.config import OPENAI_API_KEY, YOUTUBE_API_KEY

openai.api_key = OPENAI_API_KEY

def get_video_transcript(video_id):
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    try:
        request = youtube.videos().list(part="snippet", id=video_id)
        response = request.execute()
        return response['items'][0]['snippet']['description']
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def create_embeddings(text):
    response = openai.Embedding.create(input=text, model="text-embedding-ada-002")
    return response['data'][0]['embedding']

def generate_response(query, context):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions based on the given context."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {query}"}
        ]
    )
    return response.choices[0].message['content']

def process_video(video_id):
    transcript = get_video_transcript(video_id)
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
