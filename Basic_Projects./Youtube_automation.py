#REQUIREMENTS--> CHROMEDRIVER,SELENIUM PACKAGE 
#youtube Automation using selenium which searches the given text and performs the actions according to the script
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
chromedriver = 'C:\\Users\\munna\\Downloads\\chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(chromedriver) 
driver.get("https://www.youtube.com/") 
searchbutton = driver.find_element_by_class_name('style-scope ytd-searchbox')
searchbutton.send_keys("CleverProgramming") 
search_icon = driver.find_element_by_id('search-icon-legacy')
search_icon.click()
channel_text = driver.find_element_by_id('text-container')
channel_text.click()
time.sleep(6)
driver.quit()
