import time
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import bs4             
import urllib.request  
from selenium.webdriver.support.ui import Select
url = "https://pw.ktrmr.com/mrIWeb/mrIWeb.srf?i.project=WKMCD21&s=GEN24&id=1&chk=na&rs=1&WaveV=27&i.test=1&aar=1&pid=auto&korsid=9833DE4B0B568848B3D288688D475E98"

html = urllib.request.urlopen(url)
parse_html = bs4.BeautifulSoup(html, "html.parser")

driver = webdriver.Chrome(executable_path='C:/Users/park/Desktop/auto_survey/venv/chromedriver.exe')
driver.get(url=url)

#동의
html = driver.page_source
soup = bs4.BeautifulSoup(html, 'html.parser')
contents = soup.find("span",{"class":"mrQuestionTable"})
#print(contents.text)

test = driver.find_element_by_xpath('//*[@id="container_QAgreement"]/div/div[1]/div[1]/div/div').click()

time.sleep(3)
elem = driver.find_element("_NNext")
elem.submit()

#성별
html = driver.page_source
soup = bs4.BeautifulSoup(html, 'html.parser')
contents = soup.find("span",{"class":"mrQuestionTable"})
#print(contents.text)
driver.find_element_by_xpath('//*[@id="container_QS4"]/div/div[1]/div[1]/div/div/div/div[2]').click() #남
#driver.find_element_by_xpath('//*[@id="container_QS4"]/div/div[1]/div[2]/div/div/div/div[2]').click() #여
elem = driver.find_element_by_name("_NNext")
elem.submit()
time.sleep(3)

#나이입력
elem = driver.find_element_by_id("_Q0") 
elem.send_keys(33)
elem = driver.find_element_by_name("_NNext")
elem.submit()
time.sleep(3)

#직업
html = driver.page_source
soup = bs4.BeautifulSoup(html, 'html.parser')

contents = soup.findAll("span",{"class":"mrSingleText"})
print(contents.text)


#container_QAgreement > div > div.__flexgrid_row > div:nth-child(1)