import time
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import bs4             
import urllib.request  
from selenium.webdriver.support.ui import Select

def judge(soup):
    spanclass = soup.find("span",{"class":"mrQuestionTable"})
    if spanclass:
        if spanclass.find_all('input',{"type":"radio"}):
            print("라디오 버튼")
            return 2 # radio btn
        elif spanclass.find_all('input',{"type":"checkbox"}):
            print("체크 박스")
            return 3 # check box
        else:
            print("판별 불가")
            return -1 #못찾음
    if soup.find_all('input',{"type":"text"}):
            print("텍스트 박스")
            return 1 # text box
    

url = "https://pw.ktrmr.com/mrIWeb/mrIWeb.srf?i.project=WKMCD21&s=GEN24&id=1&chk=na&rs=1&WaveV=27&i.test=1&aar=1&pid=auto&korsid=9833DE4B0B568848B3D288688D475E98"
html = urllib.request.urlopen(url)
parse_html = bs4.BeautifulSoup(html, "html.parser")

driver = webdriver.Chrome(executable_path='C:/Users/park/Desktop/AutoTestSurvey/venv/chromedriver.exe')
driver.get(url=url)

#동의
html = driver.page_source
soup = bs4.BeautifulSoup(html, 'html.parser')
print("동의..........")
judge(soup)
contents = soup.find_all("span",{"class":"mrSingleText"})
cont_cnt = 0
for idx, con in enumerate(contents):
    print(str(idx)+"." + con.text)
    cont_cnt+=1
print("보기 갯수 : " + str(cont_cnt))

test = driver.find_element_by_xpath('//*[@id="container_QAgreement"]/div/div[1]/div[1]/div/div').click() #예
#test = driver.find_element_by_xpath('//*[@id="container_QAgreement"]/div/div[1]/div[2]/div/div').click() #아니오
time.sleep(3)
elem = driver.find_element_by_name("_NNext")
elem.submit()

#성별
html = driver.page_source
soup = bs4.BeautifulSoup(html, 'html.parser')
print("성별..........")
judge(soup)
contents = soup.find_all("span",{"class":"mrSingleText"})
cont_cnt = 0
for idx, con in enumerate(contents):
    print(str(idx)+"." + con.text)
    cont_cnt+=1
print("보기 갯수 : " + str(cont_cnt))

driver.find_element_by_xpath('//*[@id="container_QS4"]/div/div[1]/div[1]/div/div/div/div[2]').click() #남
#driver.find_element_by_xpath('//*[@id="container_QS4"]/div/div[1]/div[2]/div/div/div/div[2]').click() #여
elem = driver.find_element_by_name("_NNext")
elem.submit()
time.sleep(3)



#나이입력
html = driver.page_source
soup = bs4.BeautifulSoup(html, 'html.parser')
print("나이..........")
judge(soup)
contents = soup.find_all("span",{"class":"mrSingleText"})
cont_cnt = 0
for idx, con in enumerate(contents):
    print(str(idx)+"." + con.text)
    cont_cnt+=1
print("보기 갯수 : " + str(cont_cnt))
elem = driver.find_element_by_id("_Q0").send_keys(33)
elem = driver.find_element_by_name("_NNext")
elem.submit()
time.sleep(3)

#직업
html = driver.page_source
soup = bs4.BeautifulSoup(html, 'html.parser')
print("직업..........")
judge(soup)
contents = soup.find_all("span",{"class":"mrSingleText"})
cont_cnt = 0
for idx, con in enumerate(contents):
    print(str(idx)+"." + con.text)
    cont_cnt+=1
print("보기 갯수 : " + str(cont_cnt))
driver.find_element_by_xpath('//*[@id="container_QE"]/div/div[1]/div[1]/div/div/div/div[2]').click() #전문가
elem = driver.find_element_by_name("_NNext")
elem.submit()
time.sleep(3)
#contents = soup.findAll("span",{"class":"mrSingleText"})
#print(contents.text)

#본인이나 가족/친지 중에 다음의 업체에 근무하는 분이 계십니까?
html = driver.page_source
soup = bs4.BeautifulSoup(html, 'html.parser')
print("본인이나 가족/친지 중에 다음 업체..........")
judge(soup)
contents = soup.find_all("span",{"class":"mrSingleText"})
cont_cnt = 0
for idx, con in enumerate(contents):
    print(str(idx)+"." + con.text)
    cont_cnt+=1
print("보기 갯수 : " + str(cont_cnt))
driver.find_element_by_xpath('//*[@id="container_QC1"]/div/div[1]/div[1]/div/div/div/div[2]').click()
elem = driver.find_element_by_name("_NNext")
elem.submit()
time.sleep(3)

#사는 지역
html = driver.page_source
soup = bs4.BeautifulSoup(html, 'html.parser')
print("사는 지역..........")
judge(soup)
contents = soup.find_all("span",{"class":"mrSingleText"})
cont_cnt = 0
for idx, con in enumerate(contents):
    print(str(idx)+"." + con.text)
    cont_cnt+=1
print("보기 갯수 : " + str(cont_cnt))
driver.find_element_by_xpath('//*[@id="container_QS1x1"]/div/div[1]/div[1]/div/div/div/div[2]').click()
elem = driver.find_element_by_name("_NNext")
elem.submit()
time.sleep(3)

#얼마나 살았나
html = driver.page_source
soup = bs4.BeautifulSoup(html, 'html.parser')
print("얼마나 살았나..........")
judge(soup)
contents = soup.find_all("span",{"class":"mrSingleText"})
cont_cnt = 0
for idx, con in enumerate(contents):
    print(str(idx)+"." + con.text)
    cont_cnt+=1
print("보기 갯수 : " + str(cont_cnt))
driver.find_element_by_xpath('//*[@id="container_QS1"]/div/div[1]/div[1]/div/div/div/div[2]').click()
elem = driver.find_element_by_name("_NNext")
elem.submit()
time.sleep(3)


#중간에 무슨 이상한
html = driver.page_source
soup = bs4.BeautifulSoup(html, 'html.parser')
print("중간에 이상한..........")
judge(soup)
contents = soup.find_all("span",{"class":"mrSingleText"})
cont_cnt = 0
for idx, con in enumerate(contents):
    print(str(idx)+"." + con.text)
    cont_cnt+=1
print("보기 갯수 : " + str(cont_cnt))
driver.find_element_by_xpath('//*[@id="Cell.0.7"]/label').click()
elem = driver.find_element_by_name("_NNext")
elem.submit()
time.sleep(3)





#완료
#html = driver.page_source
#soup = bs4.BeautifulSoup(html, 'html.parser')
#driver.find_element_by_xpath('//*[@id="endLinkButton"]').click()
#elem = driver.find_element_by_id("endLinkButton")
#elem.submit()
#time.sleep(3)
