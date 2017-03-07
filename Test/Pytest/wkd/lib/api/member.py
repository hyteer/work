# coding: utf-8
import requests
import json
import pytest
from .generic import Generic as g

class Member(object):
    '''
    会员模块相关接口
    '''
    def __init__(self,conf):
        self.conf = conf

    def member_list(self):
        '''
        客户列表
        '''
        url = "/member/list-ajax"
        return g.post_requests(self.conf,url,page=True)

    def member_detail(self,id):
        '''
        客户详情
        '''
        url = "/member/member-detail-ajax"
        return g.post_requests(self.conf,url,id=id)

    def members_list(self):
        '''
        会员列表
        '''
        url = "/members/list-ajax"
        return g.post_requests(self.conf,url,page=True)

    def members_detail(self,id):
        '''
        会员详情
        '''
        url = "/members/detail-ajax"
        return g.post_requests(self.conf,url,id=id)

    def member_group_list(self):
        '''
        客户分组列表
        '''
        url = "/member/group-list-ajax"
        return g.post_requests(self.conf,url,page=True)

    def member_group_add(self,data):
        '''
        客户分组列表
        '''
        url = "/member/group-add-ajax"
        return g.post_requests(self.conf,url,data=data)

    def member_group_del(self,id):
        '''
        删除客户分组
        注：该接口暂无效，待确认
        '''
        url = "/member/group-del-ajax"
        return g.post_requests(self.conf,url,id=id)

    def member_last_count(self):
        '''
        会员统计
        '''
        url = "/members/last-count-ajax"
        return g.post_requests(self.conf,url,page=True)

    def member_point_list(self):
        '''
        会员积分列表
        '''
        url = "/member/point-list-ajax"
        return g.post_requests(self.conf,url,page=True)

    def members_order_list(self,id):
        '''
        客户消费记录
        '''
        url = "/members/find-member-order-list-ajax"
        data = {"_page":1,"_page_size":20,"uid":id}
        return g.post_requests(self.conf,url,data=data)

############################# 会员管理 ###############################
    def member_card_statisticst(self):
        '''
        会员卡投放统计
        '''
        url = "/members/member-card-statistics-ajax"
        return g.post_requests(self.conf,url,page=True)

    def members_offline(self):
        '''
        实体店会员统计
        '''
        url = "/members/offline-ajax"
        data = {"_page":1,"_page_size":20}
        return g.post_requests(self.conf,url,data=data)

    def members_add_import(self,data):
        '''
        实体店会员统计
        '''
        url = "/members/add-import-ajax"
        return g.post_requests(self.conf,url,data=data)

############################# 标签管理 ###############################
    def members_add_tag_ajax(self,data):
        '''
        标签管理
        '''
        url = "/members/add-tag-ajax"
        return g.post_requests(self.conf,url,data=data)

    def members_find_tag_ajax(self):
        '''
        标签列表
        '''
        url = "/members/find-tag-ajax"
        data = {"_page_size":15,"_page":1}
        return g.post_requests(self.conf,url,data=data)



############################# 会员卡 ###############################
    def get_grade_ajax(self,points):
        '''
        获取等级信息
        '''
        url = "/members/get-grade-ajax"
        data = {"growth": points}
        return g.post_requests(self.conf,url,data=data)


############################# 会员营销 ###############################
    def edit_shop_member_setting(self,data):
        '''
        会员折扣优惠共享设置
        '''
        url = "/members/edit-shop-member-setting-ajax"
        return g.post_requests(self.conf,url,data=data)

    def discounted_product_settings(self,data):
        '''
        会员折扣优惠共享设置
        '''
        url = "/members/discounted-product-settings-ajax"
        return g.post_requests(self.conf,url,data=data)



####
