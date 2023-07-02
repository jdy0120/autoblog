from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import time

def infinity_scroll(driver):
  SCROLL_PAUSE_TIME = 2

  scroll_element = driver.find_element(By.XPATH,f'//*[@id="_pcmap_list_scroll_container"]')
  # Get scroll height initially
  last_height = driver.execute_script("return arguments[0].scrollHeight", scroll_element)

  while True:
    # Scroll down to bottom within the element
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_element)

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return arguments[0].scrollHeight", scroll_element)
    if new_height == last_height:
        # If heights are the same, the bottom is reached and exit the loop
        break
    last_height = new_height

def list_element(driver):
  try:
    element = driver.find_element(By.XPATH,f'//*[@id="_pcmap_list_scroll_container"]/ul')
    return element
  except:
    return False

def search_list(shop):
  try:
    element = WebDriverWait(shop,10).until(
      EC.presence_of_element_located((By.XPATH, f"./div[1]/a[1]/div/div/span[1]"))
    )
    
    element.click()
  except:
    return
    
  finally:
    pass

def search_detail(driver):
  shop_info = dict()
  
  element = driver.find_element(By.CLASS_NAME,f'PIbes')
  all_infos = element.find_elements(By.XPATH, './div')
  
  for e in all_infos:
    try:
      # aria-expanded="false" 속성을 가진 a 태그를 찾습니다.
      a_tag = e.find_element(By.XPATH,f".//a[@aria-expanded='false']")
      
      # 찾은 a 태그를 클릭합니다.
      a_tag.click()
      
    except:
        # a 태그가 없으면 무시하고 진행합니다.
        pass


    time.sleep(0.1)
    print('\n'.split(e.text)[0])
    
    try:
      info_key = e.find_element(By.XPATH,'./strong')
      print(info_key.text)
      
      info_value = e.find_element(By.XPATH,'./div')
      print(info_value.text)
      
      if (info_key.text != '정보 수정 제안'):
        shop_info[info_key.text] = info_value.text

    except:
      pass
    
    try:
      a_tag = e.find_element(By.XPATH,f".//a[@aria-expanded='true']")
      
      a_tag.click()
      
    except:
        pass

  print(shop_info)
  
def search_naver(query):
    # 크롬 웹드라이버의 경로를 입력하세요
    
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    
    driver = webdriver.Chrome()

    # naver.com에 접근
    driver.get("https://map.naver.com/v5/search/" + query + '맛집')
    
    
    
    # searchIframe으로 이동
    driver.switch_to.frame("searchIframe")
    
    time.sleep(3)
    
    # infinity_scroll(driver)
    
    # time.sleep(2)
    
    element = list_element(driver)
    if (element == False):
      driver.close()
      return
    
    shop_list = element.find_elements(By.XPATH, "./li")
    
    page_list_count = 1
    
    while True:
      for shop in shop_list:
        # 음식점 리스트 클릭
        search_list(shop)

        time.sleep(3)
        
        # 부모 프레임으로 이동 후 음식점 상세 프레임으로 이동
        driver.switch_to.parent_frame()
        
        driver.switch_to.frame('entryIframe')
        
        search_detail(driver)
        
        try:
          driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
          
          time.sleep(3)
          
          element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,f"//a[contains(., '더보기') and .//span[contains(., '블로그리뷰')]]")))
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
          
            driver.switch_to.window(driver.window_handles[1])
            
            driver.switch_to.frame('mainFrame')
            
            blog_post = driver.find_elements(By.CSS_SELECTOR,f"div[id*='post-view']")
            
            for post in blog_post:
              print(post.text)
              
            driver.close()
          
            driver.switch_to.window(driver.window_handles[0])
          
        except:
          print('블로그 리뷰가 없습니다.')
        
        time.sleep(3)
        driver.switch_to.parent_frame()
        driver.switch_to.frame("searchIframe")
      
      page_list_count += 1
      
      try:
        element = driver.find_element(By.CLASS_NAME,f'zRM9F')
        page_number_element = element.find_element(By.XPATH, f"//a[text()={page_list_count}]")
        page_number_element.click()
        time.sleep(3)
      except:
        print('더보기 버튼이 없습니다.')
        break

    driver.close()