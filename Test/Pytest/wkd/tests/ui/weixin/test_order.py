import time,random
import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
some_cmd_param = ''
def flag(x):
    if x:
        return True
    else:
        return False

class TestOrder:
    # UI测试：订单模块
    AUTHOR = 'YT'
    wx = None
    FLAG = False

    @pytest.fixture(autouse=True)
    def setup(self,conf):
        self.wx = conf.ui.Weixin(conf)
        self.conf = conf
        self.wxurl = conf.url.Weixin(conf)
        self.sp = conf.api.Shop(conf)
        self.SP_PARAM = conf.param.Shop(conf)
        self.check = conf.combo.Check(conf)
        self.LC = self.wx.LOCATOR
        driver = webdriver.Chrome()
        self.driver = driver
        conf.COMMON.wx_login(conf,driver)
        return conf

    @pytest.mark.debug
    def test_cancel_specified_order(self):
        '''
        取消指定ID的订单
        '''
        self.wx.bottom_menu('我')
        self.wx.userhome.click('待付款')
        self.wx.order.click('取消指定订单',997035)
        self.driver.close()

    def test_cancel_random_order(self):
        self.wx.bottom_menu('我')
        self.wx.userhome.click('待付款')
        self.wx.order.choose('取消一个订单')
        self.driver.close()

    def test_buy_order_status(self):
        '''
        订单流程：状态检测
        '''
        #rand = random.randrange(1,3)
        # 下单
        self.wx.product.choose_by_name('通过名称选择一个商品','默认测试商品')
        product_id = self.wx.get_url_id()
        print("ProductId:",product_id)
        self.wx.product.click('立即购买')
        self.wx.product.click('确认购买')
        time.sleep(2)
        self.wx.order.input('留言','请尽快发货！')
        order_id = self.wx.get_url_id()
        # 状态校验：待付款
        self.check.check_order_status(order_id,'待付款')
        self.wx.order.click('其它支付')
        self.wx.order.click("货到付款")
        time.sleep(1)
        # 状态校验：待发货
        self.check.check_order_status(order_id,'待发货')
        time.sleep(1)
        # 发货
        params = self.SP_PARAM.order_deliver(order_id)
        r = self.sp.order_deliver(params)
        # 状态校验：已发货
        self.check.check_order_status(order_id,'待收货')

        # todo 收货

        self.driver.close()



    def test_buy_choose_an_address(self):
        rand = random.randrange(1,3)
        self.wx.product.choose_by_name('通过名称选择一个商品','默认测试商品')
        product_id = self.wx.get_url_id()
        print("ProductId:",product_id)
        self.wx.product.click('立即购买')
        self.wx.product.click('确认购买')
        time.sleep(2)
        #import pdb;pdb.set_trace()
        self.wx.order.click('选择地址')
        order_id = self.wx.get_url_id()
        print("OrderID:%s" % order_id)
        time.sleep(2)
        self.wx.order.click('收货地址列表',order_id)
        self.wx.order.click_one_from_list('选择一条地址')


    @pytest.mark.debug
    def test_temp(self):
        print("debug...")
        #import pdb;pdb.set_trace()

    @pytest.mark.no_cycle
    @pytest.mark.skipif(flag(some_cmd_param),reason="stop...")
    def test_temp_debug(self):
        print("temp debug...")
        #import pdb;pdb.set_trace()

    def test_combo(self):
        #self.wx.combo.check_order_status(13434,'待发货')
        self.combo.temp_combo()
        self.combo.check_order_status(13434,'待发货')
        self.wx.product.choose_by_name('通过名称选择一个商品','默认测试商品')

        pass




#