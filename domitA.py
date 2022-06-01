from selenium import webdriver
import os
path = os.path.join(os.path.dirname(__file__), 'chromedriver.exe')

# selenium으로 무엇인가 입력하기 위한 import
from selenium.webdriver.common.keys import Keys
# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time
# 크롬드라이버 실행  (경로 예: '/Users/Roy/Downloads/chromedriver')

class autoSurvey():
    def __init__(self):
        self.driver = webdriver.Chrome(path) 
        self.driver.get('https://form.office.naver.com/form/responseView.cmd?formkey=YzVhMWI5OTYtMmNhMC00YmI3LWFmMmYtNzQ3MjJlMzcyNjc2&sourceId=urlshare')
        time.sleep(1)
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
                
        
        #크롬 드라이버에 url 주소 넣고 실행

    # 페이지가 완전히 로딩되도록 3초동안 기다림
    #time.sleep(1)
    def runAuto(self,name, address, temperature):
        search_box = self.driver.find_element_by_xpath('//*[@id="answer"]')
        search_box.send_keys(address)
        search_box = self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/div[1]/div[2]/div/div/div[2]/form/div/div[2]/div/div[3]/div/input')
        search_box.send_keys(name) 
        search_box = self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/div[1]/div[2]/div/div/div[2]/form/div/div[3]/div/div[3]/div/input")
        search_box.send_keys(temperature) 
        search_box.send_keys(Keys.PAGE_DOWN) 
        search_box = self.driver.find_element_by_xpath('//*[@id="formItem_5"]/div/div[3]/div/div[2]/div')
        search_box.send_keys(Keys.ENTER) 
        search_box = self.driver.find_element_by_xpath('//*[@id="pageNav"]/button[3]')
        search_box.send_keys(Keys.ENTER) 
        time.sleep(2)
        self.driver.quit()
    def createNewuser(self, name, address, temperature):
        self.user_data[name] = [address, temperature]
    def surveyAll(self):
        for key in self.user_data.keys():
            self.runAuto(key,self.user_data[key][0],self.user_data[key][1])

Gugwon = autoSurvey()
Gugwon.surveyAll()