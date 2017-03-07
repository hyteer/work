# coding: utf-8
'''
营销API参数化配置
'''
from .utils import Utils
import time
from .generic import Generic as g


class Weixin(object):

    def __init__(self,conf):
        self.conf = conf
        self.Utils = conf.Utils

    @staticmethod
    def order_add(product_id,sku_id,num,pickup_type,**kwargs):
        '''
        创建普通订单常用参数表
    =============     ===========    ============     =================================================
     字段              类型              默认               描述
    =============     ===========    ============     =================================================
     product_id        string          无               (必填)商品ID
     sku_id            int             无               (必填)商品规格ID
     num               int             1                购买数量
     pickup_type       int             1                提货方式（1.普通发货。2.到店自提。4.同城配送）
    =============     ===========    ============     =================================================

        '''
        template = {"products[0][id]":product_id,"products[0][sku_id]":sku_id,"products[0][num]":num,"pickup_type":pickup_type}
        return g.get_params(template,kwargs)