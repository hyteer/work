# coding: utf-8
"""
wsh后台菜单栏测试
"""

import time
from selenium import webdriver
import pytest



class TestMenu:

    AUTHOR = 'xz'


    @pytest.fixture(autouse=True)
    def setup(self, conf):
        self.conf = conf
        self.ui = conf.ui
        self.admin = conf.ui.admin.Market(conf)
        self.common = conf.ui.admin.Common(conf)
        self.LC = self.admin.LOCATOR
        driver = webdriver.Chrome()
        self.driver = driver
        conf.COMMON.login(conf, driver)
        return conf



    #主菜单菜单
    def test_wsh_menu(self):
        self.common.top_menu('公众号')
        self.common.top_menu('微店铺')
        self.common.top_menu('微会员')
        self.common.top_menu('微营销')
        self.common.top_menu('微杂志')
        self.common.top_menu('微推广')
        self.common.top_menu('微分店')
        self.common.top_menu('代理商')
        self.common.top_menu('微渠道')
        self.common.top_menu('微硬件')
        self.common.top_menu('数据中心')
        self.common.top_menu('一品一码')
        self.common.top_menu('社交广告')
        self.common.top_menu('我的微客多')
        self.driver.close()



    #微店铺菜单
    def test_shop_menu(self):
        self.common.top_menu('微店铺')
        self.common.shop_menu('页面管理')
        self.common.shop_menu('页面分类')
        self.common.shop_menu('店铺导航')
        self.common.shop_menu('商品库')
        self.common.shop_menu('商品分类')
        self.common.shop_menu('商品规格')
        self.common.shop_menu('商品评论')
        self.common.shop_menu('所有订单')
        self.common.shop_menu('售后订单')
        time.sleep(1)
        self.driver.find_element_by_xpath(xpath="//*[@id='main-container']/div[3]/div[2]/div/div[2]/div[2]").click()
        time.sleep(2)
        self.common.shop_menu('交易设置')
        self.common.shop_menu('快递配送')
        self.common.shop_menu('到店自提')
        self.common.shop_menu('地址库')
        self.common.shop_menu('订单统计')
        self.driver.close()


    #微会员菜单
    def test_members_menu(self):
        self.common.top_menu('微会员')
        self.common.members_menu('客户列表')
        self.common.members_menu('客户分组')
        self.common.members_menu('标签管理')
        self.common.members_menu('会员概况')
        self.common.members_menu('会员列表')
        self.common.members_menu('实体店会员')
        self.common.members_menu('会员分组')
        self.common.members_menu('会员消费记录')
        self.common.members_menu('会员卡设置')
        self.common.members_menu('开卡优惠')
        self.common.members_menu('成长值管理')
        self.common.members_menu('等级管理')
        self.common.members_menu('会员通知')
        self.common.members_menu('扫码开卡')
        self.common.members_menu('充值策略')
        self.common.members_menu('会员账户交易流水')
        self.common.members_menu('账户交易统计图')
        self.common.members_menu('会员折扣')
        js='''var evaluator = new XPathEvaluator();var result = evaluator.evaluate('//a[@href="/members/member-card-statistics"]', document.documentElement, null,XPathResult.ORDERED_NODE_ITERATOR_TYPE, null); var node = result.iterateNext();node.scrollIntoView();'''
        self.driver.execute_script(js)
        time.sleep(1)
        self.common.members_menu('节日关怀')
        js='''var evaluator = new XPathEvaluator();var result = evaluator.evaluate('//a[@href="/members/member-card-statistics"]', document.documentElement, null,XPathResult.ORDERED_NODE_ITERATOR_TYPE, null); var node = result.iterateNext();node.scrollIntoView();'''
        self.driver.execute_script(js)
        time.sleep(1)
        self.common.members_menu('生日关怀')
        js='''var evaluator = new XPathEvaluator();var result = evaluator.evaluate('//a[@href="/members/member-card-statistics"]', document.documentElement, null,XPathResult.ORDERED_NODE_ITERATOR_TYPE, null); var node = result.iterateNext();node.scrollIntoView();'''
        self.driver.execute_script(js)
        time.sleep(1)
        self.common.members_menu('积分流水记录')
        js='''var evaluator = new XPathEvaluator();var result = evaluator.evaluate('//a[@href="/members/member-card-statistics"]', document.documentElement, null,XPathResult.ORDERED_NODE_ITERATOR_TYPE, null); var node = result.iterateNext();node.scrollIntoView();'''
        self.driver.execute_script(js)
        time.sleep(1)
        self.common.members_menu('会员新增趋势')
        js='''var evaluator = new XPathEvaluator();var result = evaluator.evaluate('//a[@href="/members/member-card-statistics"]', document.documentElement, null,XPathResult.ORDERED_NODE_ITERATOR_TYPE, null); var node = result.iterateNext();node.scrollIntoView();'''
        self.driver.execute_script(js)
        time.sleep(1)
        self.common.members_menu('消费分层统计')
        js='''var evaluator = new XPathEvaluator();var result = evaluator.evaluate('//a[@href="/members/member-card-statistics"]', document.documentElement, null,XPathResult.ORDERED_NODE_ITERATOR_TYPE, null); var node = result.iterateNext();node.scrollIntoView();'''
        self.driver.execute_script(js)
        time.sleep(1)
        self.common.members_menu('会员卡投放统计')
        self.driver.close()





    #微营销菜单
    def test_market_menu(self):
        self.common.top_menu('微营销')
        self.common.market_menu('秒杀活动')
        self.common.market_menu('拼团活动')
        self.common.market_menu('满减包邮')
        self.common.market_menu('众筹活动')
        self.common.market_menu('大转盘')
        self.common.market_menu('砸金蛋')
        self.common.market_menu('现金红包')
        self.common.market_menu('记忆翻翻看')
        self.common.market_menu('丘比特之箭')
        self.common.market_menu('积分活动')
        self.common.market_menu('商城红包')
        self.common.market_menu('卡券活动')
        self.common.market_menu('节日礼包')
        self.common.market_menu('购物礼包')
        self.common.market_menu('预约活动')
        self.common.market_menu('摇电视')
        self.common.market_menu('签到活动')
        self.common.market_menu('祝福墙')
        self.driver.close()

    #微分店菜单
    def test_terminal_menu(self):
        self.common.top_menu('微分店')
        self.common.terminal_menu('分店列表')
        self.common.terminal_menu('基础设置')
        self.common.terminal_menu('商品管理')
        self.common.terminal_menu('分店通用首页')
        self.common.terminal_menu('分店码推送策略')
        self.common.terminal_menu('员工码推送策略')
        self.common.terminal_menu('分店收款码')
        self.common.terminal_menu('员工收款码')
        self.common.terminal_menu('结算报表')
        self.common.terminal_menu('结算设置')
        self.common.terminal_menu('分店收款码满减送')
        self.common.terminal_menu('员工收款码满减送')
        self.common.terminal_menu('订单统计')
        self.common.terminal_menu('售后统计')
        self.common.terminal_menu('会员统计')
        self.common.terminal_menu('客户统计')
        self.common.terminal_menu('推广统计')
        self.driver.close()
