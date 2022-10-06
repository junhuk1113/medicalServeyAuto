from selenium import webdriver
import os

path = os.path.join(os.path.dirname(__file__), '/home/opc/chromedriver')

# selenium으로 무엇인가 입력하기 위한 import
from selenium.webdriver.common.keys import Keys

# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time

# 크롬드라이버 실행  (경로 예: '/Users/Roy/Downloads/chromedriver')
driver = webdriver.Chrome(path) 

#크롬 드라이버에 url 주소 넣고 실행
driver.get('https://form.office.naver.com/form/responseView.cmd?formkey=YzVhMWI5OTYtMmNhMC00YmI3LWFmMmYtNzQ3MjJlMzcyNjc2&sourceId=urlshare')

# 페이지가 완전히 로딩되도록 3초동안 기다림
#time.sleep(1)
search_box = driver.find_element_by_xpath('//*[@id="answer"]')
search_box.send_keys('325')
search_box = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/div[1]/div[2]/div/div/div[2]/form/div/div[2]/div/div[3]/div/input')
search_box.send_keys('권준혁') 
search_box = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/div[1]/div[2]/div/div/div[2]/form/div/div[3]/div/div[3]/div/input")
search_box.send_keys('36.4') 
search_box.send_keys(Keys.PAGE_DOWN) 
search_box = driver.find_element_by_xpath('//*[@id="formItem_5"]/div/div[3]/div/div[2]/div')
search_box.send_keys(Keys.ENTER) 
search_box = driver.find_element_by_xpath('//*[@id="pageNav"]/button[3]')
search_box.send_keys(Keys.ENTER) 
time.sleep(2)
driver.quit() 