# coding: utf-8
'''
促销活动栏：秒杀活动，拼团活动，满减包邮UI交互类
'''
import sys,time,random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from . import locators as LC
from selenium.webdriver.support.select import Select
from ...generic import Generic
from ..actions import Action
from ...conf import *


class SalesActivity(Action):

    def __init__(self,conf):
        Action.__init__(self,conf)

    def click(self,key,param=None):
        '''
        点击
        '''
        if param:
            #import pdbpdb.set_trace()
            self.G.click(self.conf.driver, LC.SECOND_KILL_MENU[key] % param)
        else:
            self.G.click(self.conf.driver,LC.SECOND_KILL_MENU[key])

    def input(self,key,value):
        '''
        输入
        '''
        self.G.input(self.conf.driver,xpath=LC.SECOND_KILL_MENU[key],value=value)

    def choose(self,key,index=None):
        '''
        选择
        '''
        self.G.choose(self.conf.driver,LC.SECOND_KILL_MENU[key],index)

    def get_value(self, key):
        '''
        获取元素value
        '''
        self.G.get_value(self.conf.driver, LC.SECOND_KILL_MENU[key])


    def xpath_with_index(self, key, index):
        xpath = '(' + LC.SECOND_KILL_MENU[key] + ')' + '[' + str(index) + ']'
        return xpath


    def get_matching_xpath_count(self,key):
        '''
        获取xpath个数
        '''
        return(super(SalesActivity,self).get_matching_xpath_count(LC.SECOND_KILL_MENU[key]))



    def get_text(self,key,param=None):
        '''
        获取文本
        '''
        if param:
            #import pdb pdb.set_trace()
            txt = self.G.get_text(self.conf.driver,LC.SECOND_KILL_MENU[key] % param)
            return txt
        else:
            txt = self.G.get_text(self.conf.driver, LC.SECOND_KILL_MENU[key])
            return txt



    def get_second_kill_status(self, index):
        '''
        获取活动状态
        '''
        xpath = self.xpath_with_index("活动状态栏", index)
        return self.get_checkbox_status(xpath)



    def select_checkbox(self):
        '''选择按钮checkbox'''
        driver = self.conf.driver
        driver.implicitly_wait(10)
        value0 = [ "1", "2", "3"]
        value = random.choice(value0)
        #import pdb pdb.set_trace()
        xpath='//input[@name="offline" and @value='+str(value)+']'
        ele1 = WebDriverWait(driver, 20).until(lambda x: x.find_element_by_xpath(xpath=xpath))
        ele1.click()
        time.sleep(1)


    def check_second_kill_info(self,second_killList):
        '''
        秒杀活动页面校验
        '''
        second_killNum=len(second_killList)
        for i in range(second_killNum):
            #活动名称
            activityNameXpath=self.xpath_with_index("活动名称栏",i+1)
            activityName=super(SalesActivity,self).get_text(activityNameXpath)
            assert second_killList[i]['name'] == activityName

            #活动类型
            activityTypeXpath=self.xpath_with_index("活动类型栏",i+1)
            activityType=super(SalesActivity,self).get_text(activityTypeXpath)
            if activityType=='开放性活动':
                assert second_killList[i]['share_type'] == 1
            elif activityType=='线下分享活动':
                assert second_killList[i]['share_type'] == 2
            else:
                assert second_killList[i]['share_type'] == 3

            #关联商品数
            seckillGoodsCountXpath=self.xpath_with_index("关联商品数栏",i+1)
            GoodsCount=super(SalesActivity,self).get_text(seckillGoodsCountXpath)  #字符串
            a=second_killList[i]['seckillGoodsCount']      #int
            b=str(a)      #将str转换成int
            assert b==GoodsCount

            # 开始时间
            startTimeXpath = self.xpath_with_index("开始时间栏", i + 1)
            startTime = super(SalesActivity, self).get_text(startTimeXpath)
            startTimestr=second_killList[i]['start_time']
            time.strptime(startTime, '%Y-%m-%d %H:%M:%S')
            localtime=time.localtime(startTimestr)
            newstarttime=time.strftime('%Y-%m-%d %H:%M:%S',localtime)
            newstarttimestr=str(newstarttime)
            assert startTime==newstarttimestr

            # 结束时间
            endTimeXpath = self.xpath_with_index("结束时间栏", i + 1)
            endTime = super(SalesActivity, self).get_text(endTimeXpath)
            endTimestr=second_killList[i]['end_time']
            time.strptime(endTime, '%Y-%m-%d %H:%M:%S')
            localtime = time.localtime(endTimestr)
            newendtime=time.strftime('%Y-%m-%d %H:%M:%S',localtime)
            assert endTime == str(newendtime)









































