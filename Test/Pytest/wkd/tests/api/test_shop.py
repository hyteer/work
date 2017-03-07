# coding: utf-8
"""
商品测试
"""

import time
import random
import pytest

class TestShop:
    '''
    店铺接口用例
    '''
    def test_get_shop(self, conf):
        self.pd = conf.api.Shop(conf)
        res = self.pd.get_shop()
        print ("response:",res)

class TestProduct:
    '''
    商品接口相关用例
    '''

    pd = None
    productID = None
    productName = ''
    
    def test_product_add(self,conf):
        self.pd = conf.api.Shop(conf)
        param = conf.param.Shop(conf).product_add()
        print("param:",param)
        TestProduct.productName = param['product']['name']
        respData = self.pd.product_add(param)
        print ("resp:%s" % respData)
        TestProduct.productID = respData['errmsg']['product']['id']

    def test_product_list(self,conf):
        self.pd = conf.api.Shop(conf)
        payload = conf.param.Shop(conf).product_list()
        r = self.pd.product_list(payload)
        print ("resp:", r)

    def test_product_list_search(self,conf):
        self.pd = conf.api.Shop(conf)
        searchKeyWord = TestProduct.productName
        payload = conf.param.Shop(conf).product_list(is_search=True,name=searchKeyWord)
        respData = self.pd.product_list(payload)
        
        totalCount = respData['errmsg']['page']['total_count']
        assert totalCount == 1
        
        assert TestProduct.productID == respData['errmsg']['data'][0]['id']
        
        productName = respData['errmsg']['data'][0]['name']
        assert searchKeyWord in productName

    def test_product_on_sale(self, conf):
        self.pd = conf.api.Shop(conf)
        payload = {"ids":[TestProduct.productID]}
        self.pd.product_on_sale(payload)

    def test_product_off_sale(self, conf):
        self.pd = conf.api.Shop(conf)
        payload = {"ids":[TestProduct.productID]}
        self.pd.product_off_sale(payload)
        
    def test_product_check(self, conf):
        self.pd = conf.api.Shop(conf)
        payload = {"product_id":[TestProduct.productID]}
        self.pd.product_check(payload)
    
    def test_product_del(self, conf):
        self.pd = conf.api.Shop(conf)
        payload = {"ids":[TestProduct.productID]}
        self.pd.product_del(payload)
        
        
class TestCategory(object):
    '''
    商品分类接口测试用例
    '''
    pid1 = None
    pid2 = None
    pid3 = None
        
    def test_category_list(self,conf):
        pd = conf.api.Shop(conf)
        payload = {"_page_size":15,"_page":1}
        respData = pd.category_list(payload)
        
        totalCount = respData['errmsg']['page']['total_count']
        assert totalCount >= 1
    
    def test_category_add(self,conf):
        pd = conf.api.Shop(conf)
        #添加一级分类
        randStr = "".join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5))
        categoryName = randStr + '一级测试分类'
        payload = {"name":categoryName,"desc":"","sort":"1"}
        firstCateResp = pd.category_add(payload)
        TestCategory.pid1 = firstCateResp['errmsg']['id']
        #添加二级分类
        randStr2 = "".join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5))
        categoryName2 = randStr2 + '二级测试分类'
        payload2 = {"name":categoryName2,"desc":"","sort":"1","pid":TestCategory.pid1}
        firstCateResp2 = pd.category_add(payload2)
        TestCategory.pid2 = firstCateResp2['errmsg']['id']
        #添加三级分类
        randStr3 = "".join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5))
        categoryName3 = randStr3 + '二级测试分类'
        payload3 = {"name":categoryName3,"desc":"","sort":"1","pid":TestCategory.pid2}
        firstCateResp2 = pd.category_add(payload3)
        TestCategory.pid3 = firstCateResp2['errmsg']['id']
        
    def test_categor_del(self, conf):
        pd = conf.api.Shop(conf)
        #删除三级分类
        pd.category_del(TestCategory.pid3)
        #删除二级分类
        pd.category_del(TestCategory.pid2)
        #删除一级分类
        pd.category_del(TestCategory.pid1)
        
class TestKind(object):
    '''
    商品规格测试用例
    '''
    kindID = None
    kindName = ''
    
    def test_kind_add(self, conf):
        pd = conf.api.Shop(conf)
        randStr = "".join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5))
        kindName = randStr + u'规格'
        TestKind.kindName = kindName
        kindValueList = []
        for i in range(5):
            tmpStr = "".join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5))
            kindValueList.append(tmpStr)
        payload = {"name":kindName,"kind_value":kindValueList}
        respData = pd.kind_add(payload)
        TestKind.kindID = respData['errmsg']['product_kind_id']
    
    def test_kind_list(self, conf):
        pd = conf.api.Shop(conf)
        respData = pd.kind_list()
        
        kindList = respData['errmsg']['data']
        kindNameList = []
        for kind in kindList:
            kindNameList.append(kind['name'])
        assert TestKind.kindName in kindNameList
        
        
    def test_kind_del(self,conf):
        pd = conf.api.Shop(conf)
        pd.kind_del(TestKind.kindID)
        
class TestProductComment(object):
    '''
    商品评论测试用例
    '''
    productID = None
    commentID = None
    comment = ''   
    
    def test_comment_add(self, conf):
        pd = conf.api.Shop(conf)
        payload = conf.param.Shop(conf).comment_without_user()
        TestProductComment.comment = payload['content']
        TestProductComment.productID = payload['product_id']
        respData = pd.comment_without_user(payload)
        TestProductComment.commentID = respData['errmsg']['id']
        
    def test_comment_list(self, conf):
        pd = conf.api.Shop(conf)
        respData = pd.comment_list()
        count = respData['errmsg']['page']['total_count']
        assert count > 0
        index = None
        dataList = respData['errmsg']['data']
        for i in range(count):
            if dataList[i]['id'] == TestProductComment.commentID:
                index = i
                break
        assert TestProductComment.comment == dataList[index]['content']
        assert TestProductComment.productID == dataList[index]['product_id']
    
    def test_comment_del(self, conf):
        pd = conf.api.Shop(conf)
        payload = {"comment_id": TestProductComment.commentID, "product_id": TestProductComment.productID}
        pd.comment_del(payload)
        
class TestOrder(object):
    '''
    订单接口用例
    '''

    @pytest.fixture(autouse=True)
    def setup(self,conf):
        self.conf = conf
        self.sp = conf.api.Shop(conf)
        self.SP_PARAM = conf.param.Shop(conf)
    
    def test_order_list(self, conf):
        pd = conf.api.Shop(conf)
        payload = conf.param.Shop(conf).order_list()
        respData = pd.order_list(payload)
        
        count = respData['errmsg']['page']['total_count']
        assert count > 0
    
    def test_refund_list(self, conf):
        pd = conf.api.Shop(conf)
        payload = conf.param.Shop(conf).refund_list()
        respData = pd.refund_list(payload)
        count = respData['errmsg']['page']['total_count']
        assert count >= 1

    @pytest.mark.skipif(True,reason="需要依赖条件订单ID")
    def test_order_deliver(self):
        order_id = 997094
        params = self.SP_PARAM.order_deliver(order_id)
        r = self.sp.order_deliver(params)

    @pytest.mark.skipif(True,reason="需要依赖条件订单ID")
    def test_order_cancel(self):
        order_id = 997089
        r = self.sp.order_cancel(order_id)



class TestShopSetting(object):
    '''
    店铺相关设置
    '''
    
    def test_shop_order_auto_settings(self, conf):
        pd = conf.api.Shop(conf)
        upayTime = (random.randint(1,24))*3600
        simpleOrderCloseUpayStatus = 2
        payload = conf.param.Shop(conf).shop_order_auto_settings(simple_order_close_unpay_status=simpleOrderCloseUpayStatus,simple_order_close_unpay_time=upayTime)
        respData = pd.shop_order_auto_settings(payload)
        orderUnpayStatus = respData['errmsg']['simple_order_close_unpay_status']
        assert orderUnpayStatus == simpleOrderCloseUpayStatus
        orderUpayTime = respData['errmsg']['simple_order_close_unpay_time']
        assert upayTime == orderUpayTime
    
    def test_selfpick_order_type_status_update(self, conf):
        pd = conf.api.Shop(conf)
        #打开自提
        parmDic = {'self_pickup_status': 1}
        pd.shipping_status_update(parmDic)
        #生成随机参数
        randInt = random.randint(1,4)
        selfpicklist = random.sample([1,2,8,9],randInt)
        payload = {"self_pickup":selfpicklist}
        print ("param data:",payload)
        respData = pd.shipping_order_type_status_update(payload)
        respSelfPickListStr = respData['errmsg']['self_pickup']
        respSelfPickList = respSelfPickListStr.strip('[').strip(']').split(",")
        assert  selfpicklist.sort() == respSelfPickList.sort()
        
    def test_shipping_order_type_status_update(self, conf):
        pd = conf.api.Shop(conf)
        #打开快递配送
        parmDic = {'shipping_status': 1}
        pd.shipping_status_update(parmDic)
        #生成随机参数
        randInt = random.randint(0,4)
        shippinglist = random.sample([1,2,8,9],randInt)
        payload = {"shipping":shippinglist}
        respData = pd.shipping_order_type_status_update(payload)
        respShippingListStr = respData['errmsg']['shipping']
        respShippingList = respShippingListStr.strip('[').strip(']').split(",")
        assert  shippinglist.sort() == respShippingList.sort()
        
    def test_shipping_status_update(self,conf):
        pd = conf.api.Shop(conf)
        selectType = random.choice(['shipping_status','self_pickup_status'])
        selectStatus = random.choice([1,2])
        payload = {selectType:selectStatus}
        resp = pd.shipping_status_update(payload)
        respTypeVaule = resp['errmsg'][selectType]
        assert selectStatus == respTypeVaule
        
class TestAddress(object):
    '''
    店铺常用地址用例
    '''
    id = None
    address = ''
    consignee = ''
    phone = ''
    isDefault = None
    isDefaultRefund = None
    
    def test_add_address(self, conf):
        pd = conf.api.Shop(conf)
        tmpStr = "".join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 10))
        tmpPhone = "".join(random.sample(['0','1','2','3','4','5','6','7','8','9'], 8)) 
        TestAddress.address = address = u'广东省深圳市南山区科技园' + tmpStr
        TestAddress.consignee = consignee = u'测试地址' + tmpStr
        TestAddress.phone = phoneNumber = '158' + tmpPhone
        TestAddress.isDefault = isdefault = random.choice([0,1])
        TestAddress.isDefaultRefund = isdefaultr = random.choice([0,1])
        payload = {"return_address": address, "return_consignee": consignee, "return_phone": phoneNumber, "is_default": isdefault,"is_default_refund": isdefaultr}
        respData = pd.add_used_address(payload)
        
        repIsDefault = respData['errmsg']['is_default']
        repIsDefaultR = respData['errmsg']['is_default_refund']
        repAddress = respData['errmsg']['return_address']
        repConsignee = respData['errmsg']['return_consignee']
        repPhone = respData['errmsg']['return_phone']
        TestAddress.id = respData['errmsg']['id']
        assert repIsDefault == isdefault
        assert repIsDefaultR == isdefaultr
        assert repAddress == address
        assert repConsignee == consignee
        assert repPhone == phoneNumber
        
    def test_get_used_address_list(self, conf):
        pd = conf.api.Shop(conf)
        respData = pd.get_used_address_list()
        dataList = respData['errmsg']['data']
        count = respData['errmsg']['page']['total_count']
        index = None
        for i in range(count):
            if dataList[i]['id'] == TestAddress.id:
                index = i
                break
        address = dataList[index]['return_address']
        consignee = dataList[index]['return_consignee']
        phone = dataList[index]['return_phone']
        isdefault = dataList[index]['is_default']
        isdefaultrefund = dataList[index]['is_default_refund']
        
        assert address == TestAddress.address
        assert consignee == TestAddress.consignee
        assert phone ==  TestAddress.phone
        assert isdefault == TestAddress.isDefault
        assert isdefaultrefund == TestAddress.isDefaultRefund
        
    def test_update_used_address(self, conf):
        pd = conf.api.Shop(conf)
        tmpStr = "".join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 10))
        tmpPhone = "".join(random.sample(['0','1','2','3','4','5','6','7','8','9'], 8)) 
        TestAddress.address = address = u'广东省深圳市宝安区西乡街道' + tmpStr
        TestAddress.consignee = consignee = u'测试地址' + tmpStr
        TestAddress.phone = phoneNumber = '159' + tmpPhone
        TestAddress.isDefault = isdefault = random.choice([0,1])
        TestAddress.isDefaultRefund = isdefaultr = random.choice([0,1])
        payload = {"id":TestAddress.id,"return_address": address, "return_consignee": consignee, "return_phone": phoneNumber, "is_default": isdefault,"is_default_refund": isdefaultr}
        respData = pd.update_used_address(payload)
        
        repIsDefault = respData['errmsg']['is_default']
        repIsDefaultR = respData['errmsg']['is_default_refund']
        repAddress = respData['errmsg']['return_address']
        repConsignee = respData['errmsg']['return_consignee']
        repPhone = respData['errmsg']['return_phone']
        addressID = respData['errmsg']['id']
        assert repIsDefault == isdefault
        assert repIsDefaultR == isdefaultr
        assert repAddress == address
        assert repConsignee == consignee
        assert repPhone == phoneNumber
        assert addressID == TestAddress.id

    def test_del_used_address(self, conf):
        pd = conf.api.Shop(conf)
        payload = {"id": TestAddress.id, "deleted": 3}
        respData = pd.update_used_address(payload)
        
        repIsDefault = respData['errmsg']['is_default']
        repIsDefaultR = respData['errmsg']['is_default_refund']
        repAddress = respData['errmsg']['return_address']
        repConsignee = respData['errmsg']['return_consignee']
        repPhone = respData['errmsg']['return_phone']
        addressID = respData['errmsg']['id']
        assert repIsDefault == TestAddress.isDefault
        assert repIsDefaultR == TestAddress.isDefaultRefund
        assert repAddress == TestAddress.address
        assert repConsignee == TestAddress.consignee
        assert repPhone == TestAddress.phone
        assert addressID == TestAddress.id

