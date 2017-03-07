# -*- coding: utf-8 -*- 

import pytest,time,random
from selenium import webdriver

class TestTerminalList(object):
    
    @pytest.fixture(autouse=True)
    def setup(self,conf):
        self.conf = conf
        self.terminal = conf.ui.admin.terminal.Terminal(conf)
        self.terminalparam = conf.param.TerminalParam(conf)
        self.terminalAPI = conf.api.Terminal(conf)
        self.driver = webdriver.Chrome()
        conf.COMMON.login(conf,self.driver)
        #切换至分店类别页面
        self.terminal.terminal_manage.click_link('微分店')
        self.terminal.terminal_manage.click_link('微分店')
        self.terminal.terminal_manage.click_link('分店列表')
    
    def test_shopsub_info(self):
        terminal = self.terminal.terminal_manage
        #接口获取分店列表
        param = self.terminalparam.terminal_list()
        terminalResp = self.terminalAPI.terminal_list(param)
        terminalList = terminalResp['errmsg']['data']
        terminalNum = len(terminalList)
        #获取页面显示分店数
        pageTerminalNum = terminal.get_matching_xpath_count('分店名称')
        assert terminalNum == pageTerminalNum
        
        terminal.check_terminal_info(terminalList)
        self.driver.close()
        
    def test_shopsub_status(self):
        terminal = self.terminal.terminal_manage
        #随机获取分店
        count = terminal.get_matching_xpath_count('分店名称')
        terminalIndex = random.randint(1,count)
        #获取分店营业状态
        businessStatus = terminal.get_terminal_status(terminalIndex)
        print('分店状态:',businessStatus)
        #切换分店营业状态
        terminal.switch_terminal_status(terminalIndex,businessStatus)
        #恢复分店营业状态
        originalStatus = not businessStatus
        terminal.switch_terminal_status(terminalIndex,originalStatus)
        self.driver.close()
        
    def test_shop_search(self):
        terminal = self.terminal.terminal_manage
        #随机获取分店名称
        count = terminal.get_matching_xpath_count('分店名称')
        terminalIndex = random.randint(1,count)
        shopName = terminal.get_text('分店名称',terminalIndex)
        #输入分店名称
        terminal.input('分店名称搜索输入框',shopName)
        #搜索
        terminal.click("分店搜索按钮")
        time.sleep(3)
        #搜索结果校验
        searchCount = terminal.get_matching_xpath_count('分店名称')
        assert searchCount == 1
        searchShopName = terminal.get_text('分店名称')
        assert searchShopName == shopName
        self.driver.close()
        
    def test_add_shop(self):
        terminal = self.terminal.terminal_manage
        terminal.click_link("新建分店")
        #分店名称
        timeStr = time.strftime("%m%d%H%M",time.localtime())
        shopName = timeStr + "分店"
        terminal.input('分店名称输入框',shopName)
        #管理员账号
        userName = self.conf.Utils.rand_str()
        terminal.input('管理员账号输入框',userName)
        #管理员密码
        terminal.input('管理员密码输入框','123456')
        #管理员姓名
        realName = self.conf.Utils.rand_name()
        terminal.input('管理员姓名输入框',realName)
        #微信店铺分类
        lableList1 = terminal.get_select_list_items('微信店铺一级分类选择框')
        print("lables:",lableList1)
        randomIndex1 = random.randint(1,len(lableList1)-1)
        print("random int:",randomIndex1)
        terminal.select_from_list_by_index('微信店铺一级分类选择框',randomIndex1)
        time.sleep(1)
        lableList2 = terminal.get_select_list_items('微信店铺二级分类选择框')
        print("lables:",lableList2)
        randomIndex2 = random.randint(1,len(lableList2)-1)
        print("random int:",randomIndex2)
        terminal.select_from_list_by_index('微信店铺二级分类选择框',randomIndex2)
        time.sleep(1)
        lableList3 = terminal.get_select_list_items('微信店铺三级分类选择框')
        print("lables:",lableList3)
        if len(lableList3) > 1:
            randomIndex3 = random.randint(1,len(lableList3)-1)
            print("random int:",randomIndex3)
            terminal.select_from_list_by_index('微信店铺三级分类选择框',randomIndex3)
        #所属商圈
        provinceList = terminal.get_select_list_items('所属商圈省选择框')
        provinceRandom = random.randint(1,len(provinceList)-1)
        terminal.select_from_list_by_index('所属商圈省选择框',provinceRandom)
        time.sleep(1)
        cityList = terminal.get_select_list_items('所属商圈市选择框')
        cityRandom = random.randint(0,len(cityList)-1)
        terminal.select_from_list_by_index('所属商圈市选择框',cityRandom)
        time.sleep(1)
        districtList = terminal.get_select_list_items('所属商圈区选择框')
        districtRandom = random.randint(0,len(districtList)-1)
        terminal.select_from_list_by_index('所属商圈区选择框',districtRandom)
        time.sleep(1)
        circleList = terminal.get_select_list_items('所属商圈选择框')
        circleRandom = random.randint(0,len(circleList)-1)
        terminal.select_from_list_by_index('所属商圈选择框',circleRandom)
        time.sleep(1)
        #营业时间
        weekNum = random.randint(1,7)
        weekList = random.sample([1,2,3,4,5,6,7],weekNum)
        for week in weekList:
            terminal.click("营业时间周",week)
        #电话
        phoneNumber = self.conf.Utils.rand_mobile()
        terminal.input('分店电话输入框',phoneNumber)
        #支持配送
        terminal.click('快递配送选择框')
        terminal.click('买家自提选择框')
#         terminal.click('同城配送选择框')
        #网址
        terminal.input('店铺网址输入框','''http://www.sctek.com''')
        #店铺背景
        terminal.click('店铺背景图片选择')
        time.sleep(1)
        terminal.select_image()
        #店铺logo
        terminal.click('店铺log图片选择')
        time.sleep(1)
        terminal.select_image()
        #人均消费
        averagePrice = str(random.randint(50,300))
        terminal.input('人均消费输入框',averagePrice)
        #特色推荐
        terminal.input('特色推荐输入框','特色推荐')
        #特色服务
        terminal.input('特色服务输入框','特色服务')
        #商家描述
        terminal.input('商家描述输入框','商家描述')
        #详细地址
        terminal.input('详细地址输入框','广东省深圳市南山区科技园比克科技大厦')
        #门店定位图
        terminal.input('门店地图定位输入框','深圳市南山区')
        #门店地图定位搜索
        terminal.click('门店地图定位搜索按钮')
        #点击保存
#         terminal.click('门店保存按钮')
        self.driver.close()