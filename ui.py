import streamlit as st

# Streamlit UI elements
st.title("YouTube Chatbot")

# Input field for YouTube video link
youtube_link = st.text_input("Paste the YouTube video link here:")

# Button to submit the link and trigger chatbot processing
if st.button("Submit"):
    if youtube_link:
        # Process the YouTube video link here (e.g., fetch video data, extract information)
        st.write("You submitted the following YouTube video link:", youtube_link)
    else:
        st.warning("Please enter a valid YouTube video link.")
