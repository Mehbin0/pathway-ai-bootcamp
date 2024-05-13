import pathway as pw
from common.openaiapi_helper import openai_chat_completion


def prompt(index, embedded_query, user_query):
    """
    Generate a prompt and obtain a response from the chatbot model.

    Parameters:
        index: Index of embeddings for efficient retrieval.
        embedded_query: Embedded query from the user.
        user_query: Original query from the user.

    Returns:
        Response from the chatbot model.
    """
    @pw.udf
    def build_prompt(local_indexed_data, query):
        docs_str = "\n".join(local_indexed_data)
        prompt = f"Given the following data: \n {docs_str} \nanswer this query: {query}"
        return prompt
    
    # Generate a prompt using the indexed data and the user query
    prompt = index.select(
        prompt=build_prompt(pw.this.local_indexed_data_list, user_query)
    )

    # Obtain completion for the generated prompt from the chatbot model
    response = prompt.select(
        query_id=pw.this.id,
        result=openai_chat_completion(pw.this.prompt),
    )

    return response
