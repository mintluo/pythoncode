#coding=utf-8
__author__ = 'milletluo'

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #导入鼠标操作
from selenium.webdriver.common.keys import Keys #倒入键值操作
import time

myusername = "your_user_name"#帐号
mypassword = "your_password"#密码
signpage = "http://vip.jd.com/home.html" #签到页
browser = webdriver.Chrome()
browser.get(signpage)
try:
    jumplogin = browser.find_element_by_css_selector("#content > div.login-wrap > div.w > div > div.login-tab.login-tab-r > a")#切换到账户登录
    loginname = browser.find_element_by_id("loginname")
    password = browser.find_element_by_id("nloginpwd")
    submit = browser.find_element_by_id("loginsubmit")
    jumplogin.click()
    loginname.send_keys(myusername)
    password.send_keys(mypassword)
    submit.click()
    browser.implicitly_wait(5)
    if len(browser.find_elements_by_css_selector("body > div.floor-vip > div.w.clearfix > div.user-welfare > div.sign-in.signed > div.title")): #判断是否领取
        print("今日已领取!无需重复领取")
    else:
        signsubmit = browser.find_element_by_class_name("icon-sign") #签到规则
        signsubmit.click()
        print("领取成功!")
except:
     print("京豆领取失败!")

time.sleep(5)
#退出驱动
#browser.close()
browser.quit()