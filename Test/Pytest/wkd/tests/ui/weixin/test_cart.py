import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert


class TestCart:
    # 测试UI库Action类相关方法
    wx = None
    FLAG = False

    @pytest.fixture(autouse=True)
    def setup(self,conf):
        self.conf = conf
        self.wx = conf.ui.Weixin(conf)
        self.LC = self.wx.LOCATOR
        driver = webdriver.Chrome()
        self.driver = driver
        conf.COMMON.wx_login(conf,driver)
        return conf

    def test_cart_choose(self):
        self.wx.bottom_menu('购物车')
        self.driver.back()
        time.sleep(2)
        self.wx.click(self.LC.BOTTOM_MENU['我'])
        self.driver.close()

    def test_cart_add_num(self):
        driver = self.driver
        self.wx.product.choose_one(name='默认测试商品')
        self.wx.product.click('购物车')
        num = self.wx.get_value(self.LC.PRODUCT['数量'])
        if int(num) <= 3:
            self.wx.cart.click('加')
            self.wx.cart.click('加')
        self.wx.cart.click('减')
        driver.close()

    def test_add_to_cart(self):
        '''
        用例：添加商品到购物车
        说明：检测商品限购，添加后自动删除
        '''
        driver = self.driver
        time.sleep(1)
        self.wx.product.choose_one(name='默认测试商品')
        product_id = self.wx.product.get_current_product_id()
        self.wx.product.click('加入购物车')
        self.wx.product.input(key='数量',value='6')
        self.wx.product.click('确定_加入购物车')
        alert_text = Alert(driver).text
        print("Alert:%s" % alert_text)
        assert alert_text == '超过限购数量'
        Alert(driver).dismiss()
        self.wx.product.input(key='数量',value='1')
        self.wx.product.click('确定_加入购物车')
        time.sleep(1)
        self.wx.product.click('购物车')
        self.wx.cart.choose_by_product_id(product_id)
        self.wx.cart.click('删除')
        self.wx.common.click('确定')
        driver.close()

    def test_buy_from_cart(self):
        '''
        用例: 从购物车购买商品
        '''
        product_id = '289873'
        self.wx.product.choose_one(name='默认测试商品')
        self.wx.product.click('加入购物车')
        self.wx.product.click('确定_加入购物车')
        time.sleep(1)
        self.wx.product.click('购物车')
        self.wx.cart.choose_by_product_id(product_id)
        self.wx.cart.click('去结算')








