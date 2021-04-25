import time
# import json
# from lxml import html
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
from selenium.common.exceptions import NoSuchElementException
import pymongo

options = webdriver.ChromeOptions()

options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--no-sandbox')
# Path to your chrome profile

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get("https://www.jnelectric.com/")
time.sleep(60)
print("Time end")
# user a.henein@caparts.ca
# pass Gil@#$2022

my_client = pymongo.MongoClient("localhost", 27017)
my_db = my_client["jnelectric"]
product_url_col = my_db["product_urls"]

for i in range(370, 600):

    product = product_url_col.find_one({'_id': i})
    page_link = product['link']
    driver.get(page_link)
    time.sleep(4)

    try:
        title = driver.find_element_by_xpath(
            '//*[@id="ProductDetails.Full.View"]/div/div[2]/article/section/div[2]/div/div[1]/h1').text
    except NoSuchElementException:
        title = 'null'

    try:
        address = driver.find_element_by_xpath(
            '//*[@id="main-container"]/div[1]/div').text
        category = address
    except NoSuchElementException:
        address = 'null'
        category = 'null'

    try:
        part_number = driver.find_element_by_xpath(
            '//*[@id="ProductDetails.Full.View"]/div/div[2]/article/section/div[2]/div/div[1]/div[3]/div/span').text
    except NoSuchElementException:
        part_number = 'null'

    try:
        list_price = driver.find_element_by_class_name(
            'product-views-price-lead').text
    except NoSuchElementException:
        list_price = 'null'

    try:
        quantity = driver.find_element_by_class_name(
            'stock-info-message-qty-show-detail').text
    except NoSuchElementException:
        quantity = 'null'

    try:
        description = driver.find_element_by_class_name(
            'product-details-information-section-column-two').text
    except NoSuchElementException:
        description = 'null'

    try:
        references = driver.find_element_by_class_name(
            'product-details-information-references').text
    except NoSuchElementException:
        references = 'null'

    try:
        application = driver.find_element_by_xpath(
            '//*[@id="app_content"]/div/div').text
    except NoSuchElementException:
        application = 'null'

    try:
        pic_1 = driver.find_element_by_xpath(
            '//*[@id="ProductDetails.Full.View"]/div/div[2]/article/section/div[1]/div/div[2]/div/div/div[2]/div[2]/div[1]/a/img').get_attribute(
            'src')
    except NoSuchElementException:
        pic_1 = 'null'

    try:
        pic_2 = driver.find_element_by_xpath(
            '//*[@id="ProductDetails.Full.View"]/div/div[2]/article/section/div[1]/div/div[2]/div/div/div[2]/div[2]/div[2]/a/img').get_attribute(
            'src')
    except NoSuchElementException:
        pic_2 = 'null'

    try:
        pic_3 = driver.find_element_by_xpath(
            '//*[@id="ProductDetails.Full.View"]/div/div[2]/article/section/div[1]/div/div[2]/div/div/div[2]/div[2]/div[3]/a/img').get_attribute(
            'src')
    except NoSuchElementException:
        pic_3 = 'null'

    try:
        pic_4 = driver.find_element_by_xpath(
            '//*[@id="ProductDetails.Full.View"]/div/div[2]/article/section/div[1]/div/div[2]/div/div/div[2]/div[2]/div[4]/a/img').get_attribute(
            'src')
    except NoSuchElementException:
        pic_4 = 'null'

    try:
        pic_5 = driver.find_element_by_xpath(
            '//*[@id="ProductDetails.Full.View"]/div/div[2]/article/section/div[1]/div/div[2]/div/div/div[2]/div[2]/div[5]/a/img').get_attribute(
            'src')
    except NoSuchElementException:
        pic_5 = 'null'

    try:
        pic_6 = driver.find_element_by_xpath(
            '//*[@id="ProductDetails.Full.View"]/div/div[2]/article/section/div[1]/div/div[2]/div/div/div[2]/div[2]/div[6]/a/img').get_attribute(
            'src')
    except NoSuchElementException:
        pic_6 = 'null'

    try:
        pic_7 = driver.find_element_by_xpath(
            '//*[@id="ProductDetails.Full.View"]/div/div[2]/article/section/div[1]/div/div[2]/div/div/div[2]/div[2]/div[7]/a/img').get_attribute(
            'src')
    except NoSuchElementException:
        pic_7 = 'null'

    product_data = {
        "url_id": product["_id"],
        "page_link": page_link,
        "address": address,
        "category": category,
        "titles": title,
        "part_number": part_number,
        "list_price": list_price,
        "quantity": quantity,
        "description": description,
        "references": references,
        "application": application,
        "pic_1": pic_1,
        "pic_2": pic_2,
        "pic_3": pic_3,
        "pic_4": pic_4,
        "pic_5": pic_5,
        "pic_6": pic_6,
        "pic_7": pic_7,
    }

    product_col = my_db["products"]
    x = product_col.insert_one(product_data)
    print(x.inserted_id)

driver.close()
print("Process finished")
