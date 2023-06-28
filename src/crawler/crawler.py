from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def search_naver(query):
    # 크롬 웹드라이버의 경로를 입력하세요
    
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    
    driver = webdriver.Chrome()

    # naver.com에 접근
    driver.get("https://map.naver.com/v5/search/" + query + '맛집')
    
    # searchIframe으로 이동
    driver.switch_to.frame("searchIframe")
    
    try:
      element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH, f"/html/body/div[3]/div/div[3]/div[1]/ul/li[3]/div[1]/a[1]/div/div/span[1]"))
      )
      
      element.click()
      
    finally:
      pass

    time.sleep(3)
    
    # 부모 프레임으로 이동 후 음식점 상세 프레임으로 이동
    driver.switch_to.parent_frame()
    
    driver.switch_to.frame('entryIframe')
    
    #주소
    driver.find_element(By.XPATH,f'')
    
    #주차장
    driver.find_element(By.XPATH,f'')
    
    #시간
    driver.find_element(By.XPATH,f'')
    
    #전화
    driver.find_element(By.XPATH,f'')
    
    #가게
    driver.find_element(By.XPATH,f'')
    
    #홈페이지
    driver.find_element(By.XPATH,f'')
    
    #detail
    driver.find_element(By.XPATH,f'')
    
    
    try:
      element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH, f"/html/body/div[3]/div/div/div/div[2]/div[2]/a[1]"))
      )
      
      element.click()
      
    finally:
      pass

    
    
    while(True):
      pass
