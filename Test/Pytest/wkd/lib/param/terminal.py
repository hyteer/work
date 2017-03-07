#coding:utf-8


import time,json,random

from .utils import Utils
from .generic import Generic as g


class Terminal(object):

    def __init__(self,conf):
        self.conf = conf

    def terminal_add(self,**args):
        paraDic = {"shopInfo[province_id]":137,"shopInfo[city_id]":138,"shopInfo[district_id]":139,
"shopInfo[circle_id]":140,
"shopInfo[name]":"分店测试0207",
"shopInfo[phone]":"15895623569",
"shopInfo[url]":"http://www.360.cn",
"shopInfo[bg_img]":"https://imgcache.vikduo.com/static/44ae6a2fae8d1ae7acddc0129dabb128.png",
"shopInfo[logo]":"https://imgcache.vikduo.com/static/89c357c48d8830326acfa5fb4b4cc3f7.png",
"shopInfo[avg_price]":30,
"shopInfo[recommend]":"没有特色推荐",
"shopInfo[special]":"没有特色服务",
"shopInfo[description]":"没有描述",
"shopInfo[address]":"比克大厦",
"shopInfo[businesshour]":"08:00-21:00",
"shopInfo[wx_categories][0][id]":1,
"shopInfo[wx_categories][0][name]":"美食",
"shopInfo[wx_categories][1][id]":16,
"shopInfo[wx_categories][1][name]":"粤菜",
"shopInfo[wx_categories][2][id]":17,
"shopInfo[wx_categories][2][name]":"潮汕菜",
"shopInfo[businessweek][0][Monday]":1,
"shopInfo[businessweek][0][Tuesday]":1,
"shopInfo[businessweek][0][Wednesday]":1,
"shopInfo[businessweek][0][Thursday]":1,
"shopInfo[businessweek][0][Friday]":1,
"shopInfo[businessweek][0][Saturday]":1,
"shopInfo[businessweek][0][Sunday]":0,
"shopInfo[shipping_status]":1,
"shopInfo[intracity_shipping_status]":2,
"shop_type":1,
"shopStaff[user_name]":"test0207",
"shopStaff[password]":"test0207",
"shopStaff[real_name]":"test",
"lat":22.541222892341,
"lng":113.932718326450,
"is_pickup_shop":1}
    

    def terminal_edit(self,originalInfo,**kwargs):
        '''
        '''
        #originalInfo为接口/terminal/get-agent-franchisee-ajax获取的信息
        originalInfo['shopInfo'].pop('staff_total_count')
        originalInfo['shopInfo'].pop('agent_name')
        originalInfo['shopInfo'].pop('fx_member_count')
        #originalInfo的wx_categories的编码转换,转换成中文
        wxCategories = originalInfo['shopInfo']['wx_categories']
        print("type:",type(wxCategories))
        uniCategories = wxCategories.encode('UTF-8').decode('unicode_escape').strip('"')
        categoriesDic = json.loads(uniCategories)
        originalInfo['shopInfo']['wx_categories'] = categoriesDic
        g.get_params(originalInfo['shopInfo'], kwargs)
        return originalInfo
    
    def terminal_list(self,**kwargs):
        '''
        '''
        template = {"_page":1,"_page_size":20,"shop_type":1,"name":"","search_all":True,"isShowDisableShopsub":1}
        return g.get_params(template, kwargs)
    
    def sub_product_update(self,**args):
        '''
    ===========================     ===========     ===================================
              字段                     类型                        描述
    ===========================     ===========     ===================================
     intracity_shipping_status        int                  卡券标题
	 product_id                       string                商品ID
	 self_pickup_status               int                   到店自提
	 shipping_status                  int                   快递配送
	 shop_sub_id                      int                   分店ID
	 status                           int                   商品上下架状态
    ===========================     ===========     ===================================
	    '''
        template = {"product_id": "289888", "shop_sub_id": 109829, "shipping_status": 1, "self_pickup_status": 1,"intracity_shipping_status":2,"status":1}
        return g.get_params(template,args)
    
    def staff_list(self,**args):
        '''
	===============     =========   ====================
	   字段                类型            描述
	===============     =========   ====================
	 _page                int            页数
	 _page_size           int            每页大小
	 agent_id             int            商店ID 
	 real_name            string         真实姓名
	 search_all           bool           是否搜索所有
	 shop_type            int            分店类型
	 terminal_id          int            分店ID 
	===============     =========   ====================
	    '''
        template = {"_page":1,"_page_size":20,"agent_id":None,"real_name":"","search_all":True,"shop_type":1,"terminal_id":None}
        return g.get_params(template, args)
    
    def statement_param(self,**args):
        '''
        '''
                #当前时间
        now = time.time()
        #当天凌晨
        midnight = now - (now % 86400) + time.timezone
        #昨天凌晨
        createStart = int(midnight - 86400)
        #昨天23.59.59
        createEnd = int(midnight - 1)
        template = {"page": 1, "count": 20, "search_type": 1, "payTimeEnd": createEnd, "payTimeStart": createStart, "hideZero": 0,"keyword":""}
        return g.get_params(template, args)
    
    def reduction_list(self,**args):
        '''
	=============  ==========    =================================
	  字段 	          类型 	        描述
	=============  ==========    =================================
	 name 	         string 	   选填，活动名称
	 start_time 	     Number 	   选填，活动开始时间
	 end_time 	     Number 	   选填，活动结束时间
	 deleted 	     Number 	   选填，活动状态 1.启用 2.禁用
	 isUnstart 	     Number 	   选填，是否开始，值传1
	 underwayFlag 	 Number 	   选填，值传1
	 isEnd 	         Number 	   选填，是否结束，值传1
	 _page 	         Number 	   选填，当前页码
	 _page_size 	 Number 	   选填，每页条数
	 =============  ==========    =================================
        '''
        template = {"terminal": 2, "name": "", "start_time": "", "end_time": "", "deleted": "", "_page": 1, "_page_size": 10,"shop_type":1}
        return g.get_params(template, args)
    
    def reduction_add(self,**args):   
        '''
		====================   ========   ================================================================================================
		  字段 	                 类型 	                      描述
		====================   ========   ================================================================================================
		terminal_ids 	        array 	   终端店数组集合
		name 	                string     活动名称
		start_time 	            number 	   活动开始时间
		end_time 	            number 	   活动结束时间
		limit_time 	            number 	   活动限制，（每个微信号享受优惠设置），0则不限制，1则限制仅享受一次
		conditions 	            array 	   活动条件（二维数组）
		  level 	            number 	   优惠条件层级
		  condition_min 	    number 	   优惠条件值
		  strategys 	        array 	   优惠设置（二维数组）
			reduction_type 	    number 	   减免类型）1.金额 2.打折 3.积分、4.包邮、5.送卡券、6.商城红包 7.现金红包
			point 	            number 	   选填，积分
			amount 	            number 	   选填，减免金额(最多两位小数，传值过来需100，例如：用户输入8.5，请求参数为8.5100即850 )
			discount 	        number 	   选填，打折(0-10区间 最多一位小数)，传值过来需10，例如：用户输入8.5，请求参数为8.510即85
			card_type_id 	    number 	   赠送卡券id
			cash_redpack_id 	number 	   赠送现金红包id
			red_packet_id 	    number 	   赠送商城红包id
			order_limit 	    number 	   订单使用限制 1.所以订单 2.适用于未使用卡券或红包优惠的订单
			is_limit 	        number 	   是否上不封顶）1、是 2、否
		====================   ========   ================================================================================================
        '''
        start_time = int(time.time()) - 3600
        end_time = start_time + 3600*24
        name = "分店收款码满减活动-" + time.strftime('%m%d%H%M',time.localtime(time.time()))
        #分店ID(分店收款码状态开启)
        terminal = self.conf.api.Terminal(self.conf)
        terminalPara = self.terminal_list()
        terminalListResp = terminal.terminal_list(terminalPara)
        terminalList = []
        for term in terminalListResp['errmsg']['data']:
            if term['shopSubSetting']['is_scan_pay'] == 1:
                terminalList.append(term['id'])
            
        #订单支付立享优惠
        #立减固定金额
        reductionType1 = {"reduction_type":1,"amount":2000,"is_limit":2}    
        #折扣
        reductionType2 = {"reduction_type":2,"discount":80}
        #订单完成后赠送
        #卡券
        reductionType3 = {"reduction_type":3,"point":"20","is_limit":2}
        #积分
        reductionType5 = {"reduction_type":5,"card_type_id":1168,"order_limit":1}
        conditionDic = {"level":1,"condition_min":15000,"strategys":[]}
        template = {"terminal":2,"terminal_ids":[],"name":name,"start_time":start_time,"end_time":end_time,"limit_time":1,"conditions":[conditionDic]}
        template['terminal_ids'].extend(terminalList)
        
        for key in args:
            if key =="reduction_type":
                if not((1 in args[key]) and (2 in args[key])):
                    for rtype in args[key]:
                        if rtype == 1:
                            conditionDic['strategys'].append(reductionType1)
                        elif rtype == 2:
                            conditionDic['strategys'].append(reductionType2)
                        elif rtype == 3:
                            conditionDic['strategys'].append(reductionType3)                
                        elif rtype == 5:
                            conditionDic['strategys'].append(reductionType5)
                else:
                    raise AssertionError("reduction_type 1 and reduction_type 2 should not both in args")
            elif key == "is_limit":
                if ( args[key] == 1 or args[key] == 2):
                    if 1 in args['reduction_type']:
                        reductionType1[key] = args[key]
                    if 3 in args['reduction_type']:
                        reductionType3[key] = args[key]   
                    if (1 not in args['reduction_type']) and (3 not in args['reduction_type']):
                        raise AssertionError("reduction_type类型错误，该类型无%s类型参数" % key)
                else:
                    raise AssertionError("%s参数值错误" % key)
            elif key ==  "terminal_ids":
                template['terminal_ids'] = []
                template['terminal_ids'].extend(args[key])                       
            elif key in reductionType1:
                reductionType1[key] = args[key]
            elif key in reductionType2:
                reductionType2[key] = args[key]
            elif key in reductionType3:
                reductionType3[key] = args[key]
            elif key in reductionType5:
                reductionType5[key] = args[key]
            elif key in conditionDic:
                conditionDic[key] = args[key]
            elif key in template:
                template[key] = args[key]
            else:
                raise AssertionError("参数名不存在!:%s" % key)
        return template
    
    def order_statistics(self,**args):
        '''
		=================  ========    ============================================================		
		  字段 	             类型 	               描述
		=================  ========    ============================================================
		 auto_get_params 	Number 	    是否禁止自动获取 agent_id 和 terminal_id，传值即不自动获取
		 _page 	Number 	
		 _page_size 	    Number 	
		 createStart 	    Number 	    开始时间
		 createEnd 	        Number 	    结束时间
		 statement 	        Number 	    非必填，对账单标志，生成终端店对账单需传1
		=================  ========    ============================================================		 
        '''
        #当前时间
        now = time.time()
        #当天凌晨
        midnight = now - (now % 86400) + time.timezone
        #昨天凌晨
        createStart = int(midnight - 86400)
        #昨天23.59.59
        createEnd = int(midnight - 1)
        template = {"_page":1,"_page_size":20,"createStart":createStart,"createEnd":createEnd,"auto_get_params":0,"newSortStr":{"num":3,"attrName":"id"},"keyword":""}
        return g.get_params(template, args)
    
    def aftersales_statistics(self,**args):
        '''
        =================  ========    ============================================================        
          字段                  类型                    描述
        =================  ========    ============================================================
         auto_get_params     Number         是否禁止自动获取 agent_id 和 terminal_id，传值即不自动获取
         _page     Number     
         _page_size         Number     
         createStart         Number         开始时间
         createEnd             Number         结束时间
         statement             Number         非必填，对账单标志，生成终端店对账单需传1
        =================  ========    ============================================================         
        '''
        now = time.time()
        midnight = now - (now % 86400) + time.timezone
        createStart = int(midnight - 86400)
        createEnd = int(midnight - 1)
        template = {"_page":1,"_page_size":20,"createStart":createStart,"createEnd":createEnd,"auto_get_params":0,"newSortStr":{"num":3,"attrName":"id"},"keyword":"","kind":1}
        return g.get_params(template, args)

    def member_statistics(self,**args):
        '''
        =================  ========    ============================================================        
          字段                  类型                    描述
        =================  ========    ============================================================
         auto_get_params     Number         是否禁止自动获取 agent_id 和 terminal_id，传值即不自动获取
         _page     Number     
         _page_size         Number     
         createStart         Number         开始时间
         createEnd             Number         结束时间
         statement             Number         非必填，对账单标志，生成终端店对账单需传1
        =================  ========    ============================================================         
        '''
        now = time.time()
        midnight = now - (now % 86400) + time.timezone
        createStart = int(midnight - 86400)
        createEnd = int(midnight - 1)
        template = {"_page":1,"_page_size":20,"createStart":createStart,"createEnd":createEnd,"auto_get_params":0,"newSortStr":{"num":3,"attrName":"id"},"keyword":"","kind":1}
        return g.get_params(template, args)
    
    def customer_statistics(self,**args):
        '''
        =================  ========    ============================================================        
          字段                  类型                    描述
        =================  ========    ============================================================
         auto_get_params     Number         是否禁止自动获取 agent_id 和 terminal_id，传值即不自动获取
         _page     Number     
         _page_size         Number     
         createStart         Number         开始时间
         createEnd             Number         结束时间
         statement             Number         非必填，对账单标志，生成终端店对账单需传1
        =================  ========    ============================================================         
        '''
        now = time.time()
        midnight = now - (now % 86400) + time.timezone
        createStart = int(midnight - 86400)
        createEnd = int(midnight - 1)
        template = {"_page":1,"_page_size":20,"createStart":createStart,"createEnd":createEnd,"auto_get_params":0,"newSortStr":{"num":3,"attrName":"id"},"keyword":"","kind":2}
        return g.get_params(template, args)
    
    def promotion_statistics(self,**args):
        '''
        =================  ========    ============================================================        
          字段                  类型                    描述
        =================  ========    ============================================================
         auto_get_params     Number         是否禁止自动获取 agent_id 和 terminal_id，传值即不自动获取
         _page     Number     
         _page_size         Number     
         createStart         Number         开始时间
         createEnd             Number         结束时间
         statement             Number         非必填，对账单标志，生成终端店对账单需传1
        =================  ========    ============================================================         
        '''
        now = time.time()
        midnight = now - (now % 86400) + time.timezone
        createStart = int(midnight - 86400)
        createEnd = int(midnight - 1)
        template = {"_page":1,"_page_size":20,"createStart":createStart,"createEnd":createEnd,"auto_get_params":0,"newSortStr":{"num":3,"attrName":"id"},"keyword":"","status":""}
        return g.get_params(template, args)
    
    def qrcode_detail(self,**kwargs):
        
        template = {"model":"terminal","model_id":109828}
        return g.get_params(template, kwargs)
    
    def statement_receive_setting(self,**kwargs):
        '''
	    ==============    =========      =======================
	        字段             类型             描述
	    ==============    =========      =======================
	     account_no         string           银行账号
	     due_bank           string           收款银行
	     opening_bank       string           开户行
	     payee              string           收款人姓名
	     shop_sub_id        string           分店ID
	     tel                string           联系电话   
	    ==============    =========      =======================	 
	    '''
        template = {"payee":"分店测试","due_bank":"招商银行","opening_bank":"招商银行科技园支行","account_no":"6225887856895623","tel":"0755-52658959","shop_sub_id":"109830"}
        return g.get_params(template, kwargs)
    
    def role_add(self,**kwargs):
        '''
        '''
        title = u"角色" + Utils.rand_str()
        template = {"title":title,"is_cancel":2}
        return g.get_params(template, kwargs)
    
    def save_role_function(self,**kwargs):
        '''
        '''
        template = {"ids":[589,607,608,610,611,955,969,970,1152,1154,1156,1193,1194,1195,590,591,592,593,594,1161,595,596,597,598,599,600,601,602,603,605,606,612,613,614,
                           820,616,617,620,621,622,624,625,626,628,643,644,645,646,647,743,649,651,650,744,629,906,1593,636,631,632,633,634,635,637,638,639,640,641,642,
                           1356,1457,1458,1459,1355,844,876,877,878,879,881,882,885,1460,1461,1464,1465,1463,1466,1467,652,653,976,655,1196,1198,1199,659,978,661,662,
                           1197,1200,1201,656,977,658],"auth_role_id":26586}
        return g.get_params(template, kwargs)
    
    def staff_add(self,**kwargs):
        '''
        '''
        usename = "员工" + Utils.rand_str()
        realname = "姓名" + Utils.rand_str()
        template = {"user_name":usename,"shop_sub_id":109828,"role_id":26583,"password":"123456","real_name":realname,"email":"test@snsshop.net","mobile":"15898565858"}
        return g.get_params(template, kwargs)
    
    def terminal_members_list(self,**kwargs):
        '''
		===================  ==========     =====================================================
		   字段 	            类型 	           描述
		===================  ==========     =====================================================
		 member_no 	           number 	      会员编号
		 keyword 	           string 	      关键字
		 source 	           number 	      来源
		 growth 	           number 	      成长值
		 status 	           number 	      状态）1：正常，2：冻结，3未绑定
		 is_get_card 	       number 	      是否领取会员卡）1：领取了，2：未领取
		 level 	               number 	      等级
		 member_group_id 	   number 	      分组id
		 wxUserInfos 	       number 	      以下是wxUserInfos的字段
		 sex 	               number 	      性别 1时是男性，值为2时是女性，值为3时是未知
		 birth 	               number 	      
		 nickname 	           string 	      昵称）最多45字符
		 headimgurl 	       string 	      头像）最多250字符
		 real_name 	           string 	      姓名）最多30字符
		 province 	           number 	      省）最多30字符
		 city 	               number 	      市）最多50字符
		 country 	           number 	      区）最多100字符
		 address 	           number 	      详细地址）最多100字符
		 email 	               number 	      邮箱）最多100字符
		 mobile 	           string 	      手机号
		 point 	               string 	      积分
		 memberGroup 	       number 	      以下是memberGroup的字段
		 name 	               string 	      分组名称
		 memberTagRelation 	   number 	      以下是memberTagRelation的字段
		   name 	           string 	      标签名称
		===================  ==========     =====================================================
        '''
        template = {"_page":1,"_page_size":20,"keyword":"","real_name":"","create_start":"","create_end":"","bind_mobile":"","status":[],"source":[],"level":[],
                    "member_group_id":[],"tags":[],"sex":[],"city_id":[],"city":[],"shop_sub_id":"109828","belong_to_staff_id":""}
        return g.get_params(template, kwargs)
    
    def members_last_count(self,**kwargs):
        '''
        '''
        template = {"create_start":"","create_end":"","shop_sub_id":"109828"}
        return g.get_params(template, kwargs)
        
    def terminal_member_list(self,**kwargs):
        '''
		===================  ==========     =====================================================
		   字段 	            类型 	           描述
		===================  ==========     =====================================================
		 member_no 	           number 	      会员编号
		 keyword 	           string 	      关键字
		 source 	           number 	      来源
		 growth 	           number 	      成长值
		 status 	           number 	      状态）1：正常，2：冻结，3未绑定
		 is_get_card 	       number 	      是否领取会员卡）1：领取了，2：未领取
		 level 	               number 	      等级
		 member_group_id 	   number 	      分组id
		 wxUserInfos 	       number 	      以下是wxUserInfos的字段
		 sex 	               number 	      性别 1时是男性，值为2时是女性，值为3时是未知
		 birth 	               number 	      
		 nickname 	           string 	      昵称）最多45字符
		 headimgurl 	       string 	      头像）最多250字符
		 real_name 	           string 	      姓名）最多30字符
		 province 	           number 	      省）最多30字符
		 city 	               number 	      市）最多50字符
		 country 	           number 	      区）最多100字符
		 address 	           number 	      详细地址）最多100字符
		 email 	               number 	      邮箱）最多100字符
		 mobile 	           string 	      手机号
		 point 	               string 	      积分
		 memberGroup 	       number 	      以下是memberGroup的字段
		 name 	               string 	      分组名称
		 memberTagRelation 	   number 	      以下是memberTagRelation的字段
		   name 	           string 	      标签名称
		===================  ==========     =====================================================
        '''
        template = {"_page":1,"_page_size":20,"nickname":"","group_id":None,"shop_sub_id":"109828","agent_id":"",
                    "is_search":False,"belong_to_staff_id":"","createStart":"","createEnd":"","group_ids":[],"yestoday":False,"user_platform":0,"tags":[]}
        return g.get_params(template, kwargs)
    
    def terminal_count_wx_member(self,**kwargs):
        '''
        '''
        template = {"agent_id":"","shop_sub_id":"109828","belong_to_staff_id":"","createStart":"","createEnd":""}
        return g.get_params(template, kwargs)

    def cancel_record_list(self,**kwargs):
        '''
        '''
        template = {"_page":1,"_page_size":10,"createStart":None,"createEnd":None,"cancel_type":None,"shop_sub_id":None,"auto_get_params":1}
        return g.get_params(template, kwargs)
    
    def shopsub_cancel_list(self,**kwargs):
        '''
        '''
        template = {"_page":1,"_page_size":10,"shop_sub_id":""}
        return g.get_params(template, kwargs)

    def staff_cancel_list(self,**kwargs):
        '''
        '''
        template = {"_page":1,"_page_size":10,"staff_id":""}
        return g.get_params(template, kwargs)
    
    def fx_member_list(self,**kwargs):
        '''
        '''
        template = {"_page":1,"_page_size":20,"typeId":None,"memberId":"","name":"","storeId":""}
        return g.get_params(template, kwargs)

    def fx_order_list(self,**kwargs):
        '''
        '''
        template = {"_page":1,"_page_size":20,"menberName":"","_status":"","orderId":"","terminal_id":"109828","createStart":"","createEnd":"","auto_get_params":0,"agent_id":"","staff_id":""}
        return g.get_params(template, kwargs)
    
    def order_list(self,**kwargs):
        '''
        '''
        template = {"_status":2,"after_sales_status":2,"pickup_type":None,"_page":1,"_page_size":20,"order_type":None,"s_tel":None,
                    "s_consignee":None,"createStart":None,"createEnd":None,"order_no":None,"pay_type":None,"should_pay_min":None,
                    "should_pay_max":None,"user_name":None,"express_type":None,"agent_id":None,"distribution_id":None,
                    "shop_sub_id":"109828","staff_id":None,"pay_time_start":None,"pay_time_end":None,"pickup_date_start":None,
                    "pickup_date_end":None,"consignor_status":None,"statement":None,"page":1}
        return g.get_params(template, kwargs) 
    
    def refund_list(self,**kwargs):
        '''
        '''
        template = {"_page":1,"_page_size":20,"createStart":"","createEnd":"","pay_type":"","order_type":"","type":"","processing_state":"",
                    "pickup_type":"","order_id":"","tel":"","consignee":"","order_no":"","user_phone":"","service_no":"","user_name":"",
                    "distribution_id":[],"shop_sub_id":[109828],"shop_staff_id":[]}
        return g.get_params(template, kwargs)