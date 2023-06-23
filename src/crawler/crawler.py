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

    driver.switch_to.frame("searchIframe")
    
    try:
      element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH, f"/html/body/div[3]/div/div[3]/div[1]/ul/li[3]/div[1]/a[1]/div/div/span[1]"))
      )
      
      element.click()
      
    finally:
      pass

    
    
    while(True):
      pass
