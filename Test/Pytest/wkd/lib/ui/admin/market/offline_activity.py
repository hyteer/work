# coding: utf-8
'''
线下互动栏：预约活动，摇电视，签到活动，祝福墙UI交互类
'''
import sys,time,random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from . import locators as LC
from ...generic import Generic
from ..actions import Action
from ...conf import *


class OfflineActivity(Action):

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