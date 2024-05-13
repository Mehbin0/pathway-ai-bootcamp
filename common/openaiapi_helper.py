from dotenv import load_dotenv
import os
import pathway as pw
from pathway.xpacks.llm.embedders import OpenAIEmbedder
from pathway.xpacks.llm.llms import OpenAIChat, prompt_chat_single_qa

# Load environment variables
load_dotenv()

# Get OpenAI API key from environment variable
api_key = os.environ.get("OPENAI_API_TOKEN", "")

# Get embedder locator and model locator from environment variables, default to provided values if not provided
embedder_locator = os.environ.get("EMBEDDER_LOCATOR", "text-embedding-ada-002")
model_locator = os.environ.get("MODEL_LOCATOR", "gpt-3.5-turbo")

# Get other model parameters from environment variables, default to provided values if not provided
max_tokens = int(os.environ.get("MAX_TOKENS", 200))
temperature = float(os.environ.get("TEMPERATURE", 0.0))


def openai_embedder(data):
    """
    Embed data using the OpenAI Embeddings API.

    Parameters:
        data: Data to be embedded.

    Returns:
        Embedded data.
    """
    embedder = OpenAIEmbedder(
        api_key=api_key,
        model=embedder_locator,
        retry_strategy=pw.asynchronous.FixedDelayRetryStrategy(),
        cache_strategy=pw.asynchronous.DefaultCache(),
    )

    return embedder(data)


def openai_chat_completion(prompt):
    """
    Get completion for a given prompt using the OpenAI Chat API.

    Parameters:
        prompt: Prompt for which completion is required.

    Returns:
        Completion response.
    """
    model = OpenAIChat(
        api_key=api_key,
        model=model_locator,
        temperature=temperature,
        retry_strategy=pw.asynchronous.FixedDelayRetryStrategy(),
        cache_strategy=pw.asynchronous.DefaultCache(),
        max_tokens=max_tokens,
    )

    return model(prompt_chat_single_qa(prompt))
