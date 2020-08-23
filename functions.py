import time
from selenium import webdriver
import Locators as locator
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome('./chromedriver')


def login():
    try:
        driver.find_element_by_xpath(locator.login_email).send_keys('anaam.nizami@xorbix.com')
        time.sleep(5)
        driver.find_element_by_xpath(locator.login_password).send_keys('112233')
        time.sleep(5)
        driver.find_element_by_xpath(locator.login_btn).click()
        time.sleep(10)
        try:
            driver.find_element_by_xpath(locator.login_btn).click()
            return True
        except:
            print('already clicked')
    except:
        return False


def start():
    driver.get(locator.url_home)
    driver.maximize_window()
    time.sleep(10)
def CreateVendor:
    driver.find_element_by_xpath(locator.Settings).click()
    driver.find_element_by_xpath(locator.VendManage).click()
    time.sleep(4)
    driver.find_element_by_xpath(locator.CreateVendor).click()
    time.sleep(4)
    driver.find_element_by_id(locator.VendName).send_keys('john')
    driver.find_element_by_id(locator.VendAddress).send_keys('street 21 ')
    driver.find_element_by_id(locator.VendCity).send_keys('Newyork')
    driver.find_element_by_id(locator.VendState).send_keys('NY')
    driver.find_element_by_id(locator.VendZip).send_keys('111')
    driver.find_element_by_id(locator.VendorActive).click()
    driver.find_element_by_xpath(locator.VendOption).click()
    time.sleep(4)
    driver.find_element_by_class_name(locator.VendSelect).click()
    time.sleep(4)
    # driver.find_element_by_class_name('dx-item-content dx-list-item-content').send_keys()
    # driver.find_element_by_id('updateVendor').submit()
def DelVendor():
    driver.find_element_by_xpath(locator.Settings).click()
    driver.find_element_by_xpath(locator.VendManage).click()
    time.sleep(4)
    driver.find_element_by_xpath(locator.VendNameSearch).send_keys('abccc')
    time.sleep(4)
    driver.find_element_by_xpath(locator.VendDeleteIcon).click()
    time.sleep(4)
    #driver.find_element_by_xpath(locator.VendDelete_OK).click()