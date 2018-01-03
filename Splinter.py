#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   Jack.Xu
#   E-mail  :   xuxiangxiaoup@163.com
#   Date    :   18/01/03 14:11:35
from splinter import Browser
from xvfbwrapper import Xvfb
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-setuid-sandbox")

browser = Browser('chrome',options=chrome_options,executable_path='/usr/bin/chromedriver')
browser.visit('forxu.cn:80')
print browser.title

browser.quit()
