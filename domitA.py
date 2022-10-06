from selenium import webdriver
import os
path = os.path.join(os.path.dirname(__file__), '/home/opc/chromedriver')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--single-process")
chrome_options.add_argument("--disable-dev-shm-usage")
# selenium으로 무엇인가 입력하기 위한 import
from selenium.webdriver.common.keys import Keys
import time
import schedule
testurl = "https://naver.me/xBhETdUD"
url = "https://naver.me/xNoaOYLe"

class autoSurvey():
    def __init__(self):
        self.user_data = {}
        while True:
            try:
                file = open('userData.dat','r',encoding='UTF-8')
            except FileNotFoundError:#userData.dat 파일이 없으면 새로 생성
                file = open('userData.dat','w',encoding='UTF-8')
                file.close()
            else:
                flist=file.readlines()
                for i in flist:
                    tlist = i.split()
                    self.user_data[tlist[0]] = tlist[1:]
                break
                
    def runAuto(self,name, address, temperature):
        driver = webdriver.Chrome(path,chrome_options=chrome_options) # 크롬드라이버 실행
        #크롬 드라이버에 url 주소 넣고 실행
        driver.get(testurl)
        time.sleep(1) #웹페이지 로딩 대기
        search_box = driver.find_element_by_xpath('//*[@id="answer"]')
        search_box.send_keys(address)
        search_box = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/div[1]/div[2]/div/div/div[2]/form/div/div[2]/div/div[3]/div/input')
        search_box.send_keys(name) 
        search_box = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/div[1]/div[2]/div/div/div[2]/form/div/div[3]/div/div[3]/div/input")
        search_box.send_keys(temperature) 
        search_box.send_keys(Keys.PAGE_DOWN) 
        search_box = driver.find_element_by_xpath('//*[@id="formItem_5"]/div/div[3]/div/div[2]/div')
        search_box.send_keys(Keys.ENTER) 
        search_box = driver.find_element_by_xpath('//*[@id="pageNav"]/button[3]')
        search_box.send_keys(Keys.ENTER) 
        time.sleep(2)
        driver.quit()
    def createNewuser(self, name, address, temperature):
        self.user_data[name] = [address, temperature]
    def surveyAll(self):
        print("ttt")
        for key in self.user_data.keys():
            print(key)
            self.runAuto(key,self.user_data[key][0],self.user_data[key][1])

Gugwon = autoSurvey()
#Gugwon.surveyAll()
schedule.every(5).seconds.do(Gugwon.surveyAll) 
while True:
    schedule.run_pending()
    time.sleep(1)