import os
import openai
from dotenv import load_dotenv

load_dotenv(verbose=True)

# openai.api_base = os.getenv("OPENAI_API_BASE")
openai.api_key = os.getenv("CHAT_GPT_API")

def answer_api_chat_gpt(text):
  
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", # The deployment name you chose when you deployed the ChatGPT or GPT-4 model.
    messages=[{"role": "user", "content": f"다음 내용을 정리해서 출력해줘 \n {text}"}]
  )
  
  answer = response.choices[0].message.content
  print('chat_gpt 답변', answer)