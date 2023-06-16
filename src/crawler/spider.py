from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def search_naver(query):
    # 크롬 웹드라이버의 경로를 입력하세요
    driver_path = './chromedriver' 
    driver = webdriver.Chrome(executable_path=driver_path)

    # naver.com에 접근
    driver.get("http://www.naver.com")

    # 검색창을 찾아 검색어 입력
    search_box = driver.find_element_by_name("query")
    search_box.send_keys(query)

    # 검색 실행
    search_box.send_keys(Keys.RETURN)

    # 검색 결과가 로드될 때까지 기다림
    time.sleep(2)

    # 웹드라이버 종료
    driver.quit()

# 함수 테스트
search_naver("OpenAI")