import os
from dotenv import load_dotenv
from pathway.stdlib.ml.index import KNNIndex
from common.openaiapi_helper import openai_embedder

# Load environment variables
load_dotenv()

# Get embedding dimension from environment variable, default to 1536 if not provided
embedding_dimension = int(os.environ.get("EMBEDDING_DIMENSION", 1536))


def embeddings(context, data_to_embed):
    """
    Compute embeddings for the given data using OpenAI Embeddings API.

    Parameters:
        context: Contextual information for the embeddings.
        data_to_embed: Data to be embedded.

    Returns:
        Embedded data.
    """
    return context + context.select(vector=openai_embedder(data_to_embed))


def index_embeddings(embedded_data):
    """
    Index the embeddings for efficient retrieval.

    Parameters:
        embedded_data: Embedded data to be indexed.

    Returns:
        Index for the embedded data.
    """
    return KNNIndex(embedded_data.vector, embedded_data, n_dimensions=embedding_dimension)
