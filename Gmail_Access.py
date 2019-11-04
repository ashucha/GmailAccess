import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time

username = input('Enter your username: ')
password = input('Enter your password: ')

driver = webdriver.Chrome(executable_path='C:/chromedriver_win32')
driver.get('https://mail.google.com/mail/u/0/#inbox')

driver.find_element_by_name('identifier').send_keys(username)
driver.switch_to.active_element.send_keys(Keys.ENTER)

time.sleep(1)

driver.switch_to.active_element.send_keys(password)
driver.switch_to.active_element.send_keys(Keys.ENTER)

time.sleep(4)

driver.find_element_by_class_name('gb_Ia').click()
driver.find_element_by_class_name('gb_9f').click()

time.sleep(1)

driver.find_element_by_class_name('Z4o1ee').click()

time.sleep(3)

driver.switch_to.active_element.send_keys(Keys.TAB * 12 + Keys.ENTER)

time.sleep(1)

#driver.switch_to.active_element.send_keys(Keys.TAB * 2 + Keys.ENTER)

time.sleep(1)

#driver.switch_to.active_element.send_keys(Keys.ENTER)

time.sleep(1)

#driver.switch_to.active_element.send_keys(Keys.ENTER)

time.sleep(1)
'''driver.find_element_by_xpath('//*[@id=\'ow287\']/div[1]/ul/li[3]/div').click()
driver.find_element_by_xpath('//*[@id=\'ow287\']/div[1]/ul/li[1]/div').click()
driver.find_element_by_xpath('//*[@id=\'yDmH0d\']/div[4]/div/div[2]/div[3]/div[1]/div[2]').click()'''
