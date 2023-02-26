from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('https://www.taiwanlottery.com.tw/Lotto/SuperLotto638/history.aspx')

driver.find_element(By.ID,'SuperLotto638Control_history1_radYM').click()
select_year = Select(driver.find_element(By.ID,'SuperLotto638Control_history1_dropYear'))
select_year.select_by_value('105')
select_month = Select(driver.find_element(By.ID,'SuperLotto638Control_history1_dropMonth'))
select_month.select_by_value('2')
driver.find_element(By.ID,'SuperLotto638Control_history1_btnSubmit').click()

soup = BeautifulSoup(driver.page_source,'lxml')
term10 = soup.find('span',{'id':'SuperLotto638Control_history1_dlQuery_DrawTerm_7'})
print(term10.text)
lottolist =[]
for i in range(1,8):
    lottonum = soup.find('span',{'id':'SuperLotto638Control_history1_dlQuery_SNo'+str(i)+'_7'})
    lottolist.append(lottonum.text)
print(term10.text,lottolist)
