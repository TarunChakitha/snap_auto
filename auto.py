from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.remote import mobile
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import pickle

chromedriver_path = '/usr/bin/chromedriver'
brave_path = '/usr/bin/brave-browser'
option = webdriver.ChromeOptions()
option.add_argument("user-data-dir=selenium") 
option.binary_location = brave_path
browser = webdriver.Chrome(executable_path=chromedriver_path,options=option)
browser.get('https://support.snapchat.com/en-US/i-need-help?start=5695496404336640')

cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    browser.add_cookie(cookie)

fusername = 'nnn'

# wait = WebDriverWait(browser, 10)
WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '#field-24281229')))

search_form = browser.find_element(By.TAG_NAME, "form")

username = search_form.find_element_by_xpath('//*[@id="field-24281229"]')
username.send_keys("nmm")

email = search_form.find_element_by_xpath('//*[@id="field-24335325"]')
email.send_keys("dummy@gmail.com")

mobile_num = search_form.find_element_by_xpath('//*[@id="field-24369716"]')
mobile_num.send_keys("8888888888")

device = search_form.find_element_by_xpath('//*[@id="field-24369726"]')
device.send_keys("Vivo Z1 Pro")

friend_username = search_form.find_element_by_xpath('//*[@id="field-24369736"]')
friend_username.send_keys(fusername)

today = search_form.find_element_by_xpath('//*[@id="field-24326423"]')
today.send_keys('Today')

streak = search_form.find_element_by_xpath('//*[@id="field-24641746"]')
streak.send_keys('200')
streak.send_keys(Keys.TAB,'N',Keys.TAB,"My Streak Disappeared.")

# pickle.dump(browser.get_cookies() , open("cookies.pkl","wb"))
submit = search_form.find_element_by_xpath('//*[@id="submit-button"]')
submit.click()

sleep(5)

browser.close()
