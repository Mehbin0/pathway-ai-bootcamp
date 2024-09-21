import tkinter as tk
from tkinter import scrolledtext
import threading
from main import setup_apis, process_video, answer_query

class ChatbotUI:
    def __init__(self, master):
        self.master = master
        master.title("YouTube Video Chatbot")

        self.label_openai = tk.Label(master, text="OpenAI API Key:")
        self.label_openai.pack()
        self.entry_openai = tk.Entry(master, width=50)
        self.entry_openai.pack()

        self.label_youtube = tk.Label(master, text="YouTube API Key:")
        self.label_youtube.pack()
        self.entry_youtube = tk.Entry(master, width=50)
        self.entry_youtube.pack()

        self.label_url = tk.Label(master, text="YouTube Video URL:")
        self.label_url.pack()
        self.entry_url = tk.Entry(master, width=50)
        self.entry_url.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.process_video)
        self.submit_button.pack()

        self.chat_display = scrolledtext.ScrolledText(master, state='disabled', height=20)
        self.chat_display.pack()

        self.query_entry = tk.Entry(master, width=50)
        self.query_entry.pack()

        self.ask_button = tk.Button(master, text="Ask", command=self.ask_question)
        self.ask_button.pack()

        self.youtube = None
        self.index = None

    def process_video(self):
        openai_key = self.entry_openai.get()
        youtube_key = self.entry_youtube.get()
        video_url = self.entry_url.get()

        self.youtube = setup_apis(openai_key, youtube_key)
        video_id = video_url.split("v=")[1]

        def process():
            _, self.index = process_video(self.youtube, video_id)
            self.chat_display.configure(state='normal')
            self.chat_display.insert(tk.END, "Video processed. You can now ask questions.\n")
            self.chat_display.configure(state='disabled')

        threading.Thread(target=process).start()

    def ask_question(self):
        if not self.index:
            self.chat_display.configure(state='normal')
            self.chat_display.insert(tk.END, "Please process a video first.\n")
            self.chat_display.configure(state='disabled')
            return

        query = self.query_entry.get()
        self.query_entry.delete(0, tk.END)

        def get_answer():
            response = answer_query(query, self.index)
            self.chat_display.configure(state='normal')
            self.chat_display.insert(tk.END, f"Q: {query}\n")
            self.chat_display.insert(tk.END, f"A: {response}\n\n")
            self.chat_display.configure(state='disabled')

        threading.Thread(target=get_answer).start()
