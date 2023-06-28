import os
import openai

openai.api_key = os.getenv("CHAT_GPT_API")

def answer_api_chat_gpt(text):
  print('apiKey')