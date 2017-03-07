# coding: utf-8
'''
Weixin UI库：购物车模块
'''
import sys,time,random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from . import locators as LC
from ..generic import Generic
from .actions import Action
from ..conf import *



class Cart(Action):

    def __init__(self,conf):
        Action.__init__(self,conf)

    def click(self,name):
        '''
        说明：购物车点击控件,name为控件对应的key
        '''
        self.G.click(self.conf.wxdriver,LC.CART[name])

    def choose_one(self,name=None,index=0):
        '''
        说明：在购物车中通过index选择一个商品
        '''
        driver = self.conf.wxdriver
        driver.implicitly_wait(WAIT_TIME)
        if name:
            xpath = '//div[@class="goods-li-right"]/div[text()="' + name + '"]/ancestor::a[@on-finished="goodsListRepeatFinished"]'
            el = WebDriverWait(driver, WAIT_TIME).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            time.sleep(1)
            el.click()
        else:
            xpath = LC.CART['选择商品']
            els = WebDriverWait(driver, WAIT_TIME).until(EC.presence_of_all_elements_located((By.XPATH,xpath)))
            time.sleep(1)
            els[index].click()

    def choose_by_product_id(self,product_id):
        '''
        说明：在购物车中根据商品ID选择特定商品
        '''
        driver = self.conf.wxdriver
        xpath = '//a[@href="../product/detail?id=%s"]/ancestor::li[@ng-repeat="list in model"]//i[@ng-click="changeCheck($index, list)"]' % product_id
        el = WebDriverWait(driver, WAIT_TIME).until(EC.presence_of_element_located((By.XPATH, xpath)))
        time.sleep(WAIT_TIME)
        el.click()



