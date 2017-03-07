# coding: utf-8
"""
API测试
"""
import time,random,json,chardet
import pytest



TIMER = 0.1


class TestTerminalManager:
    '''
    终端店API测试
    '''
    tm = None
    shopID = None
    defaultSubShopID = None
    randomSubShopID = None
    productInfo = {}
    clsdata = {}
    
    @pytest.fixture(scope="class",autouse=True)
    def setUp(self, conf):
        #初始化
        tm = conf.api.Terminal(conf)
        shop = conf.api.Shop(conf)
        shopRes = shop.get_shop()
        TestTerminalManager.shopID = shopRes['errmsg']['id']
        isOpenSub = shopRes['errmsg']['shopSetting']['is_open_sub']
        isSingleSetting = shopRes['errmsg']['shopSetting']['is_single_setting']
        if isOpenSub == 1:
            tm.main_sub_close()
        if isSingleSetting == 1:
            tm.single_setting_close()
        yield
        if isOpenSub == 1:
            tm.main_sub_open(conf)
        if isSingleSetting == 1:
            tm.single_setting_open()
            
    def test_terminal_list(self, conf):
        tm = conf.api.Terminal(conf)
        payload = {"_page":1,"_page_size":20,"isShowDisableShopsub":1}
        resp = tm.terminal_list(payload)
        
        totalCount = resp['errmsg']['page']['total_count']
        assert totalCount >= 1
        #获取随机分店ID
        subShopNum =len(resp['errmsg']['data'])
        randomInt = random.randint(0,subShopNum-1)
        TestTerminalManager.randomSubShopID = resp['errmsg']['data'][randomInt]['id']
        #获取默认分店ID
        terminalList = resp['errmsg']['data']
        for ter in terminalList:
            if ter['is_main_sub'] == 1:
                TestTerminalManager.defaultSubShopID = ter['id']
                break
    
    def test_terminal_edit(self,conf):
        tm = conf.api.Terminal(conf)
        #通过接口get_agent_franchisee获取分店信息
        InfoResp = tm.get_agent_franchisee(conf.TERMINAL_ID)
        phoneNum = '139' + ("".join(random.sample(['0','1','2','3','4','5','6','7','8','9'], 8)))
        param = conf.param.Terminal(conf).terminal_edit(InfoResp['errmsg'],phone=phoneNum)
        print("param:",param)
        editResp = tm.terminal_edit(param)
        print ("edit resp",editResp)        
    
    def test_main_sub_open(self ,conf):
        tm = conf.api.Terminal(conf)
        terminalRes = tm.main_sub_open()
        respShopID = terminalRes['errmsg']['shop_id']
        
        assert TestTerminalManager.shopID == respShopID
        
    def test_single_setting_open(self, conf):
        tm = conf.api.Terminal(conf)
        terminalRes = tm.single_setting_open()
        respShopID = terminalRes['errmsg']['shop_id']
        
        assert TestTerminalManager.shopID == respShopID
    
    def test_product_list(self,conf):
        tm = conf.api.Terminal(conf)
        payload = {"_page": 1, "_page_size": 10, "sale_scope": "", "name": ""}
        productRes = tm.product_list(payload)
        
        productList = productRes['data']
        randInt = random.randint(0,len(productList)-1)
        TestTerminalManager.productInfo = productList[randInt]
        totalCount = productRes['page']['total_count']
        assert totalCount >= 1
        
    def test_sub_shop_product_list(self,conf):
        tm = conf.api.Terminal(conf)
        productID = TestTerminalManager.productInfo['id']
        payload = {"page": 1, "count": 20, "product_id": productID, "shop_name": ""}
        resp = tm.sub_shop_product_list(payload)
        
        errmsg = resp['errmsg']
        assert errmsg == "ok"
        
    def test_sub_product_update(self, conf):
        tm = conf.api.Terminal(conf)
        productID = TestTerminalManager.productInfo['id']
        payload = conf.param.Terminal(conf).sub_product_update(product_id=productID,shop_sub_id=TestTerminalManager.shopID)
        resp = tm.sub_product_update(payload)
        
        errmsg = resp['errmsg']
        assert errmsg == "ok"
    
    def test_sub_sku_arr_update(self,conf):
        tm = conf.api.Terminal(conf)
        productID = TestTerminalManager.productInfo['id']
        skuNum = len(TestTerminalManager.productInfo['productSkus'])
        idsDic = {}
        for i in range(skuNum):
            reserves = str(random.randint(10,800))
            skuID = TestTerminalManager.productInfo['productSkus'][i]['id']
            idsDic[i] = {"shop_sub_id": TestTerminalManager.shopID, "sku_id": skuID, "product_id": productID, "reserves": reserves,}
        payload = {"ids":idsDic}        
        resp = tm.sub_sku_arr_update(payload)
        
        errmsg = resp['errmsg']
        assert errmsg == "ok"
        
    def test_set_main_sub(self,conf):
        tm = conf.api.Terminal(conf)
        resp1 = tm.set_main_sub(TestTerminalManager.randomSubShopID)
        errmsg1 = resp1['errmsg']
        assert errmsg1 == 'ok'
        resp1 = tm.set_main_sub(TestTerminalManager.defaultSubShopID)
     
    def test_single_setting_close(self, conf):
        tm = conf.api.Terminal(conf)
        terminalRes = tm.single_setting_close()
        respShopID = terminalRes['errmsg']['shop_id']
         
        assert TestTerminalManager.shopID == respShopID
        
    def test_main_sub_close(self ,conf):
        tm = conf.api.Terminal(conf)
        terminalRes = tm.main_sub_close()
        respShopID = terminalRes['errmsg']['shop_id']
         
        assert TestTerminalManager.shopID == respShopID
        
class TestTerminalScanPay(object):
    '''
    收银台管理相关接口用例
    '''
    subShopID = None
    shopScanPayStatus = None
    staffID = None
    staffScanPayStatus = None
    staffScanRefundStatus = None
    
    @pytest.fixture(scope="class",autouse=True)
    def setUp(self, conf):
        tm = conf.api.Terminal(conf)
        payload = {"_page":1,"_page_size":20,"isShowDisableShopsub":1}
        #获取随机分店ID与扫码支付状态
        resp = tm.terminal_list(payload)
        subShopNum =len(resp['errmsg']['data'])
        randomInt = random.randint(0,subShopNum-1)
        TestTerminalScanPay.subShopID = resp['errmsg']['data'][randomInt]['id']
        TestTerminalScanPay.shopScanPayStatus = resp['errmsg']['data'][randomInt]['shopSubSetting']['is_scan_pay']
        #获取随机员工收款码状态和退款权限状态
        reqData = conf.param.Terminal(conf).staff_list()
        staffResp = tm.staff_list(reqData)
        staffNum = len(staffResp['errmsg']['data'])
        randomInt1 = random.randint(0,staffNum-1)
        TestTerminalScanPay.staffID = staffResp['errmsg']['data'][randomInt1]['id']
        TestTerminalScanPay.staffScanPayStatus = staffResp['errmsg']['data'][randomInt1]['is_scan_pay']
        TestTerminalScanPay.staffScanRefundStatus = staffResp['errmsg']['data'][randomInt1]['is_scan_refund']
        #初始化
        if TestTerminalScanPay.shopScanPayStatus == 1:
            tm.terminal_scan_pay_close(TestTerminalScanPay.subShopID)
        if TestTerminalScanPay.staffScanPayStatus == 1:
            tm.staff_scan_pay_close(TestTerminalScanPay.staffID)
        if TestTerminalScanPay.staffScanRefundStatus == 1:
            tm.staff_pay_refund_close(TestTerminalScanPay.staffID)
        yield
        if TestTerminalScanPay.shopScanPayStatus == 1:
            tm.terminal_scan_pay_open(TestTerminalScanPay.subShopID)
        if TestTerminalScanPay.staffScanPayStatus == 1:
            tm.staff_scan_pay_open(TestTerminalScanPay.staffID)
        if TestTerminalScanPay.staffScanRefundStatus == 1:
            tm.staff_pay_refund_open(TestTerminalScanPay.staffID)         
    
    def test_terminal_scan_pay_open(self, conf):
        tm = conf.api.Terminal(conf)
        resp = tm.terminal_scan_pay_open(TestTerminalScanPay.subShopID)
        isScanPay = resp['errmsg']['is_scan_pay']
        assert isScanPay == 1
        
    def test_teriminal_scan_pay_close(self,conf):
        tm = conf.api.Terminal(conf)
        resp = tm.terminal_scan_pay_close(TestTerminalScanPay.subShopID)
        isScanPay = resp['errmsg']['is_scan_pay']
        assert isScanPay == 2
    
    def test_staff_scan_pay_open(self,conf):
        tm = conf.api.Terminal(conf)
        resp = tm.staff_scan_pay_open(TestTerminalScanPay.staffID)
        isScanpay = resp['errmsg']['is_scan_pay']
        assert isScanpay == 1
        
    def test_staff_scan_pay_close(self,conf):
        tm = conf.api.Terminal(conf)
        resp = tm.staff_scan_pay_close(TestTerminalScanPay.staffID)
        isScanpay = resp['errmsg']['is_scan_pay']
        assert isScanpay == 2
        
    def test_staff_pay_refund_open(self,conf):   
        tm = conf.api.Terminal(conf)
        resp = tm.staff_pay_refund_open(TestTerminalScanPay.staffID)
        isScanRefund = resp['errmsg']['is_scan_refund']
        assert isScanRefund == 1
        
    def test_staff_pay_refund_close(self,conf):   
        tm = conf.api.Terminal(conf)
        resp = tm.staff_pay_refund_close(TestTerminalScanPay.staffID)
        isScanRefund = resp['errmsg']['is_scan_refund']
        assert isScanRefund == 2
        
class TestTerminalSettlement(object):
    '''
    结算相关测试用例
    '''
    
    def test_statement_hq(self,conf):
        tm = conf.api.Terminal(conf)
        payload = conf.param.Terminal(conf).statement_param()
        resp = tm.statement_hq(payload)
        
        errmsg = resp['errmsg']
        payNums = resp['data']['totalData']['payNums']
        assert errmsg == 'ok'
        assert payNums >= 0
    
    def test_statment_sub(self,conf):
        tm = conf.api.Terminal(conf)
        payload = conf.param.Terminal(conf).statement_param()
        resp = tm.statement_sub(payload)
        
        errmsg = resp['errmsg']
        payNums = resp['data']['totalData']['payNums']
        assert errmsg == 'ok'
        assert payNums >= 0
        
    def test_statment_find_push_record(self,conf):
        tm = conf.api.Terminal(conf)
        payload = conf.param.Terminal(conf).statement_param()
        resp = tm.statement_find_push_record(payload)
        
        errmsg = resp['errmsg']
        assert errmsg == 'ok'
        
class TestTerminalReduction(object):
    '''
    分店满减活动测试用例
    '''
    terminalReductionID = None
    staffReductionID = None
    
    def test_terminal_reduction_add(self, conf):
        tm = conf.api.Terminal(conf)
#         storeResp = tm.reduction_store_list({"shop_type": "1"})
#         storeIDList = []
#         for store in storeResp['errmsg']:
#             storeIDList.append(store['_id'])
        payload = conf.param.Terminal(conf).reduction_add(reduction_type=[1,3],terminal=2)
        resp = tm.terminal_reduction_add(payload)
        TestTerminalReduction.terminalReductionID = terReductionID = resp['errmsg']['id']
        assert terReductionID != 0
    
    def test_terminal_reduction_open(self,conf):
        tm = conf.api.Terminal(conf)
        resp = tm.terminal_reduction_open(TestTerminalReduction.terminalReductionID)
        reductionID = resp['errmsg']['id']
        
        assert reductionID == TestTerminalReduction.terminalReductionID 
    
    def test_terminal_reduction_close(self,conf):
        tm = conf.api.Terminal(conf)
        resp = tm.terminal_reduction_close(TestTerminalReduction.terminalReductionID)
        reductionID = resp['errmsg']['id']
        
        assert reductionID == TestTerminalReduction.terminalReductionID    
    
    def test_terminal_reduction_list(self, conf):
        tm = conf.api.Terminal(conf)
        payload = conf.param.Terminal(conf).reduction_list(terminal=2)
        resp = tm.terminal_reduction_list(payload)
        
        totalCount = resp['errmsg']['page']['total_count']
        reductionIDList = []
        reductionList = resp['errmsg']['data']
        for key in reductionList:
            reductionIDList.append(key['id'])

        assert totalCount >= 0
        assert TestTerminalReduction.terminalReductionID in reductionIDList
        
    def test_terminal_reduction_delete(self,conf):
        tm = conf.api.Terminal(conf)
        resp = tm.terminal_reduction_delete(TestTerminalReduction.terminalReductionID)
        
    def test_staff_reduction_add(self, conf):
        tm = conf.api.Terminal(conf)
        staffResp = tm.reduction_staff_list({"shop_type": "1"})
        staffIDList = []
        for staff in staffResp['errmsg']:
            if staff['children'][0]['is_scan_pay'] ==1:
                staffIDList.append(staff['children'][0]['_id'])
        reductionName = "员工收款码满减活动-" + time.strftime('%m%d%H%M',time.localtime(time.time()))
        payload= conf.param.Terminal(conf).reduction_add(reduction_type=[1,3],terminal_ids=staffIDList,terminal=3,name=reductionName)
        resp = tm.staff_reduction_add(payload)
         
        TestTerminalReduction.staffReductionID = staReductionID = resp['errmsg']['id']
        assert staReductionID != 0
   
    def test_staff_reduction_open(self,conf):
        tm = conf.api.Terminal(conf)
        resp = tm.staff_reduction_open(TestTerminalReduction.staffReductionID)
        reductionID = resp['errmsg']['id']
         
        assert reductionID == TestTerminalReduction.staffReductionID 
     
    def test_staff_reduction_close(self,conf):
        tm = conf.api.Terminal(conf)
        resp = tm.staff_reduction_close(TestTerminalReduction.staffReductionID)
        reductionID = resp['errmsg']['id']
         
        assert reductionID == TestTerminalReduction.staffReductionID  
     
    def test_staff_reduction_list(self,conf):
        tm = conf.api.Terminal(conf)
        payload = conf.param.Terminal(conf).reduction_list(terminal=3)
        resp = tm.staff_reduction_list(payload)
         
        totalCount = resp['errmsg']['page']['total_count']
        reductionIDList = []
        reductionList = resp['errmsg']['data']
        for key in reductionList:
            reductionIDList.append(key['id'])
 
        assert totalCount >= 0
        assert TestTerminalReduction.staffReductionID in reductionIDList
 
    def test_staff_reduction_delete(self,conf):
        tm = conf.api.Terminal(conf)
        resp = tm.staff_reduction_delete(TestTerminalReduction.staffReductionID)
        
class TestTerminalStatistics(object):
    '''
    分店数据统计
    '''
    
    def test_order_statistics_by_shop(self, conf):
        tm = conf.api.Terminal(conf)
        paramData = conf.param.Terminal(conf).order_statistics()
        resp = tm.order_statistics_by_shop(paramData)
        print( "resp:",resp)
        
    def test_order_statistics_by_staff(self, conf):
        tm = conf.api.Terminal(conf)
        paramData = conf.param.Terminal(conf).order_statistics()
        resp = tm.order_statistics_by_staff(paramData)
        print( "resp:",resp)
        
    def test_aftersales_statistics_by_shop(self, conf):
        tm = conf.api.Terminal(conf)
        paramData = conf.param.Terminal(conf).aftersales_statistics()
        resp = tm.aftersales_statistics_by_shop(paramData)
        print( "resp:",resp)
        
    def test_aftersale_statistics_by_staff(self, conf):
        tm = conf.api.Terminal(conf)
        paramData = conf.param.Terminal(conf).aftersales_statistics()
        resp = tm.aftersale_statistics_by_staff(paramData)
        print( "resp:",resp)
    
    def test_member_statistics_by_shop(self, conf):
        tm = conf.api.Terminal(conf)
        paramData = conf.param.Terminal(conf).member_statistics()
        resp = tm.member_statistics_by_shop(paramData)
        print( "resp:",resp)
        
    def test_member_statistics_by_staff(self, conf):
        tm = conf.api.Terminal(conf)
        paramData = conf.param.Terminal(conf).member_statistics()
        resp = tm.member_statistics_by_staff(paramData)
        print( "resp:",resp)
        
    def test_customer_statistics_by_shop(self, conf):
        tm = conf.api.Terminal(conf)
        paramData = conf.param.Terminal(conf).customer_statistics()
        resp = tm.customer_statistics_by_shop(paramData)
        print( "resp:",resp)
        
    def test_customer_statistics_by_staff(self, conf):
        tm = conf.api.Terminal(conf)
        paramData = conf.param.Terminal(conf).customer_statistics()
        resp = tm.customer_statistics_by_staff(paramData)
        print( "resp:",resp)
        
    def test_promotion_statistics_by_shop(self, conf):
        tm = conf.api.Terminal(conf)
        paramData = conf.param.Terminal(conf).promotion_statistics()
        resp = tm.promotion_statistics_by_shop(paramData)
        print( "resp:",resp)
        
    def test_promotion_statistics_by_staff(self, conf):
        tm = conf.api.Terminal(conf)
        paramData = conf.param.Terminal(conf).promotion_statistics()
        resp = tm.promotion_statistics_by_staff(paramData)
        print( "resp:",resp)

    def test_promotion_statistics_by_promoter(self, conf):
        tm = conf.api.Terminal(conf)
        paramData = conf.param.Terminal(conf).promotion_statistics()
        resp = tm.promotion_statistics_by_promoter(paramData)
        print( "resp:",resp) 

class TestSubTerminal(object):
    '''
    分店相关用例
    '''
    roleID = None
    realName = ''
    staffID = None
    
    def test_get_agent_franchisee(self, conf):
        tm = conf.api.Terminal(conf)
        resp = tm.get_agent_franchisee(conf.TERMINAL_ID)
         
        terminalID = resp['errmsg']['id']
        assert conf.TERMINAL_ID == terminalID
         
    def test_qrcode_detail(self, conf):
        tm = conf.api.Terminal(conf)
        paramData = conf.param.Terminal(conf).qrcode_detail(model_id=conf.TERMINAL_ID)
        resp = tm.qrcode_detail(paramData)
         
        print( "resp:",resp)
         
    def test_statement_receive_setting(self, conf):
        tm = conf.api.Terminal(conf)
        phoneNum = '139' + ("".join(random.sample(['0','1','2','3','4','5','6','7','8','9'], 8)))
        paramData = conf.param.Terminal(conf).statement_receive_setting(shop_sub_id=conf.TERMINAL_ID,tel=phoneNum)
        resp = tm.statement_receive_setting(paramData)
         
        print( "resp:",resp)
        
    def test_role_add(self, conf):
        tm = conf.api.Terminal(conf)
        param = conf.param.Terminal(conf).role_add()
        resp = tm.role_add(param)
        
        TestSubTerminal.roleID = roleID = resp['errmsg'][0]['id']
        assert roleID != 0    
        
    def test_save_role_function(self, conf):
        tm = conf.api.Terminal(conf)
        param = conf.param.Terminal(conf).save_role_function(auth_role_id=TestSubTerminal.roleID)
        resp = tm.save_role_function(param)
        
        authoRoleID = resp['errmsg'][0]['auth_role_id']
        assert TestSubTerminal.roleID == authoRoleID
        
    def test_role_list(self,conf):
        tm = conf.api.Terminal(conf)
        resp = tm.role_list()
          
        hasRole = False
        print ("roleID:",TestSubTerminal.roleID)
        for role in resp['errmsg']['data']:
            if role['id'] == TestSubTerminal.roleID:
                hasRole = True
                break
        assert hasRole is True

    def test_staff_add(self,conf):
        tm = conf.api.Terminal(conf)
        randStr = "".join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 8))
        TestSubTerminal.realName = realName = u'员工' + randStr
        phoneNum = '139' + ("".join(random.sample(['0','1','2','3','4','5','6','7','8','9'], 8)))
        param = conf.param.Terminal(conf).staff_add(role_id=TestSubTerminal.roleID,shop_sub_id=conf.TERMINAL_ID,mobile=phoneNum,user_name=randStr,real_name=realName)
        resp = tm.staff_add(param)
        print( "resp:",resp)
         
    def test_staff_list(self, conf):
        tm = conf.api.Terminal(conf)
        param = conf.param.Terminal(conf).staff_list()
        resp = tm.staff_list(param)
          
        totalCount = resp['errmsg']['page']['total_count']
        assert totalCount >= 0
         
        for data in resp['errmsg']['data']:
            if data['real_name'] == TestSubTerminal.realName:
                TestSubTerminal.staffID = data['id']
                break
        print ("staffID:",TestSubTerminal.staffID)
         
    def test_staff_dell(self,conf):
        tm = conf.api.Terminal(conf)
        resp = tm.staff_dell(TestSubTerminal.staffID)
          
        print( "resp:",resp)
      
    def test_role_delete(self, conf):
        tm = conf.api.Terminal(conf)
        resp = tm.role_delete(TestSubTerminal.roleID)
        print( "resp:",resp)
         
    def test_terminal_members_list(self,conf):
        tm = conf.api.Terminal(conf)
        param = conf.param.Terminal(conf).terminal_members_list(shop_sub_id=str(conf.TERMINAL_ID))
        resp = tm.terminal_members_list(param)
         
        totalCount = resp['errmsg']['page']['total_count']
        assert totalCount >=0
         
    def test_members_last_count(self,conf):
        tm = conf.api.Terminal(conf)
        param = conf.param.Terminal(conf).members_last_count(shop_sub_id=str(conf.TERMINAL_ID))
        resp = tm.members_last_count(param)
        
        lastDayCount = int(resp['errmsg']['last_day_count'])
        assert lastDayCount >= 0
    
    def test_terminal_member_list(self,conf):
        tm = conf.api.Terminal(conf)
        param = conf.param.Terminal(conf).terminal_member_list(shop_sub_id=str(conf.TERMINAL_ID))
        resp = tm.terminal_member_list(param)
         
        totalCount = resp['page']['total_count']
        assert totalCount >=0
         
    def test_terminal_count_wx_member(self, conf):
        tm = conf.api.Terminal(conf)
        param = conf.param.Terminal(conf).terminal_count_wx_member(shop_sub_id=str(conf.TERMINAL_ID))
        resp = tm.terminal_count_wx_member(param)
         
        wxTotal = int(resp['errmsg']['wx_total'])
        assert wxTotal >=0
        
    def test_cancel_member_list(self,conf):
        tm = conf.api.Terminal(conf)
        resp = tm.cancel_member_list()
        
        totalCount = resp['errmsg']['page']['total_count']
        assert totalCount >= 0
        
    def test_cancel_card(self,conf):
        #获取用户
        memberID = None
        member  = conf.api.Member(conf)
        memberResp = member.member_list()
        for mem in memberResp['errmsg']['data']:
            if mem['shop_sub_id'] == conf.TERMINAL_ID:
                memberID = mem['id']
                break
        #获取卡券
        market = conf.api.Market(conf)
        cardParam = conf.param.Market(conf).card_coupons_add()
        cardRes = market.card_coupons_add(cardParam)
        cardID = cardRes['errmsg']['id']

        #派发卡券
        data = {"user_type":1,"card_type_ids":[cardID],"to_user_ids":[memberID],"user_group":[]}
        cardSendResp = market.card_coupons_send(data)
        cardCode = cardSendResp['errmsg']['sendUserCard'][0]['cardInfo']['cardInfo']['code']
        #核销
        tm = conf.api.Terminal(conf)
        cancelCardRes = tm.cancel_card({"code":cardCode})
        codeResp = cancelCardRes['errmsg']['code']
        assert codeResp == cardCode
        #删除卡券
        market.card_coupons_del(cardID)
    
    def test_cancel_record_list(self,conf):
        tm = conf.api.Terminal(conf)
        param = conf.param.Terminal(conf).cancel_record_list()
        resp = tm.cancel_record_list(param)

        totalCount = resp['errmsg']['page']['total_count']
        assert totalCount >= 0
        
    def test_shopsub_cancel_list(self,conf):
        tm = conf.api.Terminal(conf)
        param = conf.param.Terminal(conf).shopsub_cancel_list()
        resp = tm.shopsub_cancel_list(param)

        totalCount = resp['errmsg']['page']['total_count']
        assert totalCount >= 0   
  
    def test_staff_cancel_list(self,conf):
        tm = conf.api.Terminal(conf)
        param = conf.param.Terminal(conf).staff_cancel_list()
        resp = tm.staff_cancel_list(param)

        totalCount = resp['errmsg']['page']['total_count']
        assert totalCount >= 0          
        
    def test_fx_member_list(self,conf):
        tm = conf.api.Terminal(conf)
        param = conf.param.Terminal(conf).fx_member_list()
        resp = tm.fx_member_list(param)
        
        totalCoutn = resp['errmsg']['page']['total_count']
        assert totalCoutn >= 0
    
    def test_fx_order_list(self,conf):
        tm = conf.api.Terminal(conf)
        param = conf.param.Terminal(conf).fx_order_list()
        resp = tm.fx_order_list(param)
        
        totalCoutn = resp['errmsg']['page']['total_count']
        assert totalCoutn >= 0    
    
    def test_order_list(self, conf):
        tm = conf.api.Terminal(conf)
        orderStatus = random.choice([0,1,2,3,4,5,7])
        afterSalesStatus = random.choice([1,2,None])
        param = conf.param.Terminal(conf).order_list(shop_sub_id=str(conf.TERMINAL_ID),_status=orderStatus,after_sales_status=afterSalesStatus)
        resp = tm.order_list(param)
         
        totalCount = resp['errmsg']['page']['total_count']
        assert totalCount >=0    
         
    def test_refund_list(self, conf):
        tm = conf.api.Terminal(conf)
        param = conf.param.Terminal(conf).refund_list(shop_sub_id=str(conf.TERMINAL_ID))
        resp = tm.refund_list(param)
         
        totalCount = resp['errmsg']['page']['total_count']
        assert totalCount >=0    
        