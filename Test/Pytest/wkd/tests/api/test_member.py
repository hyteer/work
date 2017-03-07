# coding: utf-8
"""
会员API测试用例
"""
import pytest,time,os

run_flag = True
debug_level = None


class TestMemberMain:

    AUTHOR = 'YT'
    COVERAGE = 50
    dt = {}
    TEST_USER_ID = 13764904

    @pytest.fixture(autouse=True)
    def setup(self,conf):
        self.conf = conf
        self.mb = conf.api.Member(conf)
        self.MB_PARAM = conf.param.Member(conf)

    @pytest.mark.skipif(run_flag,reason="跳过该用例")
    def test_member_list(self):
        '''
        客户列表
        '''
        mytest = "sksksk"
        print("Flag:",run_flag)
        print("DebugLevel:",debug_level)
        r = self.mb.member_list()

    @pytest.mark.no_cycle
    def test_member_group_add(self):
        data = self.MB_PARAM.member_group_add()
        print("args:",data)
        r = self.mb.member_group_add(data)
        self.dt['group_id'] = r['errmsg']['id']

    #@pytest.mark.not_ready
    @pytest.mark.debug
    def test_member_detail(self):
        r = self.mb.member_detail(self.TEST_USER_ID)

    @pytest.mark.not_ready
    def test_members_order_list(self):
        r = self.mb.members_order_list(self.TEST_USER_ID)

    def test_members_list(self):
        r = self.mb.members_list()

    def test_members_detail(self):
        r = self.mb.members_detail(self.conf.MEMBER_ID)

    def test_member_group_list(self):
        r = self.mb.member_group_list()

    def test_member_last_count(self):
        '''
        会员统计
        '''
        r = self.mb.member_last_count()

    def test_member_point_list(self):
        '''
        会员积分列表
        '''
        r = self.mb.member_point_list()

    def test_members_offline(self):
        '''
        实体店会员
        '''
        r = self.mb.members_offline()

    def test_members_add_import(self):
        '''
        添加实体店会员
        '''
        payload = self.MB_PARAM.members_add_import()
        r = self.mb.members_add_import(data=payload)


class TestTags:

    dt = {}

    @pytest.fixture(autouse=True)
    def setup(self,conf):
        self.conf = conf
        self.mb = conf.api.Member(conf)
        self.MB_PARAM = conf.param.Member(conf)

    def test_members_find_tag_ajax(self):
        r = self.mb.members_find_tag_ajax()


class TestMemberMarketing:
    '''
    会员营销
    '''

    dt = {}
    AUTHOR = 'BW'

    @pytest.fixture(autouse=True)
    def setup(self,conf):
        self.conf = conf
        self.mb = conf.api.Member(conf)
        self.MB_PARAM = conf.param.Member(conf)

    def teardown_method(self, test_method):
        print("\nAll tests finished, begin to teardown...")
        conf = self.conf
        def tear_shop_member_setting():
            data = self.MB_PARAM.edit_shop_member_setting(is_member_discount=1)
            self.mb.edit_shop_member_setting(data)
        tear_shop_member_setting()


    def test_edit_shop_member_setting(self):
        #折扣优惠共享设置
        data = self.MB_PARAM.edit_shop_member_setting(is_member_discount=2)
        r = self.mb.edit_shop_member_setting(data)

    def test_discounted_product_settings(self):
        #折扣商品设置
        data = self.MB_PARAM.discounted_product_settings(member_discounted_product_type=1,sku=[1171813])
        r = self.mb.discounted_product_settings(data)
        time.sleep(2)
        data = self.MB_PARAM.discounted_product_settings(member_discounted_product_type=1,sku_del=[1171813])
        r = self.mb.discounted_product_settings(data)








####
