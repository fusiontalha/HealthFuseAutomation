from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import wait
from selenium.webdriver.support.ui import Select
chrome_driver = webdriver.Chrome('./chromedriver')
chrome_driver.maximize_window()
chrome_driver.get('https://hf-op-dev-webapp.azurewebsites.net/')
chrome_driver.find_element_by_id('usernameval').send_keys('anaam.nizami@xorbix.com')
chrome_driver.find_element_by_id('passwordval').send_keys('123456')
#chrome_driver.find_element_by_id('formCheck-2').click()
time.sleep(4)
chrome_driver.find_element_by_id('loginbuttonid').submit()
chrome_driver.implicitly_wait(10)
chrome_driver.find_element_by_xpath('//*[@id="navcol-1"]/ul/li[5]/a').click()
chrome_driver.find_element_by_xpath('//*[@id="navcol-1"]/ul/li[5]/div/a[3]').click()
chrome_driver.find_element_by_xpath('//*[@id="creatUserButton"]/i').click()
time.sleep(4)
chrome_driver.find_element_by_id('FirstName').send_keys('David')
chrome_driver.find_element_by_id('LastName').send_keys('Jhonson')
chrome_driver.find_element_by_id('EmailAddress').send_keys('yegeh21327@brosj.net')
chrome_driver.find_element_by_id('PhoneNumber').send_keys('123321123')
btn = chrome_driver.find_element_by_xpath('//*[@id="RolesDropdown"]')
btn = Select(btn)
btn.select_by_visible_text('Administrators')
chrome_driver.find_element_by_id('createUserSave').click()

#FirstName
#LastName
#EmailAddress
#PhoneNumber



