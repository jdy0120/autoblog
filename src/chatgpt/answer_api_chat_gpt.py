import os
import openai
from dotenv import load_dotenv
from src.chatgpt.slice_token import cut_tokens

load_dotenv(verbose=True)

# openai.api_base = os.getenv("OPENAI_API_BASE")
openai.api_key = os.getenv("CHAT_GPT_API")

def answer_api_chat_gpt(shopinfo,text):
  
  question = cut_tokens(text)
  print(question)
  
  try:
    response = openai.ChatCompletion.create(
      model='gpt-3.5-turbo', # The deployment name you chose when you deployed the ChatGPT or GPT-4 model.
      messages=[{"role": "user", "content": f"다음은 {shopinfo}의 리뷰를 모은 글이야 읽기 쉽게 정리해서 출력해줘 \n {question}"}]
    )
  except:
    print('너무 긴 글이 들어왔습니다.')
    return ''
  
  answer = response.choices[0].message.content
  return answer