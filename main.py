from src.crawler.crawler import search_naver
from src.chatgpt import answer_api_chat_gpt

import json

if __name__ == "__main__":
    print('start')
    dong_name_list = []
    with open('./data/korean_dong_name.json', 'r', encoding='utf-8') as f:
        dong_name_list = json.load(f)
        
    answer_api_chat_gpt('s')

    # for index,item in enumerate(dong_name_list):
        
    #     search_naver(item['address'])
        
        