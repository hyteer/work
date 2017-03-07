# coding: utf-8
import requests
import json
from .generic import Generic as g


class Market(object):
    '''
    市场营销模块
    '''
    def __init__(self,conf):
        self.conf = conf

############################# 添加推广活动 ############################
    def market_activity_add(self,data):
            '''
            添加推广活动（注：砸金蛋、大转盘、众筹等推广活动添加为同一接口）
            '''
            url = "/market-activity/add-ajax"
            return g.post_requests(self.conf,url,data,header='form')


############################# 拼团活动 ###############################
    def together_buy_list(self):
        '''
        拼团活动列表
        '''
        url = "/together-buy/list-ajax"
        return g.post_requests(self.conf,url)

    def togetherBuy_add(self,data):
        '''
        添加拼团活动
        '''
        url = "/together-buy/add-ajax"
        return g.post_requests(self.conf, url, data)
    
    def togetherBuy_goods_add(self, data):
        '''
        添加拼团活动商品
        '''
        url = "/together-buy/together-buy-goods-add-ajax"
        return g.post_requests(self.conf, url, data)
    
    def togetherBuy_edit(self,data):
        '''
        拼团活动编辑
        '''
        url = "/together-buy/edit-ajax"
        return g.post_requests(self.conf, url, data)

    
############################# 卡券活动 ###############################
    def card_coupons_list(self):
        '''
        获取卡券列表
        '''
        url = "/card-coupons/list-ajax"
        return g.post_requests(self.conf,url)

    def card_coupons_add(self,data):
        '''
        添加卡券
        '''
        url = "/card-coupons/add-ajax"
        return g.post_requests(self.conf,url,data)

    def card_coupons_receive_add(self,data):
        '''
        直接领取卡券
        '''
        url = "/card-coupons/receive-add-ajax"
        return g.post_requests(self.conf,url,data)

    def card_coupons_policy_add(self,data):
        '''
        赠送策略
        '''
        url = "/card-coupons/policy-add-ajax"
        return g.post_requests(self.conf,url,data)


    def card_coupons_send(self,data):
        '''
        派发卡券
        '''
        url = "/card-coupons/sends-ajax"
        return g.post_requests(self.conf,url,data)


    def card_coupons_del(self,id):
        '''
        删除卡券
        '''
        url = "/card-coupons/del-ajax"
        return g.post_requests(self.conf,url,id=id)

############################# 满减活动 ###############################
    def reduction_list(self):
        '''
        满减活动列表
        '''
        url = "/reduction/list-ajax"
        return g.post_requests(self.conf,url)

    def reduction_add(self,data):
        '''
        添加满减活动
        '''
        url = "/reduction/add-ajax"
        return g.post_requests(self.conf,url,data)

    def reduction_open(self,id):
        '''
        开启满减活动
        '''
        url = "/reduction/open-ajax"
        return g.post_requests(self.conf,url,id=id)

    def reduction_close(self,id):
        '''
        关闭满减活动
        '''
        url = "/reduction/close-ajax"
        return g.post_requests(self.conf,url,id=id)

    def reduction_del(self,id):
        '''
        删除满减活动
        '''
        url = "/reduction/delete-ajax"
        return g.post_requests(self.conf,url,id=id)

############################# 现金红包 ###############################
    def cash_redpack_list(self):
        '''
        现金红包列表
        '''
        url = "/cash-redpack/list-ajax"
        return g.post_requests(self.conf,url,page=True)

    def cash_redpack_add(self,data):
        '''
        添加现金红包
        '''
        url = "/cash-redpack/add-ajax"
        return g.post_requests(self.conf,url,data)

    def cash_redpack_open(self,id):
        '''
        开启现金红包
        '''
        url = "/cash-redpack/open-ajax"
        return g.post_requests(self.conf,url,id=id)

    def cash_redpack_close(self,id):
        '''
        关闭现金红包
        '''
        url = "/cash-redpack/close-ajax"
        return g.post_requests(self.conf,url,id=id)

    def cash_redpack_del(self,id):
        '''
        删除现金红包
        '''
        url = "/cash-redpack/del-ajax"
        return g.post_requests(self.conf,url,id=id)

############################# 商城红包 ###############################
    def redpack_manage_list(self):
        '''
        商城红包列表
        '''
        url = "/redpack-manage/list-ajax"
        return g.post_requests(self.conf,url,page=True)

    def redpack_manage_add(self,data):
        '''
        添加商城红包
        '''
        url = "/redpack-manage/add-ajax"
        return g.post_requests(self.conf,url,data)

    def redpack_manage_del(self,id):
        '''
        删除商城红包
        '''
        url = "/cash-redpack/del-ajax"
        return g.post_requests(self.conf,url,id=id)

    def redpack_list(self):
        '''
        商城红包活动列表
        '''
        url = "/redpack/list-ajax"
        return g.post_requests(self.conf,url,page=True)

    def redpack_add(self,data):
        '''
        添加商城红包活动
        '''
        url = "/redpack/add-ajax"
        return g.post_requests(self.conf,url,data)

    def redpack_open(self,id):
        '''
        开启商城红包活动
        '''
        url = "/redpack/open-ajax"
        return g.post_requests(self.conf,url,id=id)

    def redpack_close(self,id):
        '''
        关闭商城红包活动
        '''
        url = "/redpack/close-ajax"
        return g.post_requests(self.conf,url,id=id)

    def redpack_del(self,id):
        '''
        删除商城红包活动
        '''
        url = "/redpack/del-ajax"
        return g.post_requests(self.conf,url,id=id)


############################# 积分活动 ###############################
    def activity_points_list(self):
        '''
        积分活动列表
        '''
        url = "/activity-points/list-ajax"
        return g.post_requests(self.conf,url,page=True)

    def activity_points_add(self,data):
        '''
        添加积分活动
        '''
        url = "/activity-points/add-ajax"
        return g.post_requests(self.conf,url,data)

    def activity_points_open(self,id):
        '''
        开启积分活动
        '''
        url = "/activity-points/open-ajax"
        return g.post_requests(self.conf,url,id=id)

    def activity_points_close(self,id):
        '''
        关闭积分活动
        '''
        url = "/activity-points/close-ajax"
        return g.post_requests(self.conf,url,id=id)

    def activity_points_del(self,id):
        '''
        删除积分活动
        '''
        url = "/activity-points/del-ajax"
        return g.post_requests(self.conf,url,id=id)

############################# 砸金蛋活动 ###############################
    def smashegg_list(self):
        '''
        砸金蛋活动列表
        '''
        url = "/market-activity/smashegg-list-ajax"
        return g.post_requests(self.conf,url,page=True)

    def smashegg_open(self,id):
        '''
        砸金蛋开启积分活动
        '''
        url = "/market-activity/open-smashegg-ajax"
        return g.post_requests(self.conf,url,id=id)

    def smashegg_close(self,id):
        '''
        砸金蛋闭关积分活动
        '''
        url = "/market-activity/close-smashegg-ajax"
        return g.post_requests(self.conf,url,id=id)

    def smashegg_del(self,id):
        '''
        砸金蛋删除积分活动
        '''
        url = "/market-activity/del-smashegg-ajax"
        return g.post_requests(self.conf,url,id=id)

############################# 秒杀活动 ###############################
    def second_kill_list(self):
        '''
        秒杀活动列表
        '''
        url = "/second-kill/list-ajax"
        return g.post_requests(self.conf,url,page=True)

    def second_kill_add(self,data):
        '''
        添加秒杀活动
        '''
        url = "/second-kill/add-ajax"
        return g.post_requests(self.conf,url,data)

    def second_kill_goods_add(self,data):
        '''
        添加秒杀活动商品
        '''
        url = "/second-kill/seckill-goods-add-ajax"
        return g.post_requests(self.conf,url,data)

    def second_kill_edit(self,data):
        '''
        编辑秒杀活动
        '''
        url = "/second-kill/edit-ajax"
        return g.post_requests(self.conf,url,data)

    def second_kill_open(self,id):
        '''
        开启秒杀活动
        '''
        url = "/second-kill/open-ajax"
        return g.post_requests(self.conf,url,id=id)

    def second_kill_close(self,id):
        '''
        关闭秒杀活动
        '''
        url = "/second-kill/close-ajax"
        return g.post_requests(self.conf,url,id=id)

    def second_kill_del(self,id):
        '''
        删除秒杀活动
        '''
        url = "/second-kill/del-ajax"
        return g.post_requests(self.conf,url,id=id)

############################# 众筹活动 ###############################
    def collect_zan_list(self):
        '''
        众筹活动列表
        '''
        url = "/collect-zan/list-ajax"
        return g.post_requests(self.conf,url)

    def collect_zan_add(self,data):
        '''
        众筹活动添加
        '''
        url = "/collect-zan/add-ajax"
        return g.post_requests(self.conf,url,data)

    def collect_zan_edit(self,data):
        '''
        众筹活动编辑
        '''
        url = "/collect-zan/edit-ajax"
        return g.post_requests(self.conf,url,data,header='xfrom')

    def collect_zan_gift_add(self,data):
        '''
        众筹活动商品的添加
        '''
        url = "/collect-zan/add-custom-gift-ajax"
        return g.post_requests(self.conf,url,data)


    def collect_zan_open(self,id):
        '''
        开启众筹活动
        '''
        url = "/collect-zan/open-ajax"
        return g.post_requests(self.conf,url,id=id)

    def collect_zan_close(self,id):
        '''
        关闭众筹活动
        '''
        url = "/collect-zan/close-ajax"
        return g.post_requests(self.conf,url,id=id)

    def collect_zan_del(self,id):
        '''
        删除众筹活动
        '''
        url = "/collect-zan/del-ajax"
        return g.post_requests(self.conf,url,id=id)


#######################大转盘活动##################################
    def slyder_list(self):
        '''
        大转盘活动列表
        '''
        url = "/market-activity/list-ajax"
        return g.post_requests(self.conf,url,page=True)


    def slyder_open(self,id):
        '''
        大转盘开启积分活动
        '''
        url = "/market-activity/open-ajax"
        return g.post_requests(self.conf,url,id=id)

    def slyder_close(self,id):
        '''
        大转盘闭关积分活动
        '''
        url = "/market-activity/close-ajax"
        return g.post_requests(self.conf,url,id=id)

    def slyder_del(self,id):
        '''
        大转盘删除积分活动
        '''
        url = "/market-activity/del-ajax"
        return g.post_requests(self.conf,url,id=id)

#######################预约活动##################################
    def reserve_list(self):
        '''
        预约活动活动列表
        '''
        url = "/reserve/list-ajax"
        return g.post_requests(self.conf,url,page=True)

    def reserve_add(self,data):
        '''
        预约活动活动添加
        '''
        url = "/reserve/add-ajax"
        return g.post_requests(self.conf,url,data,header='xfrom')


    def reserve_open(self,id):
        '''
        预约活动开启活动
        '''
        url = "/reserve/open-ajax"
        return g.post_requests(self.conf,url,id=id)

    def reserve_close(self,id):
        '''
        预约活动闭关活动
        '''
        url = "/reserve/close-ajax"
        return g.post_requests(self.conf,url,id=id)

    def reserve_del(self,id):
        '''
        预约活动删除活动
        '''
        url = "/reserve/del-ajax"
        return g.post_requests(self.conf,url,id=id)



#######################记忆翻翻看活动##################################
    def memory_fan_list(self):
        '''
        记忆翻翻看活动列表
        '''
        url = "/memory-fan/list-ajax"
        return g.post_requests(self.conf,url,page=True)

    def memory_fan_add(self,data):
        '''
        记忆翻翻看活动添加
        '''
        url = "/memory-fan/add-ajax"
        return g.post_requests(self.conf,url,data,header='xfrom')


    def memory_fan_open(self,id):
        '''
        记忆翻翻看开启活动
        '''
        url = "/memory-fan/open-ajax"
        return g.post_requests(self.conf,url,id=id)

    def memory_fan_close(self,id):
        '''
        记忆翻翻看闭关活动
        '''
        url = "/memory-fan/close-ajax"
        return g.post_requests(self.conf,url,id=id)

    def memory_fan_del(self,id):
        '''
        记忆翻翻看删除活动
        '''
        url = "/memory-fan/del-ajax"
        return g.post_requests(self.conf,url,id=id)

#######################签到活动##################################
    def signin_setting_list(self):
        '''
        签到活动活动列表
        '''
        url = "/signin-setting/list-ajax"
        return g.post_requests(self.conf,url,page=True)

    def signin_setting_add(self,data):
        '''
        签到活动活动添加
        '''
        url = "/signin-setting/add-ajax"
        return g.post_requests(self.conf,url,data,header='xfrom')


    def signin_setting_open(self,id):
        '''
        签到活动开启活动
        '''
        url = "/signin-setting/open-ajax"
        return g.post_requests(self.conf,url,id=id)

    def signin_setting_close(self,id):
        '''
        签到活动关闭活动
        '''
        url = "/signin-setting/close-ajax"
        return g.post_requests(self.conf,url,id=id)

    def signin_setting_del(self,id):
        '''
        签到活动删除活动
        '''
        url = "/signin-setting/del-ajax"
        return g.post_requests(self.conf,url,id=id)

#######################节日礼包##################################
    def giftpack_list(self):
        '''
        节日礼包活动列表
        '''
        url = "/giftpack/list-ajax"
        return g.post_requests(self.conf,url,page=True)

    def giftpack_add(self,data):
        '''
        节日礼包活动添加
        '''
        url = "/giftpack/add-ajax"
        return g.post_requests(self.conf,url,data)


    def giftpack_open(self,id):
        '''
        节日礼包开启活动
        '''
        url = "/giftpack/open-ajax"
        return g.post_requests(self.conf,url,id=id)

    def giftpack_close(self,id):
        '''
        节日礼包关闭活动
        '''
        url = "/giftpack/close-ajax"
        return g.post_requests(self.conf,url,id=id)

    def giftpack_del(self,id):
        '''
        节日礼包删除活动
        '''
        url = "/giftpack/del-ajax"
        return g.post_requests(self.conf,url,id=id)

#######################购物礼包##################################
    def cardpack_list(self):
        '''
        购物礼包活动列表
        '''
        url = "/cardpack/list-ajax"
        return g.post_requests(self.conf,url,page=True)

    def cardpack_add(self,data):
        '''
        购物礼包活动添加
        '''
        url = "/cardpack/add-ajax"
        return g.post_requests(self.conf,url,data)


    def cardpack_open(self,id):
        '''
        购物礼包开启活动
        '''
        url = "/cardpack/open-ajax"
        return g.post_requests(self.conf,url,id=id)

    def cardpack_close(self,id):
        '''
        购物礼包关闭活动
        '''
        url = "/cardpack/close-ajax"
        return g.post_requests(self.conf,url,id=id)

    def cardpack_del(self,id):
        '''
        购物礼包删除活动
        '''
        url = "/cardpack/del-ajax"
        return g.post_requests(self.conf,url,id=id)



