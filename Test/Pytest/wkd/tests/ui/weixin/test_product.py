import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert


class TestProduct:
    # UI测试：商品模块
    wx = None
    FLAG = False

    @pytest.fixture(autouse=True)
    def setup(self,conf):
        self.wx = conf.ui.Weixin(conf)
        self.pd = conf.ui.weixin.Product(conf)
        self.conf = conf
        self.LC = self.wx.LOCATOR
        driver = webdriver.Chrome()
        self.driver = driver
        conf.COMMON.wx_login(conf,driver)
        return conf


    def test_product_detail_check(self):
        '''
        用例：商品详情检测
        说明：检查商品详情界面相关操作有效性及数据一致性
        '''
        driver = self.driver
        time.sleep(1)
        self.wx.product.choose_one(name='默认测试商品')
        pd_name = self.wx.get_text(self.LC.PRODUCT['商品名称'])
        price = self.wx.get_text(self.LC.PRODUCT['价格'])
        sales = self.wx.get_text(self.LC.PRODUCT['销量'])
        member_price = self.wx.get_text(self.LC.PRODUCT['会员价'])
        member_rank = self.wx.get_text(self.LC.PRODUCT['会员等级'])
        member_discount = self.wx.get_text(self.LC.PRODUCT['会员折扣'])
        print("名称:%s,价格:%s,销量:%s" %(pd_name,price,sales))
        print("会员价:%s,会员等级:%s,会员折扣:%s" %(member_price,member_rank,member_discount))
        driver.close()

    def test_product_detail_info(self):
        '''
        用例：商品详情页面信息检测
        说明：检查商品详情界面相关操作有效性及数据一致性
        完善度：50%
        '''
        driver = self.driver
        time.sleep(1)
        self.wx.product.choose_one(name='默认测试商品')
        pd_name = self.wx.product.get_text('商品名称')
        price = self.wx.product.get_text('价格')
        sales = self.wx.product.get_text('销量')
        member_price = self.wx.product.get_text('会员价')
        member_rank = self.wx.product.get_text('会员等级')
        member_discount = self.wx.product.get_text('会员折扣')
        #url = driver.current_url
        product_id = self.wx.product.get_current_product_id()
        print("名称:%s,ID:%s,价格:%s,销量:%s" %(pd_name,product_id,price,sales))
        print("会员价:%s,会员等级:%s,会员折扣:%s" %(member_price,member_rank,member_discount))
        driver.close()

    def test_product_list(self):
        '''
        用例: 商品列表界面检测
        '''
        self.wx.product.click('商品分类')
        self.wx.common.click('返回')
        self.wx.product.click('切换显示方式')
        time.sleep(1)
        self.wx.product.click('切换显示方式')

    def test_product_sort(self):
        '''
        用例: 商品列表排序
        '''
        self.wx.product.click('排序')
        self.wx.product.click('低格最低')
        self.wx.product.click('排序')
        self.wx.product.click('销量最高')
        self.wx.product.click('排序')
        self.wx.product.click('最新上架')
        self.wx.product.click('排序')
        self.wx.product.click('默认排序')
        self.driver.close()

    def test_product_buy(self):
        '''
        用例: 商品列表排序
        '''
        pd = self.pd
        pd.choose_one(name='默认测试商品')
        pd.click('立即购买')
        pd.click('确认购买')

        self.driver.close()










