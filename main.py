from src.crawler.crawler import search_naver
from src.chatgpt import answer_api_chat_gpt


import json

if __name__ == "__main__":
    print('start')
    dong_name_list = []
    with open('./data/korean_dong_name.json', 'r', encoding='utf-8') as f:
        dong_name_list = json.load(f)
        
        
    item = dong_name_list[0]
    search_naver(item['address'])
        
    dong_name_list = dong_name_list[1:]

    with open('./data/korean_dong_name.json', 'w', encoding='utf-8') as f:
        json.dump(dong_name_list, f, ensure_ascii=False, indent=4)
        
    print('end')