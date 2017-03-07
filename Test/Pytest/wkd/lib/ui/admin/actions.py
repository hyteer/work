# coding: utf-8
'''
UI库交互行为基础类
'''
import sys,time,random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from ..generic import Generic
from ..conf import *


class Action(object):
    

    def __init__(self,conf):
        self.conf = conf
        self.G = Generic(conf)



    def click(self,xpath):
        '''
        点击操作,入参为XPath
        '''
        self.G.click(self.conf.driver,xpath)

    def input(self,xpath,value):
        '''
        输入操作
        '''
        self.G.input(self.conf.driver,xpath=xpath,value=value)

    def choose(self,xpath,index=None):
        '''
        单选操作
        '''
        self.G.choose(self.conf.driver,xpath,index)

    def get_text(self,xpath):
        '''
        获取文本
        '''
        txt = self.G.get_text(self.conf.driver,xpath)
        return txt

    def get_value(self,xpath):
        '''
        获取value
        '''
        val = self.G.get_value(self.conf.driver,xpath)
        return val

    def get_attr(self,xpath):
        '''
        获取属性值
        '''
        val = self.G.get_value(self.conf.driver,xpath)
        return val

    def delete_from_list(self,xpath,index=None,min=None):
        '''
        从列表中删除一个,默认如果元素少于3个则不删除
        '''
        driver = self.conf.wxdriver
        #G.click(self.conf,CF.SUPRRISE[key])
        els = WebDriverWait(driver, WAIT_TIME).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
        #import pdb;pdb.set_trace()
        if min == None and len(els) < 3:
            print("元素少于三个，取消删除...")
            return True
        if index == None:
            index = random.randrange(0,len(els))
        time.sleep(1)
        els[index].click()
        
    def get_matching_xpath_count(self,xpath):
        '''
        获取符合xpath元素的个数
        '''    
        elements = self._find_elements(xpath)
        return len(elements)
    
    def get_checkbox_status(self,xpath):
        '''
        获取checkbox的状态
        '''
        status = WebDriverWait(self.conf.driver, TIME_OUT).until(EC.element_located_to_be_selected((By.XPATH,xpath)))
        return status
    
    def click_link(self,linktext):
        '''
        点击链接
        '''
        element = self._find_element(linktext, By.LINK_TEXT)
        time.sleep(1)
        element.click()
        time.sleep(0.8)
    
    def get_select_list_items(self,xpath,item='label'):
        '''
        item = label获取select下拉列表label值,item=value获取select下拉列表value值
        '''
        element = self._find_element(xpath)
        return self._get_labels_for_options(Select(element).options,item)
    
    def select_from_list_by_index(self, xpath, index):
        element = self._find_element(xpath)
        Select(element).select_by_index(index)

    def select_from_list_by_label(self, xpath, label):
        element = self._find_element(xpath)
        Select(element).select_by_visible_text(label)
        
    def select_frame(self,xpath):
        element = self._find_element(xpath)
        self.conf.driver.switch_to.frame(element)
        
    def _find_element(self, value, by=By.XPATH):
        element = WebDriverWait(self.conf.driver, TIME_OUT).until(EC.presence_of_element_located((by, value)))
        return element
    
    def _find_elements(self, value, by=By.XPATH):
        elements = WebDriverWait(self.conf.driver, TIME_OUT).until(EC.presence_of_all_elements_located((by,value)))
        return elements
    
    def wait_until_element_is_visible(self,xpath):  
        WebDriverWait(self.conf.driver, TIME_OUT).until(EC.visibility_of_element_located((By.XPATH,xpath)))
    
    def _get_labels_for_options(self, options,item):
        items = []
        for option in options:
            if item == 'label':
                items.append(option.text)
            else:
                items.append(option.get_attribute('value'))
        return items
    