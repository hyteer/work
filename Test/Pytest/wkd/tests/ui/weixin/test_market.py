import time,random
import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert


class TestOrder:
    # UI测试：订单模块
    AUTHOR = 'YT'
    wx = None
    FLAG = False

    def add_a_secondkill_act(self,mk,MK_PARAM):
        data1 = MK_PARAM.second_kill_add()
        r1 = mk.second_kill_add(data1)
        id = r1['errmsg']['id']
        data2 = MK_PARAM.second_kill_edit(id)
        print("data:",data2)
        r2 = mk.second_kill_edit(data2)
        r3 = mk.second_kill_open(id)
        return id


    @pytest.fixture(autouse=True)
    def setup(self,conf):
        apimk = conf.api.Market(conf)
        MK_PARAM = conf.param.Market(conf)
        self.second_kill_id = self.add_a_secondkill_act(apimk,MK_PARAM)
        #
        self.wx = conf.ui.Weixin(conf)
        self.conf = conf
        #self.combo = conf.combo.Main(conf)
        self.LC = self.wx.LOCATOR
        driver = webdriver.Chrome()
        self.driver = driver
        conf.COMMON.wx_login(conf,driver)
        return conf

    def test_cancel_specified_order(self):
        '''
        取消指定ID的订单
        '''
        print("ID:%s" % self.second_kill_id)
        pass

