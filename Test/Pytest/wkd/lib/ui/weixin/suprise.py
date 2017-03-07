# coding: utf-8
'''
Weixin UI库交互类:惊喜活动
'''
import sys,time,random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from . import locators as LC
from ..generic import Generic
from .actions import Action
from ..conf import *



class Suprise(Action):

    def __init__(self,conf):
        Action.__init__(self,conf)

    def click(self,name):
        '''
        点击
        '''
        self.G.click(self.conf.wxdriver,LC.USERHOME[name])



