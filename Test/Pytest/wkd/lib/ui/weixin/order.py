# coding: utf-8
'''
Weixin UI库：订单模块
'''
import sys,time,random,re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from . import locators as LC
from ..generic import Generic
from .actions import Action
from ..conf import *



class Order(Action):

    def __init__(self,conf):
        Action.__init__(self,conf)

    def click(self,key,param=None):
        self.G.click(self.conf.wxdriver,LC.ORDER[key],param)

    def click_one_from_list(self,key,index=None):
        '''
        从元素组中选择一个
        '''
        self.G.click_one_from_list(self.conf.wxdriver,LC.ORDER[key],index)

    def input(self,key,value,param=None):
        '''
        输入Input值,name为对应的XPATH字典key
        '''
        xpath = LC.ORDER[key]
        self.G.input(self.conf.wxdriver,xpath,value,param)

    def get_text(self,key,param=None):
        '''
        获取文本
        '''
        return self.G.get_text(self.conf.wxdriver,LC.ORDER[key],param)

    def get_element(self,key,param=None):
        '''
        获取元素
        '''
        return self.G.get_element(self.conf.wxdriver,LC.ORDER[key],param)

    def get_current_product_id(self):
        url = self.conf.wxdriver.current_url
        match = re.findall(r"(?<=\?id=)\d+",url)
        product_id = match[0]
        return product_id

    def choose(self,key,index=None):
        '''
        从元素组中选择一个
        '''
        self.G.choose(self.conf.wxdriver,LC.ORDER[key],index=None)

    def click_by_order_id(self,key,id):
        driver = self.conf.wxdriver
        #import pdb;pdb.set_trace()
        xpath = LC.ORDER[key] % str(id)
        el = WebDriverWait(driver, WAIT_TIME).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        time.sleep(1)
        el.click()

