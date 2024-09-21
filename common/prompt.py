SYSTEM_PROMPT = "You are a helpful assistant that answers questions based on the given context."

def generate_user_prompt(context, query):
    return f"Context: {context}\n\nQuestion: {query}"
