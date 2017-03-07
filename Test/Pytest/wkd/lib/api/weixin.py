# coding: utf-8
import requests
import json
import pytest
from .generic import Generic as g

class Weixin(object):
    '''
    微信前端相关接口
    '''
    def __init__(self,conf):
        self.conf = conf

    def product_category_list(self):
        '''
        商品列表
        '''
        url = "/product/category-list-ajax"
        data = {"pid":0}
        return g.wx_post_requests(self.conf,url, data=data)

    def product_get_detail(self,id):
        '''
        商品详情
        '''
        url = "/product/get-detail-ajax"
        data = {"id":id,"mid":""}
        return g.wx_post_requests(self.conf,url,data=data)

    def order_add(self,data):
        '''
        添加普通订单
        '''
        url = "/order/order-add-ajax"
        return g.wx_post_requests(self.conf,url,data=data)





####
