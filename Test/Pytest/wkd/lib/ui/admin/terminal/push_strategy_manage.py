# -*- coding: utf-8 -*- 

from ..actions import Action
from . import locators as LC
import random

class PushStrategyManage(Action):
 
    def __init__(self,conf):
        Action.__init__(self,conf)

    def click(self,key,param=None):
        '''
        点击
        '''
        if param:
            super(PushStrategyManage,self).click(LC.PUSH_STRATEGY[key] %param)
        else:
            super(PushStrategyManage,self).click(LC.PUSH_STRATEGY[key])

    def input(self,key,value):
        '''
        输入
        '''
        super(PushStrategyManage,self).input(LC.PUSH_STRATEGY[key], value)

    def xpath_with_index(self,key,index):
        xpath = '(' + LC.PUSH_STRATEGY[key] + ')'+ '[' + str(index) + ']'
        return xpath

    def click_with_index(self,key,index):
        xpath = self.xpath_with_index(key, index)
        super(PushStrategyManage,self).click(xpath)

    def get_matching_xpath_count(self,key):
        '''
        获取xpath个数
        '''
        return(super(PushStrategyManage,self).get_matching_xpath_count(LC.PUSH_STRATEGY[key]))
        
    def get_select_list_items(self,key,attribute='label'):
        return(super(PushStrategyManage,self).get_select_list_items(LC.PUSH_STRATEGY[key],attribute))    
     
    def select_from_list_by_label(self,key,label):
        super(PushStrategyManage,self).select_from_list_by_label(LC.PUSH_STRATEGY[key], label)
        
    def wait_until_element_is_visible(self,key):
        super(PushStrategyManage,self).wait_until_element_is_visible(LC.PUSH_STRATEGY[key])
        
    def choose_response_type(self):
        self.wait_until_element_is_visible('扫码回复模块选择框')
        activityTypeNum = self.get_matching_xpath_count('扫码回复模块活动类型列表')
        print("act type num:",activityTypeNum)
        for i in range(1,activityTypeNum+1):
            try:
                activityNum = self.get_matching_xpath_count('扫码回复模块活动列表')
                print("act num:",activityNum)
                randomAct = random.randint(1,activityNum)
                self.click_with_index('扫码回复模块活动列表', randomAct)
                self.click('扫码回复模块确定按钮')
                break
            except Exception:
                print("this activity type has not acvivities,try next")
                if i <= activityTypeNum:
                    self.click_with_index('扫码回复模块活动类型列表', i+1)