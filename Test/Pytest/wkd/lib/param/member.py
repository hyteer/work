# coding: utf-8
'''
会员API参数化配置
'''
from .utils import Utils
import time
from .generic import Generic as g
import random


class Member(object):

    def __init__(self,conf):
        self.conf = conf
        self.Utils = conf.Utils

    @staticmethod
    def member_group_add(**kwargs):
        '''
        添加客户分组常用参数表

        =============     ===========    ============     ===================================
         字段              类型              默认               描述
        =============     ===========    ============     ===================================
         group_name        中文字符        随机             分组名称
         sort              int             随机(0-4)        排序
        =============     ===========    ============     ===================================

        '''
        group_name = "测试" + Utils.rand_cn_str()
        sort = random.randrange(0,4)
        template = {"group_name":group_name,"sort":sort}
        return g.get_params(template,kwargs)

    @staticmethod
    def card_coupons_add(title='default'):
        if title == 'default':
            title = "测试卡" + Utils.rand_str()
        data = {"brand_name":"微客联盟","title":title,"logo_url":"http://imgcache.vikduo.com/static/44ae6a2fae8d1ae7acddc0129dabb128.png","color":"#55bd47","date_info_type":1,"begin":1483977600,"end":1581436799,"quantity":"999","get_limit":"200","can_give_friend":1,"code_type":"3","notice":"请出示卡券二维码","description":"使用说明。。。","service_phone":"13344556677","card_type":1,"assign":-1,"wx_card_type":2,"card_money":0,"money_limit":0,"card_discount":"8.8","exchange_content_text":"","product_ids":"","deal_detail":"8.8折折扣券1张，全场通用"}
        return data

    @staticmethod
    def reduction_add(name='default'):
        if name == 'default':
            name = "满减" + Utils.rand_str()
        data = {"name":name,"is_relate_all":1,"start_time":1484115936,"end_time":1579587938,"conditions":[{"condition_type":1,"level":1,"condition_min":90000,"strategys":[{"reduction_type":1,"amount":20000,"discount":"","point":"","card_type_id":"","red_packet_id":"","is_all_area":1,"area_id":"","area_cn":"","is_limit":2},{"reduction_type":3,"amount":"","discount":"","point":"20","card_type_id":"","red_packet_id":"","is_all_area":1,"area_id":"","area_cn":"","is_limit":2}]}],"products":[]}
        return data

    @staticmethod
    def cash_redpack_add(name='default'):
        if name == 'default':
            name = "红包" + Utils.rand_str()
        data = {"type":1,"act_name":name,"send_name":"微客联盟","wishing":"恭喜发财！大吉大利！","remark":"一个测试红包","min_value":100,"max_value":100,"quantity":"50","deleted":2,"can_share":1}
        return data

    @staticmethod
    def activity_points_add(name='default'):
        if name == 'default':
            name = "积分赠送" + Utils.rand_str()
        data = {"activity":{"name":name,"expire_type":2,"start_time":0,"end_time":0},"pointsConsumption":{"type":2,"amount":1000,"points":"1","count_type":"2","together_buy_flag":2,"seckill_flag":2,"scan_flag":1,"normal_flag":1}}
        return data

    @staticmethod
    def members_add_import(**kwargs):
        '''
        添加实体店会员

        =============     ===========    ============     ===================================
         字段              类型              默认               描述
        =============     ===========    ============     ===================================
         group_name        中文字符        随机             分组名称
         sort              int             随机(0-4)        排序
        =============     ===========    ============     ===================================

        '''
        #rand_name = "姓名" + Utils.rand_cn_str(2)
        rand_phone = Utils.rand_mobile()
        rand_name = Utils.rand_name()
        growth = Utils.rand_num(1,['2','3','4']) + Utils.rand_num(2)
        template = {"real_name":rand_name,"bind_mobile":rand_phone,"growth":growth,"point":"300","sex":1,"birth":1487721600,"province":"1","city":"2","address":"北京东城区"}
        return g.get_params(template,kwargs)

    ############################### 会员营销 ################################
    @staticmethod
    def edit_shop_member_setting(**kwargs):
        '''
        会员折扣优惠共享设置参数

        ===========================     ===========    =============     ===================================
         字段                              类型           默认               描述
        ===========================     ===========    =============     ===================================
         is_member_discount                int             1               会员折扣开关(1开启，2关闭)
         is_discount                       int             1               商城红包共享(1开启，2关闭)
         is_card                           int             1               卡券共享(1开启，2关闭)
         is_point                          int             1               积分共享(1开启，2关闭)
        ===========================     ===========    =============     ===================================

        '''
        template = {"is_member_discount":1,"is_discount":1,"is_card":1,"is_point":1,"statistics_offset":None}
        return g.get_params(template,kwargs)

    @staticmethod
    def discounted_product_settings(**kwargs):
        '''
        折扣商品设置参数

        =================================     ===========    =============     ===================================
         字段                                   类型           默认               描述
        =================================     ===========    =============     ===================================
         member_discounted_product_type        int             2                折扣类型(1全场商品，2指定商品)
         sku                                   long           1171784           包含/排除的商品
         sku_del                               long                             需要删除的包含/排除的商品
        =================================     ===========    =============     ===================================

        '''
        template = {"member_discounted_product_type":2,"sku":[1171784],"sku_del":[]}
        return g.get_params(template,kwargs)




