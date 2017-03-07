# -*- coding: utf-8 -*- 

import pytest,time,random
from selenium import webdriver

class TestPushStrategyManage(object):
    
    @pytest.fixture(autouse=True)
    def setup(self,conf):
        self.conf = conf
        self.terminal = conf.ui.admin.terminal.Terminal(conf)
        self.driver = webdriver.Chrome()
        conf.COMMON.login(conf,self.driver)
        #切换至分店类别页面
        self.terminal.push_strategy_manage.click_link('微分店')
        self.terminal.push_strategy_manage.click_link('微分店')
        self.terminal.push_strategy_manage.click_link('分店码推送策略')    
    
    def test_add_shop_strategy(self):
        pushStrategy = self.terminal.push_strategy_manage
        pushStrategy.click_link('添加分店码推送策略')
        #策略名称
        timeStr = time.strftime("%m%d%H%M",time.localtime())
        strategyName = timeStr + '门店码推送策略'
        pushStrategy.input("门店码推送策略名称输入框",strategyName)
        #生效时间
#         pushStrategy.click('门店码推送策略开始时间输入框')
#         pushStrategy.click('门店码推送策略结束时间输入框')
        #推送动作
        pushStrategy.select_from_list_by_label('推送动作下拉列表','扫码回复模块')
        pushStrategy.choose_response_type()
        self.driver.close()