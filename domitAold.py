from selenium import webdriver
import os
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--single-process")
chrome_options.add_argument("--disable-dev-shm-usage")
path = os.path.join(os.path.dirname(__file__), '/home/junhuk1113/chromedriver')

# selenium으로 무엇인가 입력하기 위한 import
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time

# 크롬드라이버 실행  (경로 예: '/Users/Roy/Downloads/chromedriver')
driver = webdriver.Chrome(path,chrome_options=chrome_options) 

#크롬 드라이버에 url 주소 넣고 실행
driver.get('https://naver.me/xBhETdUD')

# 페이지가 완전히 로딩되도록 3초동안 기다림
#time.sleep(1)
search_box = driver.find_element(By.XPATH,'//*[@id="answer"]')
search_box.send_keys('237')
search_box = driver.find_element(By.XPATH,'/html/body/div[5]/div[1]/div[1]/div[1]/div[2]/div/div/div[2]/form/div/div[2]/div/div[3]/div/input')
search_box.send_keys('권준혁') 
search_box = driver.find_element(By.XPATH,"/html/body/div[5]/div[1]/div[1]/div[1]/div[2]/div/div/div[2]/form/div/div[3]/div/div[3]/div/input")
search_box.send_keys('36.4') 
search_box.send_keys(Keys.PAGE_DOWN) 
search_box = driver.find_element(By.XPATH,'//*[@id="formItem_5"]/div/div[3]/div/div[2]/div')
search_box.send_keys(Keys.ENTER) 
search_box = driver.find_element(By.XPATH,'//*[@id="pageNav"]/button[3]')
search_box.send_keys(Keys.ENTER) 

driver.quit() 