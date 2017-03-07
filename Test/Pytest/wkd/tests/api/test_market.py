# coding: utf-8
"""
API测试
"""
import json,time,datetime
import pytest

TIMER = 0.1

class TestCardCoupons:

    AUTHOR='xz'
    mk = None
    clsdata = {}
    USER_ID = '13764907'

    @pytest.fixture(autouse=True)
    def setup(self,conf):
        self.conf=conf
        self.mk = conf.api.Market(conf)
        self.MK_PARAM = conf.param.Market(conf)

    # Test Cases

    def test_card_coupons_list(self):
        r = self.mk.card_coupons_list()

    def test_card_coupons_add(self):

        data = self.MK_PARAM.card_coupons_add()
        print("args:",data)
        r = self.mk.card_coupons_add(data)
        print("card_id:", r['errmsg']['id'])
        self.clsdata['card_id'] = r['errmsg']['id']


    def test_card_coupons_send(self):
        id = self.clsdata['card_id']
        data = {"user_type":1,"card_type_ids":[id],"to_user_ids":[self.USER_ID],"user_group":[]}
        print("args:",data)
        r = self.mk.card_coupons_send(data)

    def test_card_coupons_del(self,conf):
        self.mk = conf.api.Market(conf)
        self.MK_PARAM = conf.param.Market(conf)
        id = self.clsdata['card_id']
        r = self.mk.card_coupons_del(id)

    def test_card_coupons_receive_add(self):
        data=self.MK_PARAM.card_coupons_receive_add()
        print("args:",data)
        r=self.mk.card_coupons_receive_add(data)

    def test_card_coupons_policy_add(self):
        data = self.MK_PARAM.card_coupons_policy_add()
        print("args:", data)
        r = self.mk.card_coupons_policy_add(data)



class TestReduction:
    '''
    满减活动API测试
    '''

    mk = None
    clsdata = {}
    USER_ID = '13764907'

    @pytest.fixture(autouse=True)
    def setup(self,conf):
        self.mk = conf.api.Market(conf)
        self.MK_PARAM = conf.param.Market(conf)

    # Tests

    def test_reduction_list(self,conf):
        self.mk = conf.api.Market(conf)
        r = self.mk.reduction_list()

    def test_reduction_add(self,conf):
        self.mk = conf.api.Market(conf)
        data = self.MK_PARAM.reduction_add()
        print("Data",data)
        r = self.mk.reduction_add(data)
        self.clsdata['reduction_id'] = r['errmsg']['id']
        print("id:", r['errmsg']['id'])

    def test_reduction_open(self,conf):
        self.mk = conf.api.Market(conf)
        id = self.clsdata['reduction_id']
        r = self.mk.reduction_open(id)

    def test_reduction_close(self,conf):
        self.mk = conf.api.Market(conf)
        id = self.clsdata['reduction_id']
        r = self.mk.reduction_close(id)


    def test_reduction_del(self,conf):
        self.mk = conf.api.Market(conf)
        id = self.clsdata['reduction_id']
        r = self.mk.reduction_del(id)


class TestCashRedpack:
    '''
    现金红包API测试
    '''
    mk = None
    clsdata = {}

    @pytest.fixture(autouse=True)
    def setup(self,conf):
        self.mk = conf.api.Market(conf)
        self.MK_PARAM = conf.param.Market(conf)


    def test_cash_redpack_list(self,conf):
        self.mk = conf.api.Market(conf)
        r = self.mk.cash_redpack_list()
        print("resp:", r)

    def test_cash_redpack_add(self,conf):
        data = self.MK_PARAM.cash_redpack_add()
        self.mk = conf.api.Market(conf)
        r = self.mk.cash_redpack_add(data)
        self.clsdata['cash_redpack_id'] = r['errmsg']['id']
        time.sleep(1)

    def test_cash_redpack_open(self,conf):
        self.mk = conf.api.Market(conf)
        id = self.clsdata['cash_redpack_id']
        r = self.mk.cash_redpack_open(id)
        time.sleep(1)

    def test_cash_redpack_close(self,conf):
        self.mk = conf.api.Market(conf)
        id = self.clsdata['cash_redpack_id']
        r = self.mk.cash_redpack_close(id)

    def test_cash_redpack_del(self,conf):
        self.mk = conf.api.Market(conf)
        id = self.clsdata['cash_redpack_id']
        r = self.mk.cash_redpack_del(id)


class TestRedpack:
    '''
    商城红包活动API测试
    '''
    dt = {}

    @pytest.fixture(autouse=True)
    def setup(self,conf):
        self.mk = conf.api.Market(conf)
        self.MK_PARAM = conf.param.Market(conf)

    def test_redpack_list(self,conf):
        self.mk = conf.api.Market(conf)
        r = self.mk.redpack_list()

    def test_redpack_add(self,conf):
        self.mk = conf.api.Market(conf)
        data = self.MK_PARAM.redpack_add()
        print("data:",data)
        r = self.mk.redpack_add(data)
        self.dt['id'] = r['errmsg']['activity']['id']
        time.sleep(1)

    def test_redpack_open(self,conf):
        self.mk = conf.api.Market(conf)
        id = self.dt['id']
        r = self.mk.redpack_open(id)
        time.sleep(1)

    def test_redpack_close(self,conf):
        self.mk = conf.api.Market(conf)
        id = self.dt['id']
        r = self.mk.redpack_close(id)
        time.sleep(1)

    def test_redpack_del(self,conf):
        self.mk = conf.api.Market(conf)
        id = self.dt['id']
        r = self.mk.redpack_del(id)
        time.sleep(1)


class TestActivityPoints:
    '''
    积分活动API测试
    '''
    mk = None
    clsdata = {}

    @pytest.fixture(autouse=True)
    def setup(self,conf):

        if TestActivityPoints.mk == None:
            self.mk = conf.api.Market(conf)
            self.MK_PARAM = conf.param.Market(conf)
            print("\nSetup....")

    def test_activity_points_list(self):
        r = self.mk.activity_points_list()

    def test_activity_points_add(self):
        data = self.MK_PARAM.activity_points_add()
        r = self.mk.activity_points_add(data)
        self.clsdata['activity_points_id'] = r['errmsg']['activity']['id']
        time.sleep(TIMER)

    def test_activity_points_open(self):
        id = self.clsdata['activity_points_id']
        r = self.mk.activity_points_open(id)
        time.sleep(TIMER)

    def test_activity_points_close(self):
        id = self.clsdata['activity_points_id']
        r = self.mk.activity_points_close(id)
        time.sleep(TIMER)

    def test_activity_points_del(self):
        id = self.clsdata['activity_points_id']
        r = self.mk.activity_points_del(id)


class TestSmashegg:
    '''
    砸金蛋活动API测试
    '''
    dt = {}

    @pytest.fixture(autouse=True)
    def setup(self,conf):
        self.mk = conf.api.Market(conf)
        self.MK_PARAM = conf.param.Market(conf)

    def test_smashegg_list(self):
        r = self.mk.smashegg_list()

    def test_smashegg_add(self):

        data = self.MK_PARAM.smashegg_add(try_limit=3)
        print("data:",data)
        r = self.mk.market_activity_add(data)
        self.dt['id'] = r['errmsg']['marketingActivity']['id']
        time.sleep(1)

    def test_smashegg_open(self):

        id = self.dt['id']
        r = self.mk.smashegg_open(id)
        time.sleep(TIMER)

    def test_smashegg_close(self):

        id = self.dt['id']
        r = self.mk.smashegg_close(id)
        time.sleep(1)

    def test_smashegg_del(self):

        id = self.dt['id']
        r = self.mk.smashegg_del(id)
        time.sleep(1)
        
class TestTogetherBuy:
    '''
    拼团活动测试
    '''
    togetherBuyName = ''
    togetherBuyStatus = ''
    dt = {}
    
    @pytest.fixture(autouse=True)
    def setUp(self, conf):
        self.mk = conf.api.Market(conf)
        self.MK_PARAM = conf.param.Market(conf)
        
    def test_togetherBuy_add(self):


        payload = self.MK_PARAM.togetherBuy_add()
        r = self.mk.togetherBuy_add(payload)
        
        activityID = r['errmsg']['0']["togetherBuy"]["activity_id"]
        togetherBuyID = r['errmsg']['0']["togetherBuy"]["id"]
        assert activityID != 0
        assert togetherBuyID != 0
        self.dt['activityID'] = r['errmsg']['0']["togetherBuy"]["activity_id"]
        self.dt['togetherBuyID'] = r['errmsg']['0']["togetherBuy"]["id"]

    def test_togetherBuy_goods_add(self):

        data = self.MK_PARAM.togetherBuy_goods_add(self.dt['togetherBuyID'])
        r = self.mk.togetherBuy_goods_add(data)

    def test_togetherBuy_edit(self):

        id = self.dt['activityID']
        data = self.MK_PARAM.togetherBuy_edit(id)
        print("data:",data)
        r = self.mk.togetherBuy_edit(data)
        time.sleep(1)
        


class TestSecondKill:
    '''
    秒杀活动API测试
    '''
    dt = {}

    @pytest.fixture(autouse=True)
    def setup(self,conf):
        self.mk = conf.api.Market(conf)
        self.MK_PARAM = conf.param.Market(conf)


    def test_second_kill_list(self,conf):
        self.mk = conf.api.Market(conf)
        r=self.mk.second_kill_list()


    def test_second_kill_add(self):
        data = self.MK_PARAM.second_kill_add()
        #data = conf.Param.market.second_kill_add()
        print("data:",data)
        r = self.mk.second_kill_add(data)
        self.dt['id'] = r['errmsg']['id']
        time.sleep(1)

    def test_second_kill_goods_add(self):
        data = self.MK_PARAM.second_kill_goods_add(self.dt['id'])
        r = self.mk.second_kill_goods_add(data)
        time.sleep(1)

    def test_second_kill_edit(self):

        id = self.dt['id']
        data = self.MK_PARAM.second_kill_edit(id)
        print("data:",data)
        r = self.mk.second_kill_edit(data)
        time.sleep(1)

    def test_second_kill_open(self):

        id = self.dt['id']
        r = self.mk.second_kill_open(id)
        time.sleep(1)

    def test_second_kill_close(self):

        id = self.dt['id']
        r = self.mk.second_kill_close(id)
        time.sleep(1)

    def test_second_kill_del(self):

        id = self.dt['id']
        r = self.mk.second_kill_del(id)



class TestSlyder:
    '''
    大转盘活动API测试
    '''
    dt={}
    @pytest.fixture(autouse=True)
    def setup(self,conf):
        self.mk = conf.api.Market(conf)
        self.MK_PARAM = conf.param.Market(conf)

    def test_slyder_list(self,conf):
        self.mk = conf.api.Market(conf)
        r = self.mk.slyder_list()


    def test_slyder_add(self,conf):
        self.mk = conf.api.Market(conf)
        #data = conf.Param.market.slyder_add(try_limit=3)
        data = self.MK_PARAM.slyder_add(try_limit=3)
        print("data:",data)
        r = self.mk.market_activity_add(data)

        self.dt['id'] = r['errmsg']['marketingActivity']['id']
        time.sleep(1)

    def test_slyder_open(self,conf):
        self.mk = conf.api.Market(conf)
        id = self.dt['id']
        r = self.mk.slyder_open(id)

        time.sleep(TIMER)

    def test_slyder_close(self,conf):
        self.mk = conf.api.Market(conf)
        id = self.dt['id']
        r = self.mk.slyder_close(id)

        time.sleep(1)

    def test_slyder_del(self,conf):
        self.mk = conf.api.Market(conf)
        id = self.dt['id']
        r = self.mk.slyder_del(id)

        time.sleep(1)



class TestCollectZan:

    '''
    众筹活动API测试
    '''
    dt={}


    @pytest.fixture(autouse=True)
    def setUp(self, conf):
        self.mk = conf.api.Market(conf)
        self.MK_PARAM = conf.param.Market(conf)

    def test_collect_zan_add(self, conf):
        '''
        众筹活动添加
        '''
        self.mk = conf.api.Market(conf)

        payload = self.MK_PARAM.collect_zan_add()
        r = self.mk.collect_zan_add(payload)

        collectId = r['errmsg']['0']["collect"]["id"]
        assert collectId != 0
        self.dt['collectId'] = r['errmsg']['0']["collect"]["id"]

    def test_collect_zan_gift_add(self, conf):
        '''
        众筹活动添加商品
        '''
        self.mk = conf.api.Market(conf)
        data = self.MK_PARAM.collect_zan_gift_add(self.dt['collectId'])
        r = self.mk.collect_zan_gift_add(data)
        print("resp:", r)

    def test_collect_zan_edit(self,conf):
        '''
        众筹活动编辑
        '''
        self.mk = conf.api.Market(conf)
        id = self.dt['collectId']
        data = self.MK_PARAM.collect_zan_edit(id)
        print("data:",data)
        r = self.mk.collect_zan_edit(data)
        print("resp:", r)
        time.sleep(1)

    def test_collect_zan_open(self,conf):
        '''
        打开众筹活动
        '''
        self.mk = conf.api.Market(conf)
        id = self.dt['collectId']
        r = self.mk.collect_zan_open(id)
        print("resp:", r)
        time.sleep(1)

    def test_collect_zan_close(self,conf):
        '''
        关闭众筹活动
        '''
        self.mk = conf.api.Market(conf)
        id = self.dt['collectId']
        r = self.mk.collect_zan_close(id)
        time.sleep(1)

    def test_collect_zan_del(self,conf):
        '''
        删除众筹活动
        '''
        self.mk = conf.api.Market(conf)
        id = self.dt['collectId']
        r = self.mk.collect_zan_del(id)
        time.sleep(1)

class TestMemoryFan:
    '''
    记忆翻翻看活动API测试
    '''

    dt={}
    @pytest.fixture(autouse=True)
    def setup(self,conf):
        self.mk = conf.api.Market(conf)
        self.MK_PARAM = conf.param.Market(conf)

    def test_memory_fan_list(self,conf):
        '''
        记忆翻翻看活动列表
        '''
        self.mk = conf.api.Market(conf)
        r = self.mk.memory_fan_list()

    def test_memory_fan_add(self,conf):
        """
        记忆翻翻看添加活动
        """
        self.mk = conf.api.Market(conf)
        data = self.MK_PARAM.memory_fan_add()
        print("data:",data)
        r = self.mk.memory_fan_add(data)
        self.dt['id'] = r['errmsg']['id']
        time.sleep(1)

    def test_memory_fan_open(self,conf):
        '''
        打开记忆翻翻看活动
        '''
        self.mk = conf.api.Market(conf)
        id = self.dt['id']
        r = self.mk.memory_fan_open(id)
        time.sleep(TIMER)

    def test_memory_fan_close(self,conf):
        '''
        关闭记忆翻翻看活动
        '''
        self.mk = conf.api.Market(conf)
        id = self.dt['id']
        r = self.mk.memory_fan_close(id)
        time.sleep(1)

    def test_memory_fan_del(self,conf):
        '''
        删除记忆翻翻看活动
        '''
        self.mk = conf.api.Market(conf)
        id = self.dt['id']
        r = self.mk.memory_fan_del(id)
        time.sleep(1)

class TestReserve:
    '''
    预约活动API测试
    '''

    dt={}
    @pytest.fixture(autouse=True)
    def setup(self,conf):
        self.mk = conf.api.Market(conf)
        self.MK_PARAM = conf.param.Market(conf)

    def test_reserve_list(self,conf):
        '''
        预约活动列表
        '''
        self.mk = conf.api.Market(conf)
        r = self.mk.reserve_list()

    def test_reserve_add(self,conf):
        """
        预约添加活动
        """
        self.mk = conf.api.Market(conf)
        data = self.MK_PARAM.reserve_add()
        print("data:",data)
        r = self.mk.reserve_add(data)
        self.dt['id'] = r['errmsg']['id']
        time.sleep(1)

    def test_reserve_open(self,conf):
        '''
        打开预约活动
        '''
        self.mk = conf.api.Market(conf)
        id = self.dt['id']
        r = self.mk.reserve_open(id)

        time.sleep(TIMER)

    def test_reserve_close(self,conf):
        '''
        关闭预约活动
        '''
        self.mk = conf.api.Market(conf)
        id = self.dt['id']
        r = self.mk.reserve_close(id)

        time.sleep(1)

    def test_reserve_del(self,conf):
        '''
        删除预约活动
        '''
        id = self.dt['id']
        r = self.mk.reserve_del(id)

        time.sleep(1)

class TestsigninSetting:
    '''
    签到活动API测试
    '''

    dt={}
    @pytest.fixture(autouse=True)
    def setup(self,conf):
        self.mk = conf.api.Market(conf)
        self.MK_PARAM = conf.param.Market(conf)

    def test_signin_setting_list(self,conf):
        '''
        签到活动列表
        '''
        self.mk = conf.api.Market(conf)
        r = self.mk.signin_setting_list()

    def test_signin_setting_add(self,conf):
        """
        签到添加活动
        """
        self.mk = conf.api.Market(conf)
        data = self.MK_PARAM.signin_setting_add()
        print("data:",data)
        r = self.mk.signin_setting_add(data)

        self.dt['id'] = r['errmsg']['id']
        time.sleep(1)

    def test_signin_setting_open(self,conf):
        '''
        打开签到活动
        '''
        self.mk = conf.api.Market(conf)
        id = self.dt['id']
        r = self.mk.signin_setting_open(id)

        time.sleep(TIMER)

    def test_signin_setting_close(self,conf):
        '''
        关闭签到活动
        '''
        self.mk = conf.api.Market(conf)
        id = self.dt['id']
        r = self.mk.signin_setting_close(id)

        time.sleep(1)

    def test_signin_setting_del(self,conf):
        '''
        删除签到活动
        '''
        self.mk = conf.api.Market(conf)
        id = self.dt['id']
        r = self.mk.signin_setting_del(id)

        time.sleep(1)


class TestGiftpack:
    '''
    节日礼包API测试
    '''

    dt={}
    @pytest.fixture(autouse=True)
    def setup(self,conf):
        self.mk = conf.api.Market(conf)
        self.MK_PARAM = conf.param.Market(conf)

    def test_giftpack_list(self,conf):
        '''
        节日礼包列表
        '''
        self.mk = conf.api.Market(conf)
        r = self.mk.giftpack_list()

    def test_giftpack_add(self,conf):
        """
        节日礼包活动添加
        """
        self.mk = conf.api.Market(conf)
        data = self.MK_PARAM.giftpack_add()
        print("data:",data)
        r = self.mk.giftpack_add(data)

        self.dt['id'] = r['errmsg']['id']
        time.sleep(1)

    def test_giftpack_open(self,conf):
        '''
        打开节日礼包
        '''
        self.mk = conf.api.Market(conf)
        id = self.dt['id']
        r = self.mk.giftpack_open(id)

        time.sleep(TIMER)

    def test_giftpack_close(self,conf):
        '''
        关闭节日礼包
        '''
        self.mk = conf.api.Market(conf)
        id = self.dt['id']
        r = self.mk.giftpack_close(id)

        time.sleep(1)

    def test_giftpack_del(self,conf):
        '''
        删除节日礼包
        '''
        self.mk = conf.api.Market(conf)
        id = self.dt['id']
        r = self.mk.giftpack_del(id)

        time.sleep(1)

class TestCardpack:
    '''
    购物礼包API测试
    '''

    dt={}
    @pytest.fixture(autouse=True)
    def setup(self,conf):
        self.mk = conf.api.Market(conf)
        self.MK_PARAM = conf.param.Market(conf)

    def test_cardpack_list(self,conf):
        '''
        购物礼包列表
        '''
        self.mk = conf.api.Market(conf)
        r = self.mk.cardpack_list()

    def test_cardpack_add(self,conf):
        """
        购物礼包活动添加
        """
        self.mk = conf.api.Market(conf)
        data = self.MK_PARAM.cardpack_add()
        print("data:",data)
        r = self.mk.cardpack_add(data)

        self.dt['id'] = r['errmsg']['id']
        time.sleep(1)

    def test_cardpack_open(self,conf):
        '''
        打开购物礼包
        '''
        self.mk = conf.api.Market(conf)
        id = self.dt['id']
        r = self.mk.cardpack_open(id)

        time.sleep(TIMER)

    def test_cardpack_close(self,conf):
        '''
        关闭购物礼包
        '''
        self.mk = conf.api.Market(conf)
        id = self.dt['id']
        r = self.mk.cardpack_close(id)

        time.sleep(1)

    def test_cardpack_del(self,conf):
        '''
        删除购物礼包
        '''
        self.mk = conf.api.Market(conf)
        id = self.dt['id']
        r = self.mk.cardpack_del(id)

        time.sleep(1)














