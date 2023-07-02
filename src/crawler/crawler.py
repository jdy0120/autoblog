from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import time

def search_list(driver):
  try:
    element = WebDriverWait(driver,10).until(
      EC.presence_of_element_located((By.XPATH, f"/html/body/div[3]/div/div[3]/div[1]/ul/li[3]/div[1]/a[1]/div/div/span[1]"))
    )
    
    element.click()
  except:
    return
    
  finally:
    pass

def search_detail(driver):
  
  try:
  #주소
    element = driver.find_element(By.XPATH,f'//*[@id="app-root"]/div/div/div/div[6]/div/div[2]/div/div/div[1]/div/a/span[1]')
    print(element.text)
  except:
    print('주소가 없습니다.')
  
  try:
    #주차장
    element = driver.find_element(By.XPATH,f'//*[@id="app-root"]/div/div/div/div[6]/div/div[2]/div/div/div[2]/div/div/a/span[1]')
    element.click()
    print(element.text)
  except:
    print('주차장 정보가 없습니다.')
  
  try:
    #시간
    element = driver.find_element(By.XPATH,f'//*[@id="app-root"]/div/div/div/div[6]/div/div[2]/div/div/div[3]/div/a')
    element.click()
    print(element.text)
  except:
    print('시간 정보가 없습니다.')
  
  try:
    #전화
    element = driver.find_element(By.XPATH,f'//*[@id="app-root"]/div/div/div/div[6]/div/div[2]/div/div/div[4]/div/span[1]')
    element.click()
    print(element.text)
  except:
    print('전화 정보가 없습니다.')
  
  try:
    #가게
    element = driver.find_element(By.XPATH,f'//*[@id="app-root"]/div/div/div/div[6]/div/div[2]/div/div/div[6]/div')
    element.click()
    print(element.text)
  except:
    print('가게 정보가 없습니다.')
  
  try:
    #홈페이지
    element = driver.find_elements(By.XPATH,f'')
  except:
    print('홈페이지 정보가 없습니다.')
  
  try:
    #detail
    element = driver.find_element(By.XPATH,f'//*[@id="app-root"]/div/div/div/div[6]/div/div[2]/div/div/div[8]/div/a/span[1]')
    element.click()
    print(element.text)
  except:
    print('detail 정보가 없습니다.')
    

def search_naver(query):
    # 크롬 웹드라이버의 경로를 입력하세요
    
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    
    driver = webdriver.Chrome()

    print(query)

    # naver.com에 접근
    driver.get("https://map.naver.com/v5/search/" + query + '맛집')
    
    
    # searchIframe으로 이동
    driver.switch_to.frame("searchIframe")
    
    # 음식점 리스트 클릭
    search_list(driver)

    time.sleep(3)
    
    # 부모 프레임으로 이동 후 음식점 상세 프레임으로 이동
    driver.switch_to.parent_frame()
    
    driver.switch_to.frame('entryIframe')
    
    search_detail(driver)
    
    try:
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      
      time.sleep(3)
      
      element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,f"//a[contains(text(), '블로그리뷰 더보기')]")))
      element.click()
    except:
      print('블로그 리뷰 더보기 버튼이 없습니다.')

    try:
      element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,f'//*[@id="app-root"]/div/div/div/div[7]/div[3]/div/div[1]/ul')))
      list_items = element.find_elements(By.TAG_NAME, "li")
    
      for index,item in enumerate(list_items):
        try:
          driver.switch_to.frame('entryIframe')
        except:
          print('entryIframe이 없습니다.')
        item.click()
      
        driver.switch_to.window(driver.window_handles[index+1])
        
        driver.switch_to.frame('mainFrame')
        
        blog_post = driver.find_elements(By.CSS_SELECTOR,f"div[id*='post-view']")
        
        for post in blog_post:
          print(post.text)
      
        # print(blog_post.text)
        
        driver.switch_to.window(driver.window_handles[0])
      
    except:
      print('블로그 리뷰가 없습니다.')
    

    driver.close()