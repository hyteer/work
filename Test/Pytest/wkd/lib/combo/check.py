import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Check(object):
    '''
    组合操作：校验
    '''

    def __init__(self,conf):
        self.conf = conf
        self.wx = conf.ui.Weixin(conf)
        self.WX_LC = self.wx.LOCATOR
        #self.ADMIN_LC = conf.admin.LOCATOR
        self.SHOP_PARAM = conf.param.Shop
        self.Utils = conf.Utils

    def check_order_status(self,order_id,status):
        newdriver = webdriver.Chrome()
        conf = self.conf
        wxdirver = conf.wxdriver
        conf.COMMON.wx_login(conf,newdriver)
        self.wx.bottom_menu('我')
        if status == '待付款':
            print("--订单状态校验：待付款--")
            self.wx.userhome.click('待付款')
            #import pdb;pdb.set_trace()
            time.sleep(1)
            order_no = self.wx.order.get_text('订单号',order_id)
            status_text = self.wx.order.get_text('订单状态',order_id)
            print("OrderNo:",order_no)
            print("StatusText:",status_text)
            assert status == status_text

        elif status == '待发货':
            print("--订单状态校验：待发货--")
            self.wx.userhome.click('待发货')
            time.sleep(1)
            print("Order_ID:",order_id)
            print("Status:",status)
            order_no = self.wx.order.get_text('订单号',order_id)
            status_text = self.wx.order.get_text('订单状态',order_id)
            print("StatusText:",status_text)
            print("OrderNo:",order_no)
            assert status == status_text

        elif status == '待收货':
            print("--订单状态校验：待收货--")
            self.wx.userhome.click('待收货')
            time.sleep(1)
            order_no = self.wx.order.get_text('订单号',order_id)
            status_text = self.wx.order.get_text('订单状态',order_id)
            print("StatusText:",status_text)
            print("OrderNo:",order_no)
            assert status == status_text


        newdriver.close()
        conf.wxdriver = wxdirver


    def temp_combo(self):
        print("you called combo.")




