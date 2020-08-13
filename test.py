from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver = webdriver.Chrome('./chromedriver')
chrome_driver.maximize_window()
chrome_driver.get('https://hf-op-dev-webapp.azurewebsites.net/')
chrome_driver.find_element_by_id('usernameval').send_keys('yegeh21327@brosj.net')
chrome_driver.find_element_by_id('passwordval').send_keys('sir123')
#chrome_driver.find_element_by_id('formCheck-2').click()
time.sleep(4)
chrome_driver.find_element_by_id('loginbuttonid').submit()




