# coding: utf-8
'''
Weixin UI库交互类
'''
import sys,time,random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from . import locators as LC
from ..generic import Generic
from .actions import Action
from ..conf import *


class Address(Action):

    def __init__(self,conf):
        Action.__init__(self,conf)

    def click(self,key):
        '''
        点击
        '''
        self.G.click(self.conf.wxdriver,LC.ADDRESS[key])

    def input(self,key,value):
        '''
        输入
        '''
        self.G.input(self.conf.wxdriver,xpath=LC.ADDRESS[key],value=value)

    def choose(self,key,index=None):
        '''
        选择
        '''
        self.G.choose(self.conf.wxdriver,LC.ADDRESS[key],index)

