from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.remote import mobile
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

import time

chromedriver_path = '/usr/bin/chromedriver'
brave_path = '/usr/bin/brave-browser'
option = webdriver.ChromeOptions()
option.binary_location = brave_path
browser = webdriver.Chrome(executable_path=chromedriver_path,options=option)
browser.get("file:///home/tarunchakitha/snapchat_auto/3.html")

dropdown = browser.find_element_by_xpath('//*[@id="field-24643406"]')
sleep(4)
dropdown.send_keys('N')
sleep(4)
browser.close()



