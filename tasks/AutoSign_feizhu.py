#coding=utf-8
__author__ = 'milletluo'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

myusername = "your_user_name"#帐号
mypassword = "your_password"#密码

driver = webdriver.Chrome()
driver.get("https://h5.m.taobao.com/trip/home/index.html?_projVer=0.1.116")
content = driver.find_element_by_css_selector("li[data-trackname='Member']").click()
if driver.title == "会员中心":
    time.sleep(10)
    driver.switch_to.frame(0)
    acount = driver.find_element_by_css_selector("input[name='TPL_username']")
    acount.clear()
    acount.send_keys(myusername)
    time.sleep(2)
    password = driver.find_element_by_css_selector("input[name='TPL_password']")
    password.clear()
    password.send_keys(mypassword)
    time.sleep(2)
    driver.find_element_by_css_selector("button[id='btn-submit']").click()
    while "圆圈" in driver.page_source:
        driver.find_element_by_css_selector("span[class='km-dialog-btn']").click()
        time.sleep(2)
        password = driver.find_element_by_css_selector("input[name='TPL_password']")
        password.clear()
        password.send_keys(mypassword)
        time.sleep(2)
        driver.find_element_by_css_selector("div[class='click2slide-btn']").click()
        time.sleep(4)
        driver.find_element_by_css_selector("button[id='btn-submit']").click()
    time.sleep(5)
    if "立即签到" in driver.page_source:
        driver.find_element_by_css_selector("div[data-ref='76']").click()
    elif "已签到" in driver.page_source:
        driver.find_element_by_css_selector("div[data-ref='78']").click()