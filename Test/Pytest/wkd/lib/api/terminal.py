# coding: utf-8
import requests
import json
from .generic import Generic as g


class Terminal(object):
    '''

    '''
    def __init__(self,conf):
        self.conf = conf

############################# 分店管理 ############################
    def terminal_list(self, args):
            '''
            获取分店列表
            '''
            url = "/terminal/list-ajax"
            return g.post_requests(self.conf, url, args, terminal=True)

    def terminal_add(self, args):
            '''
            添加分店
            '''
            url = "/terminal/add-ajax"
            return g.post_requests(self.conf, url, args, terminal=True)
        
    def terminal_edit(self, args):
        '''
        修改分店信息
        '''
        url = '/terminal/edit-ajax'
        return g.post_requests(self.conf, url, args,terminal=True)
    
    def find_wxshop_category(self, param):
        '''
        查询微信店铺分类
        '''
        url = '/common/find-wxshop-category-ajax'
        return g.post_requests(self.conf, url, param,terminal=True)
    
    def main_sub_open(self):
        '''
        开启分店店铺模式
        '''
        url = '/shop/main-sub-open-ajax'
        return g.post_requests(self.conf, url, id=self.conf.SHOP_ID, terminal=True)    
    
    def main_sub_close(self):
        '''
        关闭分店店铺模式
        '''
        url = '/shop/main-sub-close-ajax'
        return g.post_requests(self.conf, url, id=self.conf.SHOP_ID, terminal=True)
    
    def single_setting_open(self):
        '''
        开启分店独立库存和价格
        '''
        url = '/shop/single-setting-open-ajax'
        return g.post_requests(self.conf, url, id=self.conf.SHOP_ID, terminal=True)
    
    def single_setting_close(self):
        '''
        关闭分店独立库存和价格
        '''
        url = '/shop/single-setting-close-ajax'
        return g.post_requests(self.conf, url, id=self.conf.SHOP_ID, terminal=True)

###########################分店商品管理#########################
    def product_list(self, args):
        '''
        分店商品列表
        '''
        url = '/terminal/product-list-ajax'
        return g.post_requests(self.conf, url, args, terminal=True)
    
    def sub_shop_product_list(self, args):
        '''
        分店商品设置
        '''
        url = '/terminal/sub-shop-product-list-ajax'
        return g.post_requests(self.conf, url, args,terminal=True)
    
    def sub_product_update(self, args):
        '''
        更新分店商品配送与上下架信息
        '''
        url = '/terminal/sub-product-update-ajax'
        return g.post_requests(self.conf, url, args, terminal=True)
    
    def sub_sku_arr_update(self, args):
        '''
        更新分店商品库存
        '''
        url = '/terminal/sub-sku-arr-update-ajax'
        return g.post_requests(self.conf, url, args, terminal=True)
    
    def set_main_sub(self, terminalID):
        '''
        设置默认分店
        '''
        url = '/terminal/set-main-sub-ajax'
        return g.post_requests(self.conf, url, id=terminalID, terminal=True)
    
    #####################收银台管理###########################
    def terminal_scan_pay_open(self,terminalID):
        '''
        开启收款码
        '''
        url = '/terminal/scan-pay-open-ajax'
        return g.post_requests(self.conf, url, id=terminalID, terminal=True)
    
    def terminal_scan_pay_close(self, terminalID):
        '''
        关闭收款码
        '''
        url = '/terminal/scan-pay-close-ajax'
        return g.post_requests(self.conf, url, id=terminalID, terminal=True)
    
    def staff_list(self, args):
        '''
        分店员工列表
        '''
        url = '/staff/list-ajax'
        return g.post_requests(self.conf, url, args, terminal=True)
    
    def staff_scan_pay_open(self, staffID):
        '''
        开启员工收款码
        '''
        url = '/staff/scan-pay-open-ajax'
        return g.post_requests(self.conf, url, id=staffID, terminal=True)
    
    def staff_scan_pay_close(self, staffID):
        '''
        关闭员工收款码
        '''
        url = '/staff/scan-pay-close-ajax'
        return g.post_requests(self.conf, url, id=staffID, terminal=True)
   
    def staff_pay_refund_open(self, staffID):
        '''
        开启员工退款权限
        '''
        url = '/staff/scan-pay-refund-open-ajax'
        return g.post_requests(self.conf, url, id=staffID, terminal=True)
    
    def staff_pay_refund_close(self, staffID):
        '''
        关闭员工退款权限
        '''
        url = '/staff/scan-pay-refund-close-ajax'
        return g.post_requests(self.conf, url, id=staffID, terminal=True)
    
    def statement_hq(self, args):
        '''
        总部结算
        '''
        url = '/statement/statement-hq'
        return g.post_requests(self.conf, url, args, terminal=True)
    
    def statement_sub(self, args):
        '''
        分店独立结算
        '''
        url = '/statement/statement-sub'
        return g.post_requests(self.conf, url, args, terminal=True)
    
    def statement_find_push_record(self, args):
        '''
        消息推送记录
        '''
        url = '/statement/find-push-record'
        return g.post_requests(self.conf, url, args, terminal=True)
    
    ######################分店满减送活动########################
    def terminal_reduction_list(self, args):
        '''
        分店收款码满减送列表
        '''
        url = '/terminal-reduction/list-by-terminal-ajax'
        return g.post_requests(self.conf, url, args, terminal=True)
    
    def terminal_reduction_add(self, args):
        '''
         添加分店收款码满减送活动
        '''
        url = '/terminal-reduction/add-by-terminal-ajax'
        return g.post_requests(self.conf, url, args, terminal=True)
    
    def terminal_reduction_open(self, reductionID):
        '''
        开启分店收款码满减送活动
        '''
        url = '/terminal-reduction/open-by-terminal-ajax'
        return g.post_requests(self.conf, url, id=reductionID, terminal=True)

    def terminal_reduction_close(self, reductionID):
        '''
        关闭分店收款码满减送活动
        '''
        url = '/terminal-reduction/close-by-terminal-ajax'
        return g.post_requests(self.conf, url, id=reductionID, terminal=True)    
    
    def reduction_store_list(self, args):
        '''
        已选择的门店（包含代理商终端店信息）
        '''
        url = '/terminal-reduction/reduction-store-list-ajax'
        return g.post_requests(self.conf, url, args, terminal=True)
    
    def terminal_reduction_delete(self, reductionID):
        '''
        删除门店满减活动
        '''
        url = '/terminal-reduction/delete-by-terminal-ajax'
        return g.post_requests(self.conf, url, id=reductionID, terminal=True)
    
    def staff_reduction_list(self, data):
        '''
        获取员工满减活动列表
        '''
        url = '/terminal-reduction/list-by-staff-ajax'
        return g.post_requests(self.conf, url, data, terminal=True)
    
    def reduction_staff_list(self, data):
        '''
        已选择的员工
        '''
        url = '/terminal-reduction/reduction-staff-list-ajax'
        return g.post_requests(self.conf, url, data, terminal=True)
    
    def staff_reduction_add(self, args):
        '''
        添加员工收款码满减送
        '''
        url = '/terminal-reduction/add-by-staff-ajax'
        return g.post_requests(self.conf, url, args, terminal=True)
    
    def staff_reduction_open(self, reductionID):
        '''
        开启分店收款码满减送活动
        '''
        url = '/terminal-reduction/open-by-staff-ajax'
        return g.post_requests(self.conf, url, id=reductionID, terminal=True)

    def staff_reduction_close(self, reductionID):
        '''
        关闭分店收款码满减送活动
        '''
        url = '/terminal-reduction/close-by-staff-ajax'
        return g.post_requests(self.conf, url, id=reductionID, terminal=True)     
    
    def staff_reduction_delete(self, reductionID):
        '''
        删除员工收款码满减送
        '''
        url = '/terminal-reduction/delete-by-staff-ajax'
        return g.post_requests(self.conf, url, id=reductionID, terminal=True)
    
    #######################分店数据统计############################
    
    def order_statistics_by_shop(self, args):
        '''
        根据门店统计订单、对账单统计、结算信息
        '''
        url = '/data/order-by-shop-ajax'
        return g.post_requests(self.conf, url, args, terminal=True)
    
    def order_statistics_by_staff(self, args):
        '''
        根据员工统计订单、对账单统计、结算信息
        '''
        url = '/data/order-by-staff-ajax'
        return g.post_requests(self.conf, url, args, terminal=True)
    
    def aftersales_statistics_by_shop(self, args):
        '''
        售后订单按门店统计
        '''
        url = '/data/after-sales-by-shop-ajax'
        return g.post_requests(self.conf, url, args, terminal=True)
    
    def aftersale_statistics_by_staff(self, args):
        '''
        售后订单按员工统计
        '''
        url = '/data/after-sales-by-staff-ajax'
        return g.post_requests(self.conf, url, args, terminal=True)
    
    def member_statistics_by_shop(self, args):
        '''
        会员统计按门店
        '''
        url = '/data/member-statistics-ajax'
        return g.post_requests(self.conf, url, args, terminal=True)
    
    def member_statistics_by_staff(self, args):
        '''
        会员统计按员工
        '''
        url = '/data/member-staff-statistics-ajax'
        return g.post_requests(self.conf, url, args, terminal=True)
    
    def customer_statistics_by_shop(self, args):
        '''
        客户统计按门店
        '''
        url = '/data/member-by-shop-ajax'
        return g.post_requests(self.conf, url, args, terminal=True)
    
    def customer_statistics_by_staff(self, args):
        '''
        客户统计按员工
        '''
        url = '/data/member-by-staff-ajax'
        return g.post_requests(self.conf, url, args, terminal=True)
    
    def promotion_statistics_by_shop(self, args):
        '''
        推广统计按门店
        '''
        url = '/data/fx-by-shop-ajax'
        return g.post_requests(self.conf, url, args, terminal=True)
    
    def promotion_statistics_by_staff(self, args):
        '''
        推广统计按员工
        '''
        url = '/data/fx-by-staff-ajax'
        return g.post_requests(self.conf, url, args, terminal=True)
    
    def promotion_statistics_by_promoter(self, args):
        '''
        推广统计按推广员
        '''
        url = '/data/fx-by-member-ajax'
        return g.post_requests(self.conf, url, args, terminal=True)
    
    ######################分店##########################
    #####分店信息######
    def get_agent_franchisee(self, terminalID):
        '''
        获取分店信息
        '''
        url = '/terminal/get-agent-franchisee-ajax'
        return g.post_requests(self.conf, url, id=terminalID, terminal=True)
    
    def qrcode_detail(self, paramData):
        '''
        分店二维码
        '''
        url = '/weixin/qrcode-detail-ajax'
        return g.post_requests(self.conf, url, data=paramData, terminal=True)
    
    #########收款账户设置############
    def statement_receive_setting(self, param):
        '''
        收款账户设置
        '''
        url = '/terminal/statement-receive-setting-ajax'
        return g.post_requests(self.conf, url, data=param, terminal=True)
    
    #########员工列表#########
    def role_add(self, param):
        '''
        添加分店角色
        '''
        url = '/role/add-ajax'
        self.conf.HEADERS['Referer']= self.conf.URL_TERMINAL+'/role/add?terminal_id='+str(self.conf.TERMINAL_ID)+'&shopType=1'
        response = g.post_requests(self.conf, url, data=param, header='x-www-form-urlencoded', terminal=True)
        self.conf.HEADERS.pop('Referer')
        return response
    
    def save_role_function(self, param):
        '''
        添加角色功能
        '''
        url = '/role/save-role-function-ajax'
        self.conf.HEADERS_JSON['Referer']= self.conf.URL_TERMINAL+'/role/add?terminal_id='+str(self.conf.TERMINAL_ID)+'&shopType=1'
        response = g.post_requests(self.conf, url, data=param, terminal=True)
        self.conf.HEADERS_JSON.pop('Referer')
        return response
         
    
    def role_delete(self, roleID):
        '''
        删除角色
        '''
        url = '/role/delete-ajax'
        self.conf.HEADERS_JSON['Referer']= self.conf.URL_TERMINAL+'/role/list?terminal_id='+str(self.conf.TERMINAL_ID)+'&shopType=1'
        response = g.post_requests(self.conf,url,id=roleID,terminal=True)
        self.conf.HEADERS_JSON.pop('Referer')
        return response
    
    def role_list(self):
        '''
        角色列表
        '''
        url = '/role/list-ajax'
        self.conf.HEADERS_JSON['Referer']= self.conf.URL_TERMINAL+'/role/list?terminal_id='+str(self.conf.TERMINAL_ID)+'&shopType=1'
        response = g.post_requests(self.conf, url, page=True, terminal=True)
        self.conf.HEADERS_JSON.pop('Referer')
        return response
    
    def staff_add(self, param):
        '''
        添加员工
        '''
        url = '/staff/add-ajax'
        self.conf.HEADERS_JSON['Referer']= self.conf.URL_TERMINAL+'/staff/add?terminal_id='+str(self.conf.TERMINAL_ID)+'&shopType=1'
        response = g.post_requests(self.conf, url, data=param, terminal=True)
        self.conf.HEADERS_JSON.pop('Referer')
        return response
    
    def staff_dell(self, staffID):
        '''
        删除员工
        '''
        url = '/staff/del-ajax'
        self.conf.HEADERS_JSON['Referer']= self.conf.URL_TERMINAL+'/staff/list?terminal_id='+str(self.conf.TERMINAL_ID)+'&shopType=1'
        response = g.post_requests(self.conf,url,id=staffID,terminal=True)
        self.conf.HEADERS_JSON.pop('Referer')
        return response
    
    ############会员列表#########
    def terminal_members_list(self, param):
        '''
        会员列表
        '''
        url = '/members/list-ajax'
        return g.post_requests(self.conf, url, data=param, terminal=True)
    
    def members_last_count(self, param):
        '''
        昨日新增会员数
        '''
        url = '/members/last-count-ajax'
        self.conf.HEADERS_JSON['Referer']= self.conf.URL_TERMINAL+'/members/list?'
        response = g.post_requests(self.conf,url,param,terminal=True)
        self.conf.HEADERS_JSON.pop('Referer')
        return response        
    
    #######客户列表##############
    def terminal_member_list(self, param):
        '''
        客户列表
        '''
        url = '/member/list-ajax'
        return g.post_requests(self.conf, url, data=param, terminal=True)
    
    def terminal_count_wx_member(self, param):
        '''
        计算微信客户数量
        '''
        url = '/member/count-wx-member'
        return g.post_requests(self.conf, url, data=param, terminal=True)
    
    ########核销管理#############
    def cancel_member_list(self):
        '''
        绑定核销员
        '''
        url = '/terminal/cancel-member-list-ajax'
        self.conf.HEADERS_JSON['Referer']= self.conf.URL_TERMINAL+'/terminal/write-off?terminal_id='+str(self.conf.TERMINAL_ID)+'&shopType=false'
        response = g.post_requests(self.conf, url, page=True, terminal=True)
        self.conf.HEADERS_JSON.pop('Referer')
        return response
    
    def cancel_card(self, param):
        '''
        网页核销
        '''
        url = '/card-coupons/cancel-card-ajax'
        self.conf.HEADERS_JSON['Referer']= self.conf.URL_TERMINAL+'/terminal/write-off-web?terminal_id='+str(self.conf.TERMINAL_ID)+'&shopType=false'
        response = g.post_requests(self.conf, url, data=param, terminal=True)
        self.conf.HEADERS_JSON.pop('Referer')
        return response        
        
    def cancel_record_list(self, param):
        '''
        核销记录
        '''
        url = '/terminal/cancel-record-list-ajax'
        self.conf.HEADERS_JSON['Referer']= self.conf.URL_TERMINAL+'/terminal/write-off-records?terminal_id='+str(self.conf.TERMINAL_ID)+'&shopType=false'
        response = g.post_requests(self.conf, url, data=param, terminal=True)
        self.conf.HEADERS_JSON.pop('Referer')
        return response
    
    def shopsub_cancel_list(self, param):
        '''
        核销门店排行榜
        '''
        url = '/terminal/shopsub-cancel-list-ajax'
        self.conf.HEADERS_JSON['Referer']= self.conf.URL_TERMINAL+'/terminal/write-off-shop?terminal_id='+str(self.conf.TERMINAL_ID)+'&shopType=false'
        response = g.post_requests(self.conf, url, data=param, terminal=True)
        self.conf.HEADERS_JSON.pop('Referer')
        return response         
    
    def staff_cancel_list(self,param):
        '''
        核销员排行榜
        '''
        url = '/terminal/staff-cancel-list-ajax'
        self.conf.HEADERS_JSON['Referer']= self.conf.URL_TERMINAL+'/terminal/write-off-staff?terminal_id='+str(self.conf.TERMINAL_ID)+'&shopType=false'
        response = g.post_requests(self.conf, url, data=param, terminal=True)
        self.conf.HEADERS_JSON.pop('Referer')
        return response     
    
    ############推广管理###############
    def fx_member_list(self, param):
        '''
        推广员列表
        '''
        url = '/fx/member-list-ajax'
        self.conf.HEADERS_JSON['Referer']= self.conf.URL_TERMINAL+'/fx/member-list?terminal_id='+str(self.conf.TERMINAL_ID)+'&shopType=1'
        response = g.post_requests(self.conf, url, data=param, terminal=True)
        self.conf.HEADERS_JSON.pop('Referer')
        return response    
    
    def fx_order_list(self, param):
        '''
        推广订单
        '''
        url = '/fx/order-list-ajax'
        self.conf.HEADERS_JSON['Referer']= self.conf.URL_TERMINAL+'/fx/order-list?terminal_id='+str(self.conf.TERMINAL_ID)+'&shopType=1'
        response = g.post_requests(self.conf, url, data=param, terminal=True)
        self.conf.HEADERS_JSON.pop('Referer')
        return response               
    
    #########所有订单###########
    def order_list(self, param):
        '''
        所有订单
        '''
        url = '/order/list-ajax'
        return g.post_requests(self.conf, url, data=param, terminal=True)
    
    ########售后订单#############
    def refund_list(self, param):
        '''
        售后订单
        '''
        url = '/order/refund-list-ajax'
        return g.post_requests(self.conf, url, data=param, terminal=True)