import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert


class TestAddress:
    # 测试UI库Address模块
    AUTHOR = 'YT'
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

    def test_add_address(self):
        '''
        新地一条收货地址
        '''
        driver = self.driver
        address = self.wx.address
        self.wx.bottom_menu('我')
        address.click('我的地址')
        address.click('新增收货地址')
        address.input('收货人',self.conf.Utils.rand_name())
        address.input('手机号码',self.conf.Utils.rand_mobile())
        address.click('所在地区')
        address.choose('选择省')
        address.choose('选择市')
        address.choose('选择区')
        time.sleep(1)
        address.input('详细地址','XX街道XX号')
        address.click('设为默认地址')
        self.wx.common.click('保存')
        driver.close()

    def test_address_set_default(self):
        '''
        随机设置一条默认地址
        '''
        driver = self.driver
        self.wx.bottom_menu('我')
        self.wx.address.click('我的地址')
        self.wx.address.choose('从地址列表中设为默认')
        driver.close()

    def test_address_edit(self):
        '''

        :return:
        '''
        driver = self.driver
        self.wx.bottom_menu('我')
        self.wx.address.click('我的地址')
        self.wx.address.click('编辑')
        time.sleep(1)
        self.wx.address.input('收货人',self.conf.Utils.rand_name())
        self.wx.address.input('手机号码',self.conf.Utils.rand_mobile())
        self.wx.address.click('所在地区')
        self.wx.address.choose('选择省')
        self.wx.address.choose('选择市')
        self.wx.address.choose('选择区')
        time.sleep(1)
        self.wx.address.input('详细地址','XX路XX小区XX号')
        self.wx.address.click('设为默认地址')
        self.wx.common.click('保存')
        driver.close()

    def test_address_del(self):
        '''

        :return:
        '''
        driver = self.driver
        self.wx.bottom_menu('我')
        self.wx.address.click('我的地址')
        self.wx.address.click('删除')
        self.wx.common.click('确认')
        driver.close()





