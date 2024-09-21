import pathway as pw
from api import process_video, answer_query
from common.config import VIDEO_ID

def chatbot():
    table, index = process_video(VIDEO_ID)

    # Set up input stream for user queries
    queries = pw.io.csv.read("queries.csv")

    # Process queries and generate responses
    responses = queries.select(
        query=pw.this.query,
        response=pw.apply(answer_query, pw.this.query, index=index)
    )

    # Output responses
    pw.io.csv.write(responses, "responses.csv")

if __name__ == "__main__":
    pw.run(chatbot)
