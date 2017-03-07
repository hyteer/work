#coding:utf-8

import random,time
from .generic import Generic as g

class Shop(object):
    
    def __init__(self,conf):
        self.conf = conf
    
    def product_add(self,**args):
        

        shop = self.conf.api.Shop(self.conf)

        #商品名称
        timeStr = time.strftime("%m%d%H%M",time.localtime())
        productName = timeStr + "测试商品"
        #商品分类
        firstCateResp = shop.category_list({"_page_size":15,"_page":1})
        firstCateID = None
        for firstCate  in firstCateResp['errmsg']['data']:
            if firstCate['name'] == '系统分类':
                firstCateID = firstCate['id']
        print('firstCateID:',firstCateID)
        
        secondCateResp = shop.category_list({"pid":firstCateID})
        secondCateID = None
        secondCaterandom = random.randint(0,len(secondCateResp['errmsg']['data'])-1)
        if secondCateResp['errmsg']['data'][secondCaterandom]['name'] == '默认分类':
            secondCaterandom = secondCaterandom +1
            secondCateID=secondCateResp['errmsg']['data'][secondCaterandom]['id']
        else:
            secondCateID=secondCateResp['errmsg']['data'][secondCaterandom]['id']
        print("secondCateID:",secondCateID)
        
        thirdCateResp = shop.category_list({"pid":secondCateID})
        thirdCaterandom = random.randint(0,len(thirdCateResp['errmsg']['data'])-1)
        thirdCateID = thirdCateResp['errmsg']['data'][thirdCaterandom]['id']
        categoryPath = thirdCateResp['errmsg']['data'][thirdCaterandom]['path']
        print("thirdCateID:",thirdCateID)
        #商品规格
        kindListResp = shop.kind_list()
        kindRandomInt = random.randint(0,len(kindListResp['errmsg']['data'])-1)
        kindID = kindListResp['errmsg']['data'][kindRandomInt]['id']
        kindIDStr = str(kindID)+";"
        kindValueResp = shop.kind_value_list(kindID)
        kindValueRandom = random.randint(0,len(kindValueResp['errmsg']['data'])-1)
        kindValueID = kindValueResp['errmsg']['data'][kindValueRandom]['id']
        kindName = kindValueResp['errmsg']['data'][kindValueRandom]['name']
        #商品图片
        imageParam = self.document_image()
        imageResp = shop.document_image(imageParam)
        imageRandom = random.randint(0,len(imageResp['errmsg']['data'])-1)
        coversID = imageResp['errmsg']['data'][imageRandom]['id']
        imageFileCDNPath = imageResp['errmsg']['data'][imageRandom]['file_cdn_path']
        detailPicID = str(coversID)+';'
        #市场价
        marketPrice = str(random.randint(160,200))
        #零售价
        retailPrice = str(random.randint(120,160))
        #条形码
        barCode = ''
        choices = ['0','1','2','3','4','5','6','7','8','9']
        for i in range(13):
            barCode += random.choice(choices)
        #商品编码
        skuNo= (random.choice(['a','b','c','e','f'])+("".join(random.sample(['0','1','2','3','4','5','6','7','8','9'], 10)))).upper()        
        #库存
        reserves = random.randint(500,1000)
        #商品重量
        prodWeight = str(random.randint(800,2000))
        
        product = {"product_type":1,"name":productName,"sales":"123","covers_id":coversID,"quota":"0","sort":"0","sale_scope":"3","product_category_id":thirdCateID,
                   "product_category_path":categoryPath,"status":2,"postage_fee_type":0,"product_kind_ids":kindIDStr,"show_sale_num":2,"prod_weight":prodWeight}
        productInfo = {"detail_pic":detailPicID,"detail":"<p>测试商品</p>"}
        shareMessage = {"desc":"优惠多多,欢迎选购","title":"测试商品","file_cdn_path":imageFileCDNPath,"pic_id":coversID}
        kindBodyDic =  {"firstName":kindName,"firstRowSpan":1,"firstShow":True,"id":kindName,"status":False}
        skuDic = {"status":1,"reserves":reserves,"market_price":marketPrice,"retail_price":retailPrice,"sku_no":skuNo,"barcode":barCode,"sales":0,"name":productName,"kind_value_ids":[kindValueID],"kind_ids":[kindID]}
        
        for key in args:
            if key == 'name':
                product[key] = args[key]
                skuDic[key] = args[key]
            elif key in product:
                product[key] = args[key]
            elif key in productInfo:
                productInfo[key] = args[key]
            elif key in shareMessage:
                shareMessage[key] = args[key]
            elif key in kindBodyDic:
                kindBodyDic[key] = args[key]
            elif key in skuDic:
                skuDic[key] = args[key]
            else :
                raise AssertionError("the args dictionary does not has the key:%s" % key)

        kindBodyList = [kindBodyDic]
        skuList = [skuDic]
        productInfomation = {"productInfo":productInfo,"product":product,"shareMessage":shareMessage,"kindBody":kindBodyList,"skus":skuList}

        return productInfomation

    def document_image(self,**kwargs):
        '''
        '''
        template = {"_page":1,"_page_size":15,"category_id":"","name":""}
        return g.get_params(template, kwargs)

    def product_list(self,**argsd):
        '''

        ====================   =========  =========================================
          字段                  类型                             描述
        ====================   =========  =========================================
        is_search               boolean     选填，是否取缓存数据
        name                    String     选填，商品名称
        product_category_id     Number     选填，商品分类
        sale_scope              Number     选填，销售平台
        status                  Number     选填，上下架状态
        reserves                Number     选填，库存筛选
        page                    Number     选填，页码(可照旧使用_page)
        count                   Number     选填，每页数据量（可照旧使用_page_size）
        ====================   =========  =========================================
        '''
        paramDic = {"_page": 1, "_page_size": 10}
        paraList = ['is_search','name','product_category_id','sale_scope','status','reserves','page','count']
        for key in argsd:
            if key in paraList:
                paramDic[key] = argsd[key]
            else:
                raise AssertionError("the args dictionary does not has the key:%s" % key)       
        return paramDic

    def comment_without_user(self,**args):
        '''
        '''
        shop = self.conf.api.Shop(self.conf)
        timeStr = time.strftime("%m%d%H%M",time.localtime())
        createTime = int(time.time())
        systemImageRes = shop.get_system_image()
        avatar = systemImageRes['errmsg']['headimgurl']
        
        star = random.choice(['1','2','3','4','5'])
        
        productParam = self.product_list()
        productResp = shop.product_list(productParam)
        proRand = random.randint(0,len(productResp['errmsg']['data'])-1)
        productID = productResp['errmsg']['data'][proRand]['id']
        productName = productResp['errmsg']['data'][proRand]['name'] 
        
        commont = timeStr + productName + '东西很好，很超值'
        
        commentDic = {"avatar":avatar,"content":commont,"created":createTime,"product_id":productID,"star":star}
        return g.get_params(commentDic, args)

    def order_list(self,**args):
        '''
        ================    ========   ================================================================
         字段                 类型                             描述
        ================    ========   ================================================================
        _status              Number     选填，状态 0全部 1待付款 2待发货 3待收货4已完成5售后中7已关闭
        order_no             Number     选填，对应的订单号
        createStart          Number     选填，订单开始的创建时间
        createEnd            Number     选填，订单结束创建时间
        service_no           Number     选填，售后单的service_no
        order_type           Number     选填，订单类型
        s_consignee          String     选填，收货人
        s_tel                Number     选填，收货人手机号
        pay_type             Number     选填，对应订单的支付类型
        should_pay_min       String     选填，应付最小金额
        should_pay_max       String     选填，应付最大金额
        user_name            String     选填，微信昵称
        pickup_type          Number     选填，对应订单的配送方式
        shop_sub_id          Array     选填，对应订单的分店id数组
        agent_id             Array     选填，对应订单的agent_id数组
        staff_id             Array     选填，订单的所属员工id数组
        page                 Number     选填，页码(可照旧使用_page)
        count                Number     选填，每页数据量（可照旧使用_page_size）
        ================    ========   ================================================================
        '''
        defaultDic = {"_status":0,"after_sales_status":None,"pickup_type":None,"_page":1,"_page_size":20,"order_type":None,"s_tel":None,"s_consignee":None,
                      "createStart":None,"createEnd":None,"order_no":None,"pay_type":None,"should_pay_min":None,"should_pay_max":None,"user_name":None,
                      "express_type":None,"agent_id":None,"shop_sub_id":None,"staff_id":None,"pay_time_start":None,"pay_time_end":None,"pickup_date_start":None,
                      "pickup_date_end":None,"consignor_status":None,"statement":None}
        return g.get_params(defaultDic, args)

    def refund_list(self,**args):
        '''
        =============     =======    ==========================================================
        字段              类型        描述
        =============     =======    ==========================================================
        order_id          Number     选填，售后单对应的订单id
        shop_sub_id       Array      选填，售后单对应订单的分店id数组
        agent_id          Array      选填，售后单对应订单的agent_id数组
        shop_staff_id     Array      选填，售后单对应订单的所属员工id数组
        order_type        Number     选填，售后单对应订单的类型（参照订单获取接口）
        pay_type          Number     选填，售后单对应订单的支付类型（参照订单获取接口）
        createStart       Number     选填，售后单开始的创建时间
        createEnd         Number     选填，售后单结束创建时间
        user_phone        String     选填，售后单用户填写的电话
        user_name         String     选填，下单时用户的微信昵称
        tel               String     选填，售后单对应订单的送货信息的用户电话
        consignee         String     选填，售后单对应订单的发货人
        service_no        String     选填，售后单的service_no
        order_no          String     选填，售后单对应订单的order_no
        type              Number     选填，售后单类型（参照/order/get-after-sale-detail-ajax）
        pickup_type       Number     选填，售后单对应订单的配送方式
        page              Number     选填，页码(可照旧使用_page)
        count             Number     选填，每页数据量（可照旧使用_page_size）
        =============     =======    ==========================================================
        '''
        defaultDic = {"_page":1,"_page_size":20,"createStart":"","createEnd":"","pay_type":"","order_type":"","type":"","processing_state":"","pickup_type":"",
                      "order_id":"","tel":"","consignee":"","order_no":"","user_phone":"","service_no":"","user_name":"","agent_id":[],"shop_sub_id":[],"shop_staff_id":[]}
        return g.get_params(defaultDic, args)

    def shop_order_auto_settings(self,**args):
        '''	
		更新订单自动任务设置信息(交易设置)
		===================================   ========    ============================================================
			字段                               类型                   描述
		===================================   ========    ============================================================
		id                                     Number     必填，要更新的设置的对应id
		simple_order_close_unpay_time          Number     可选,普通订单创建后可支付的时限
		auto_receive_time                      Number     可选,发货后可收货时限
		sk_order_close_unpay_time              Number     可选,秒杀订单创建后可支付的时限
		order_comment_time                     Number     可选,订单收货后可评论的时限
		simple_order_close_unpay_status        Number     可选,普通订单不支付自动关闭 1.开启、2.关闭
		auto_receive_status                    Number     可选,发货后自动收货 1.开启、2.关闭
		sk_order_close_unpay_status            Number     可选,秒杀订单不支付自动关闭 1.开启、2.关闭
		order_comment_status                   Number     可选,订单收货后自动评论 1.开启、2.关闭
		simple_order_close_unpay_time_type     Number     可选,普通订单创建后可支付的时限单位（1.分钟、2.小时、3.天）
		auto_receive_time_type                 Number     
		sk_order_close_unpay_time_type         Number     
		order_comment_time_type                Number
		===================================   ========    ============================================================
        '''
        defaultdic = {"id":20,"simple_order_close_unpay_time":86400,"auto_receive_time":604800,"sk_order_close_unpay_time":600,"order_comment_time":259200,
                      "simple_order_close_unpay_status":1,"auto_receive_status":1,"sk_order_close_unpay_status":1,"order_comment_status":1,
                      "simple_order_close_unpay_time_type":2,"auto_receive_time_type":3,"sk_order_close_unpay_time_type":1,"order_comment_time_type":3}
        for key in args:
            if "status" in key and key in defaultdic:
                if args[key] in [1,2]:
                    defaultdic[key] = args[key]
                else:
                    raise AssertionError("the key value is error :%s" % key)
            elif "type" in key and key in defaultdic:
                if args[key] in [1,2,3]:
                    defaultdic[key] = args[key]
                else:
                    raise AssertionError("the key value is error :%s" % key)
            elif key in defaultdic:
                defaultdic[key] = args[key]
            else:
                raise AssertionError("the args dictionary does not has the key:%s" % key)
        return defaultdic

    def order_deliver(self,order_id,**kargs):
        '''
        ================    ========   ================================================================
         字段                 类型                             描述
        ================    ========   ================================================================
        order_id             Number     必填，订单ID
        express_type         Number     选填，快递类型，默认2(申通快递)
        seller_remark        String     选填，发货备注
        express_no           Number     选填，快递单号
        ================    ========   ================================================================
        '''
        defaultDic = {"order_id":order_id,"express_type":"2","seller_remark":"已发货。。。","express_no":"5545555888555445"}
        return g.get_params(defaultDic, kargs)
