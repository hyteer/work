# coding: utf-8
import sys,time,random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .conf import *

class Generic(object):

    def __init__(self,conf):
        self.conf = conf

    def input(self,driver,xpath,value,param):
        if param:
            #import pdb;pdb.set_trace()
            xpath = xpath % param
        element = WebDriverWait(driver, TIME_OUT).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        time.sleep(1)
        #text = element.text
        #if text:
        element.clear()
        time.sleep(0.5)
        element.send_keys(value)
        time.sleep(1)

    def click(self,driver,xpath,param=None):

        #element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(xpath=xpath))
        if param:
            #import pdb;pdb.set_trace()
            xpath = xpath % param
        element = WebDriverWait(driver, TIME_OUT).until(EC.presence_of_element_located((By.XPATH, xpath)))
        time.sleep(1)
        element.click()
        time.sleep(0.8)

    def click_one_from_list(self,driver,xpath,index=None):
        '''
        从元素组中选择一个
        '''
        els = WebDriverWait(driver, TIME_OUT).until(EC.presence_of_all_elements_located((By.XPATH,xpath)))
        if index == None:
            index = random.randrange(0,len(els))
        time.sleep(1)
        els[index].click()
        time.sleep(1)

    def choose(self,driver,xpath,index=None,param=None):
        '''
        从元素组中选择一个
        '''
        if param:
            xpath = xpath % param
        els = WebDriverWait(driver, TIME_OUT).until(EC.presence_of_all_elements_located((By.XPATH,xpath)))
        if index == None:
            index = random.randrange(0,len(els))
        time.sleep(1)
        els[index].click()
        time.sleep(1)


    def get_text(self,driver,xpath,param=None):
        '''
        获取元素文本值
        '''
        if param:
            xpath = xpath % param
        text = WebDriverWait(driver, TIME_OUT).until(EC.presence_of_element_located((By.XPATH, xpath))).text
        return text

    def get_value(self,driver,xpath,param=None):
        '''
        获取元素value
        '''
        if param:
            xpath = xpath % param
        value = WebDriverWait(driver, TIME_OUT).until(EC.presence_of_element_located((By.XPATH, xpath))).get_attribute('value')
        return value

    def get_element(self,driver,xpath,param=None):
        '''
        获取元素
        '''
        if param:
            xpath = xpath % param
        el = WebDriverWait(driver, TIME_OUT).until(EC.presence_of_element_located((By.XPATH, xpath)))
        return el


