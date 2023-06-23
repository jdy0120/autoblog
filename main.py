from src.crawler.crawler import search_naver
import csv

if __name__ == "__main__":
    print('start')
    
    dong_name_list = open('./data/korean_dong_name.csv','r')
    reader = csv.reader(dong_name_list)
    
    for index,line in enumerate(reader):
        if line[3] == '' or index == 0:
            continue
        
        search_word = line[1] + line[2] + line[3]
        
        search_naver(search_word)
        