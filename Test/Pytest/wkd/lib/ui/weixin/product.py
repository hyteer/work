# coding: utf-8
'''
Weixin UI库：商品模块
'''
import sys,time,random,re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from . import locators as LC
from ..generic import Generic
from .actions import Action
from ..conf import *



class Product(Action):

    def __init__(self,conf):
        Action.__init__(self,conf)

    def click(self,key):
        self.G.click(self.conf.wxdriver,LC.PRODUCT[key])

    def click_one_from_list(self,key,index=None):
        '''
        从元素组中选择一个
        '''
        self.G.click_one_from_list(self.conf.wxdriver,LC.PRODUCT[key],index)

    def input(self,key,value):
        '''
        输入Input值,name为对应的XPATH字典key
        '''
        xpath = LC.PRODUCT[key]
        self.G.input(self.conf.wxdriver,xpath=xpath,value=value)

    def get_text(self,key):
        '''
        获取文本
        '''
        txt = self.G.get_text(self.conf.wxdriver,LC.PRODUCT[key])
        return txt

    def get_current_product_id(self):
        url = self.conf.wxdriver.current_url
        match = re.findall(r"(?<=\?id=)\d+",url)
        product_id = match[0]
        return product_id

    def choose(self,key,index=None):
        '''
        选择
        '''
        self.G.choose(self.conf.wxdriver,LC.PRODUCT[key],index)

    def choose_by_name(self,key,name):
        '''
        通过名称选择一个元素
        '''
        self.G.click(self.conf.wxdriver,LC.PRODUCT[key] % name)


