import os
import openai
from dotenv import load_dotenv

load_dotenv(verbose=True)

openai.api_key = os.getenv("CHAT_GPT_API")

def answer_api_chat_gpt(text):
  response = openai.Completion.create(
    model='gpt-3.5-turbo',
    prompt='chat gpt 사용 방법에 대해 알려줘'
  )
  
  print(response)