import openai
from common.openaiapi_helper import get_openai_api_key

def create_embeddings(text):
    openai.api_key = get_openai_api_key()
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response['data'][0]['embedding']
