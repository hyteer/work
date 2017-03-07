# coding: utf-8
"""
微信前端API测试用例
"""
import json,time,datetime
import pytest

TIMER = 0.1

class TestWeixin:

    AUTHOR = 'YT'
    mk = None
    dt = {}
    USER_ID = '13764904'

    @pytest.fixture(autouse=True)
    def setup(self,conf):
        self.wx = conf.api.Weixin(conf)
        self.WX_PARAM = conf.param.Weixin(conf)

    # Test Cases

    def test_product_category_list(self):
        r = self.wx.product_category_list()

    def test_product_get_detail(self):
        '''
        测试产品详情
        '''
        r = self.wx.product_get_detail(289873)


    '''
    def test_order_add(self,conf):
        data = conf.WeixinParam.order_add()
        print("args:",data)
        mk = conf.API['market']()
        r = mk.card_coupons_add(conf,data)
        print "card_id:", r['errmsg']['id']
        self.dt['card_id'] = r['errmsg']['id']
    '''

