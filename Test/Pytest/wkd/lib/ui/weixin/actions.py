# coding: utf-8
'''
UI库交互行为基础类
'''
import sys,time,random,re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from ..generic import Generic
from ..conf import *


class Action(object):

    def __init__(self,conf):
        self.conf = conf
        self.G = Generic(conf)


    def click(self,xpath,param=None):
        '''
        点击操作,入参为XPath
        '''
        self.G.click(self.conf.wxdriver,xpath,param)

    def input(self,xpath,value,param=None):
        '''
        输入操作
        '''
        self.G.input(self.conf.wxdriver,xpath,value,param)

    def choose(self,xpath,index=None):
        '''
        单选操作
        '''
        self.G.choose(self.conf.wxdriver,xpath,index)

    def get_text(self,xpath,param=None):
        '''
        获取文本
        '''
        txt = self.G.get_text(self.conf.wxdriver,xpath,param)
        return txt

    def get_value(self,xpath,param=None):
        '''
        获取value
        '''
        val = self.G.get_value(self.conf.wxdriver,xpath,param)
        return val

    def get_attr(self,xpath,param=None):
        '''
        获取属性值
        '''
        val = self.G.get_value(self.conf.wxdriver,xpath,param)
        return val

    def get_url_id(self):
        url = self.conf.wxdriver.current_url
        match = re.findall(r"(?<=\?id=)\d+",url)
        id = match[0]
        return id

    def delete_from_list(self,xpath,index=None,min=None):
        '''
        从列表中删除一个,默认如果元素少于3个则不删除
        '''
        driver = self.conf.wxdriver
        els = WebDriverWait(driver, WAIT_TIME).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
        if min == None and len(els) < 3:
            print("元素少于三个，取消删除...")
            return True
        if index == None:
            index = random.randrange(0,len(els))
        time.sleep(1)
        els[index].click()




