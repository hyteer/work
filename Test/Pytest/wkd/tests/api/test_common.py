# coding: utf-8
"""
API测试
"""
import time
import pytest


class TestCommon:

    COVERRAGE = 50
    PRODUCT_ID = 289873

    @pytest.fixture(autouse=True)
    def setup(self,conf):
        self.conf = conf
        self.combo = conf.combo.Main(conf)
        self.mb = conf.api.Member(conf)
        self.mk = conf.api.Market(conf)
        self.sp = conf.api.Shop(conf)
        self.wx = conf.api.Weixin(conf)
        #self.SHOP_PARAM = conf.param.Shop(conf)

    # Tests
    def test_product_list(self):
        r = self.mb.member_list()
        time.sleep(3)

    def test_member_list(self):
        r = self.mb.member_list()
        time.sleep(3)

    def test_card_coupons_list(self):
        r = self.mk.card_coupons_list()

    def test_product_category_list(self):
        r = self.wx.product_category_list()

    def test_product_get_detail(self):
        r = self.wx.product_get_detail(self.PRODUCT_ID)

    @pytest.mark.not_ready
    def test_add_product(self,conf):
        param = conf.SHOP_PARAM(conf).product_add()
        resp = self.sp.product_add(conf, param)
        product_id = resp['errmsg']['product']['id']
        print("ProductID:",product_id)

    @pytest.mark.not_ready
    def test_sets_add_product(self):
        #self.product_id = self.sets.add_a_product()
        self.product_id = self.sets.do('添加一个商品')(onsale=False)

    def test_product_onsale(self):
        id = 289996
        payload = {"ids":[id]}
        self.sp.product_on_sale(payload)

    def test_product_offsale(self):
        id = 289996
        payload = {"ids":[id]}
        self.sp.product_off_sale(payload)

    def test_combo(self):
        #self.wx.combo.check_order_status(13434,'待发货')
        self.combo.temp_combo()
        pass




