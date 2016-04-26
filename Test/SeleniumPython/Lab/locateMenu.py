# _*_ coding: utf-8 _*_
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
# create a session
dr = webdriver.Firefox()
file_path = "file:///" + os.path.abspath('DemoSite/level_locate.html')
dr.get(file_path)
# find menu
dr.find_ele


