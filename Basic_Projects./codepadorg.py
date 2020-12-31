#Automation of codepad.org with selenium 
#you can change the chromedriverpath depending on your path present in your directory 
#It takes you to site and performs basic operation of printing something in python 
from selenium import  webdriver 
import time
chromePath = "C:\\Users\\munna\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(chromePath) 
driver.get('http://codepad.org')
python_button = driver.find_elements_by_xpath('//*[@id="editor-form"]/table/tbody/tr[2]/td[1]/nobr[10]/label/input')[0]
python_button.click()
text_area = driver.find_element_by_id('textarea')
text_area.send_keys('print("HelloWorld!!")')
submit_button = driver.find_elements_by_xpath('//*[@id="editor-form"]/table/tbody/tr[3]/td/table/tbody/tr/td/div/table/tbody/tr/td[3]/button')[0]
submit_button.click()
time.sleep(5) 
driver.close()
