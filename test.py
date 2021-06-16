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
browser.get('https://support.snapchat.com/en-US/i-need-help?start=5695496404336640')

fusername = 'srujanaalli'

# wait = WebDriverWait(browser, 10)
WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '#field-24281229')))

username = browser.find_element_by_xpath('//*[@id="field-24281229"]')
username.send_keys("tarun_chakitha")

email = browser.find_element_by_xpath('//*[@id="field-24335325"]')
email.send_keys("upparitarun729@gmail.com")

mobile_num = browser.find_element_by_xpath('//*[@id="field-24369716"]')
mobile_num.send_keys("9063172882")

device = browser.find_element_by_xpath('//*[@id="field-24369726"]')
device.send_keys("Vivo Z1 Pro")

friend_username = browser.find_element_by_xpath('//*[@id="field-24369736"]')
friend_username.send_keys(fusername)

today = browser.find_element_by_xpath('//*[@id="field-24326423"]')
today.send_keys('Today')

streak = browser.find_element_by_xpath('//*[@id="field-24641746"]')
streak.send_keys('200')

# dropdown = browser.find_element_by_xpath('//*[@id="field-24643406"]')
# WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//label[contains(@class, 'housing_type')]")))
################
# dropdown_trigger = browser.find_element_by_xpath('//*[@id="field-24643406"]')
# browser.execute_script("arguments[0].click();", dropdown_trigger)
################
# actions = ActionChains(browser)
# for _ in range(8):
#     actions.send_keys(Keys.ARROW_DOWN).perform()
#     time.sleep(1)
# nav = browser.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/form/div[8]/div[2]/div')
option = browser.find_element_by_xpath('//*[@id="field-24643406"]')
option.send_keys(Keys.RETURN)

# nav = browser.find_element_by_xpath('//*[@id="field-24643406"]')
# nav = nav.send_keys(Keys.ARROW_DOWN)
# nav = nav.send_keys(Keys.ENTER)
# dropdown_option = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="field-24643406"]/option[3]')))
# option = Select(browser.find_element_by_xpath('//*[@id="field-24643406"]/option[3]'))
# option = browser.find_element_by_xpath('//*[@id="field-24643406"]/option[3]')
# browser.execute_script("arguments[2].click();", option)
# option.send_keys(Keys.ARROW_DOWN)
# option.send_keys(Keys.ARROW_DOWN)

# dropdown_option.click()
# select = (browser.find_element_by_xpath('//*[@id="field-24643406"]/option[3]')).click()
# select = Select(dropdown)
# select.select_by_value('hourglass-no')

# select.select_by_visible_text('No')
# print(select.options)
# for o in select.options:
#     o.select_by_visible_text('No')
# //*[@id="field-24643406"]
sleep(5)
# //*[@id="field-24643406"]/option[3]
browser.close()

# //*[@id="field-24643406"]