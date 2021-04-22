import time
# import json
#from lxml import html
from webdriver_manager.chrome import ChromeDriverManager
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

options = webdriver.ChromeOptions()

options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--no-sandbox')
options.add_argument("user-data-dir=C:\\Users\\arifu\\AppData\\Local\\Google\\Chrome\\User Data\\Default")  # Path to your chrome profile

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get("https://xe.com/")
# 2 | setWindowSize | 1382x754 |
driver.set_window_size(1382, 754)
# 3 | runScript | window.scrollTo(0,105) |
driver.execute_script("window.scrollTo(0,105)")
# 4 | click | id=dashboard-top-row |
driver.find_element(By.ID, "dashboard-top-row").click()
# 5 | runScript | window.scrollTo(0,600) |
driver.execute_script("window.scrollTo(0,600)")
# 6 | runScript | window.scrollTo(0,600) |
driver.execute_script("window.scrollTo(0,600)")
# 7 | mouseDown | css=#dashboard-top-row-option-14 .description |
element = driver.find_element(By.CSS_SELECTOR, "#dashboard-top-row-option-14 .description")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
# 8 | mouseUp | css=.ripple |
element = driver.find_element(By.CSS_SELECTOR, ".ripple")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
# 9 | click | id=dashboard-top-row-option-14 |
driver.find_element(By.ID, "dashboard-top-row-option-14").click()
# 10 | click | id=pugsnax |
driver.find_element(By.ID, "pugsnax").click()
# 11 | mouseDown | css=#pugsnax-option-2 .description |
element = driver.find_element(By.CSS_SELECTOR, "#pugsnax-option-2 .description")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
# 12 | mouseUp | css=.ripple |
element = driver.find_element(By.CSS_SELECTOR, ".ripple")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
# 13 | click | id=pugsnax-option-2 |
driver.find_element(By.ID, "pugsnax-option-2").click()
# 14 | click | id=pugsnax |
driver.find_element(By.ID, "pugsnax").click()
# 15 | mouseDown | css=#pugsnax-option-1 .description |
element = driver.find_element(By.CSS_SELECTOR, "#pugsnax-option-1 .description")
actions = ActionChains(driver)
actions.move_to_element(element).click_and_hold().perform()
# 16 | mouseUp | css=.ripple |
element = driver.find_element(By.CSS_SELECTOR, ".ripple")
actions = ActionChains(driver)
actions.move_to_element(element).release().perform()
# 17 | click | id=pugsnax-option-1 |
driver.find_element(By.ID, "pugsnax-option-1").click()
# 18 | click | css=.currency-dashboard__RowWrapper-sc-1lclbd-10:nth-child(3)
# .currency-dashboard__Cell-sc-1lclbd-7:nth-child(2) .overflow-tooltip___StyledDiv-sc-1bt8rl7-0 |
rate = driver.find_element(By.CSS_SELECTOR, "overflow-tooltip___StyledDiv2-sc-1bt8rl7-1 dcfPZC").text()
print(rate)

