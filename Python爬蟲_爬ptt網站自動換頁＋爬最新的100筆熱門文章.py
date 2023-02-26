import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

num=0
r = requests.get('https://www.ptt.cc/bbs/Gossiping/index.html',cookies={'over18':'1'})
soup = BeautifulSoup(r.text,'lxml')
tags = soup.find_all('div',class_='r-ent')
num += len(tags)

for tag in tags:
    if tag.find('a'):
        print(tag.find('a').text)
        print(tag.find('a')['href'])
        print(tag.find('div',class_='author').text)

print('='*20)
    
driver = webdriver.Chrome()
driver.get('https://www.ptt.cc/bbs/Gossiping/index.html')
driver.find_element(By.NAME,'yes').click()
page=2
while num <=100:
    driver.find_element(By.LINK_TEXT,'‹ 上頁').click()
    
    print('=======page {0}======'.format(page))
    soup = BeautifulSoup(driver.page_source,'lxml')
    tags = soup.find_all('div',class_='r-ent')
    
    if page <=4:
        for tag in tags:
            if tag.find('a'):
                print(tag.find('a').text)
                print(tag.find('a')['href'])
                print(tag.find('div',class_='author').text)
    else:
        rest = 100-num
        for i in range(len(tags)-1,len(tags)-1-rest,-1):
            if tags[i].find('a'):
                print('前100筆')
                print(tags[i].find('a').text)
                print(tags[i].find('a')['href'])
                print(tags[i].find('div',class_='author').text)
                
            
    num += len(tags)
    print('目前總比數：',num)
    page += 1
#%% 第二題
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


r = requests.get('https://www.ptt.cc/bbs/Gossiping/index1.html',cookies={'over18':'1'})
soup = BeautifulSoup(r.text,'lxml')
tags = soup.find_all('div',class_='r-ent')
page=1
print('第{0}頁:'.format(page))
num=0
for tag in tags:
    t = tag.find('span',class_='hl f1')
    if t and t.text == '爆':
        num +=1
        print('第{0}筆{1}'.format(num,t.text))
        print(tag.find('a').text)
        print(tag.find('a')['href'])
        print(tag.find('div',class_='author').text)

    
driver = webdriver.Chrome()
driver.get('https://www.ptt.cc/bbs/Gossiping/index1.html')
driver.find_element(By.NAME,'yes').click()

while num < 50:
    driver.find_element(By.LINK_TEXT,'下頁 ›').click()
    page +=1
    print('第{0}頁:'.format(page))
    soup = BeautifulSoup(driver.page_source,'lxml')
    tags = soup.find_all('div',class_='r-ent')
    
    for tag in tags:
       t = tag.find('span',class_='hl f1')
       if t and t.text == '爆':
            num +=1
            
            print('第{0}筆{1}'.format(num,t.text))
            print(t.text)
            print(tag.find('a').text)
            print(tag.find('a')['href'])
            print(tag.find('div',class_='author').text)
            if num == 50:
                break
            
    

            
            
   
  
   