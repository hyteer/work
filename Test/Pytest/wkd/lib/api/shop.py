#coding:utf-8

from .generic import Generic as g


class Shop(object):
    '''
    店铺接口
    '''
    def __init__(self,conf):
        self.conf = conf

    ##########################店铺###################################
    def get_shop(self):
        '''
        获取商家信息
        '''
        url = '/shop/get-ajax'
        return g.post_requests(self.conf, url)
    ###########################商品库##################################
    def product_list(self, args):
        '''
        获取商品列表
        '''
        url = "/product/list-ajax"
        return g.post_requests(self.conf, url, args)
    
    def product_on_sale(self, args):
        '''
                上架商品
        '''
        uri = '/product/on-sale-ajax'
        return g.post_requests(self.conf, uri, args)
    
    def product_off_sale(self, args):
        '''
        下架商品
        '''
        uri = "/product/off-sale-ajax"
        return g.post_requests(self.conf, uri, args)
    
    def product_add(self,args):
        '''
        添加商品
        '''
        url = "/product/add-ajax"
        return g.post_requests(self.conf, url, args)
    
    def product_check(self,args):
        '''
        删除商品检查渠道商是否在使用
        '''
        url = "/product/check-product-ajax"
        return g.post_requests(self.conf, url, args)
    def product_del(self, args):
        '''
        删除商品
        '''
        url = "/product/del-ajax"
        return g.post_requests(self.conf, url, args)
    
    ########################document########################
    def document_image(self,param):
        '''
        图库
        '''
        url = '/document/image-ajax'
        return g.post_requests(self.conf, url, param)
    
    def get_system_image(self):
        '''
        获取系统用户头像信息
        '''
        url = '/product/get-system-image'
        return g.post_requests(self.conf, url)
    
    ############################商品分类###############################
    def category_list(self,args):
        '''
        商品分类
        '''
        url = '/product/category-list-ajax'
        return g.post_requests(self.conf, url, args)
    
    def category_add(self, args):
        '''
        添加商品分类
        '''
        url = '/product/category-add-ajax'
        return g.post_requests(self.conf, url, args)
    
    def category_del(self, data):
        '''
        删除商品分类
        '''
        url = '/product/category-del-ajax'
        return g.post_requests(self.conf, url, id=data)
    
    ################################商品规格##############################
    def kind_list(self):
        '''
        商品规格
        '''
        url = '/product/kind-list-ajax'
        return g.post_requests(self.conf, url, page=True)
    
    def kind_value_list(self,kindID):
        '''
        商品规格值
        '''
        url = '/product/kind-value-list-ajax'
        return g.post_requests(self.conf, url,{"product_kind_id":kindID,"isAll":1},header="www-form")
    
    def kind_add(self,args):
        '''
        添加商品规格
        '''
        url = '/product/kind-add-ajax'
        return  g.post_requests(self.conf, url, args)
    
    def kind_del(self, args):
        '''
        删除商品规格
        '''
        url = '/product/kind-del-ajax'
        return g.post_requests(self.conf, url, id=args)
    
    ##############################商品评论###############################
    def comment_without_user(self, args):
        '''
        添加商品评论
        '''
        url = '/product/comment-without-user'
        return g.post_requests(self.conf, url, args)
    
    def comment_list(self):
        '''
        商品评论列表
        '''
        url = '/product/comment-list-ajax'
        return g.post_requests(self.conf, url, page=True)
    
    def comment_del(self, data):
        '''
        删除商品评论
        '''
        url = '/product/comment-del-ajax'
        return g.post_requests(self.conf, url, data)
    
    ############################订单################################
    def order_list(self, data):
        '''
        订单列表
        '''
        url = '/order/list-ajax'
        return g.post_requests(self.conf, url, data)
    
    def refund_list(self, data):
        '''
        售后订单列表
        '''
        url = '/order/refund-list-ajax'
        return g.post_requests(self.conf, url, data)
    
    ########################店铺设置##################################
    def shop_order_auto_settings(self, data):
        '''
        更新订单自动任务设置信息(交易设置)
        '''
        url = '/shop/update-shop-order-auto-settings-ajax'
        return g.post_requests(self.conf, url, data)
    
    def shipping_order_type_status_update(self, data):
        '''
        配送方式对（普通订单，秒杀，拼团，积分商城等类型订单单独适配）
        '''
        url = '/shop/shipping-order-type-status-update'
        return g.post_requests(self.conf, url, data)
    
    def shipping_status_update(self, data):
        '''
        更新商品配送设置（自提&快递）
        '''
        url = '/shop/shipping-status-update'
        return g.post_requests(self.conf, url, data)
    
    def get_used_address_list(self):
        '''
        获取常用地址列表
        '''
        url = '/shop/get-used-address-list-ajax'
        return g.post_requests(self.conf, url, page=True)
    
    def add_used_address(self, args):
        '''
        添加常用地址
        '''
        url = '/shop/add-used-address-ajax'
        return g.post_requests(self.conf, url, args)
    
    def update_used_address(self, args):
        '''
        更新某条常用地址
        '''
        url = '/shop/update-used-address-ajax'
        return g.post_requests(self.conf, url, args)

    ################################ 订单管理 ################################

    def order_deliver(self, data):
        '''
        订单发货
        '''
        url = '/order/deliver-ajax'
        return g.post_requests(self.conf, url, data)

    def order_cancel(self, order_id):
        '''
        订单发货
        '''
        url = '/order/cancel-ajax'
        data = {"order_id":order_id}
        return g.post_requests(self.conf, url, data)
        