import os
import openai
from dotenv import load_dotenv

load_dotenv(verbose=True)

# openai.api_base = os.getenv("OPENAI_API_BASE")
openai.api_key = os.getenv("CHAT_GPT_API")

def answer_api_chat_gpt(text):
  response = openai.Completion.create(
    model="text-davinci-003", # The deployment name you chose when you deployed the ChatGPT or GPT-4 model.
    prompt=f"Answer the question based on the context below, and if the question can't be answered based on the context, say \"I don't know\"\n\nContext: doyeon\n\n---\n\nQuestion: can you answer korean?\nAnswer:"
  )
  
  answer =response["choices"][0]["text"].strip()
  print(answer)