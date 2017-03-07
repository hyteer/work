import time,random
import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert


class TestSecondKill:


    '''
    测试UI库微营销模块_秒杀活动
    '''
    AUTHOR = 'xz'
    activity_name=u"【秒杀活动】" + ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5))
    newname=u"【修改秒杀活动】" + ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5))


    @pytest.fixture(autouse=True)
    def setup(self, conf):
        self.conf = conf
        self.admin = conf.ui.Admin(conf)
        self.sales = conf.ui.admin.market.SalesActivity(conf)
        self.second_killAPI = conf.api.Market(conf)
        self.second_killparam=conf.param.Market(conf)
        self.LC = self.admin.market.LOCATOR
        driver = webdriver.Chrome()
        self.driver = driver
        conf.COMMON.login(conf, driver)




    def test_second_kill_info(self):
        '''
        用例：秒杀活动页面校验
        '''
        self.admin.common.top_menu('微营销')
        secondResponse = self.second_killAPI.second_kill_list()
        secondkillList = secondResponse['errmsg']['data']
        print("second kill list:",secondkillList)
        second_killNum = len(secondkillList)
        print('second_killNum:',second_killNum)
        # 获取页面显示活动数
        pageSecond_killNum = self.sales.get_matching_xpath_count('活动类型栏')
        print('pageSecond_killNum:',pageSecond_killNum)
        assert second_killNum == pageSecond_killNum
        self.sales.check_second_kill_info(secondkillList)
        #分页操作
        self.admin.common.choose_page("页面总条数")
        self.driver.close()



    def test_second_kill_add(self):
        '''
        用例:秒杀活动添加
        '''
        click =self.sales.click
        input= self.sales.input
        choose=self.sales.choose
        get_text=self.sales.get_text
        self.admin.common.top_menu('微营销')
        #self.common.market_menu("秒杀活动")
        time.sleep(1)
        click("添加活动")
        choose("选择秒杀活动模板")
        #input("图文标题",u"图文标题-"+self.conf.Utils.rand_str())
        self.admin.market.common.input("图文标题", u"图文标题-" + self.conf.Utils.rand_str())
        self.admin.market.common.input("摘要内容",u"摘要内容-"+self.conf.Utils.rand_str())
        self.admin.common.choose_picture("活动图片")
        self.admin.market.common.click("下一步")
        self.admin.market.common.input("活动名称", self.activity_name)
        self.admin.market.common.input("活动说明", u"活动说明。。。。"+self.conf.Utils.rand_str())
        self.admin.common.choose_starttime("活动开始时间")
        self.admin.common.choose_endtime("活动结束时间")
        self.admin.common.select_button("运费策略")
        time.sleep(0.5)
        self.admin.common.choose_product("选择商品按钮")
        self.admin.market.common.input("活动价", random.randint(1,100))
        self.admin.market.common.input("配额", random.randint(10,100))
        self.admin.market.common.input("每人限购", random.randint(1,10))
        time.sleep(1)
        self.admin.market.common.click("保存")
        time.sleep(1)
        self.driver.switch_to_alert().accept()
        #活动类型的选择
        self.sales.select_checkbox()
        self.admin.market.common.input("分享标题",u"分享标题-"+self.conf.Utils.rand_str())
        self.admin.market.common.input("分享描述", u"分享描述-" + self.conf.Utils.rand_str())
        time.sleep(0.5)
        self.admin.common.choose_picture("分享图标")
        self.admin.market.common.click("保存并关闭")
        time.sleep(1)
        self.driver.switch_to_alert().accept()
        time.sleep(1)
        #页面校验
        activity_name1 = get_text('秒杀活动名称')
        time.sleep(0.5)
        assert self.activity_name==activity_name1,u"添加秒杀活动失败"
        print("添加秒杀活动成功")
        time.sleep(1)
        self.driver.close()


    def test_second_kill_status(self):
        '''
        用例:开启和关闭秒杀活动
        '''
        click = self.sales.click
        self.admin.common.top_menu('微营销')
        #开启活动
        click("状态",self.activity_name)
        time.sleep(0.8)
        self.driver.switch_to_alert().accept()
        time.sleep(0.8)
        #关闭活动
        click("状态", self.activity_name)
        time.sleep(0.8)
        self.driver.switch_to_alert().accept()
        self.driver.close()




    def test_second_kill_edit(self):
        '''
        用例: 秒杀活动编辑
        '''
        #执行用例
        click =self.sales.click
        input= self.sales.input
        choose=self.sales.choose
        get_text=self.sales.get_text
        self.admin.common.top_menu('微营销')
        #self.common.market_menu("秒杀活动")
        click("编辑秒杀活动",self.activity_name)
        self.admin.market.common.input("图文标题", u"图文标题-" + self.conf.Utils.rand_str())
        self.admin.market.common.input("摘要内容", u"摘要内容-" + self.conf.Utils.rand_str())
        self.admin.common.choose_picture("活动图片")
        self.admin.market.common.click("下一步")
        self.admin.market.common.input("活动名称", self.newname)
        self.admin.market.common.input("活动说明", u"活动说明。。。。" + self.conf.Utils.rand_str())
        self.admin.common.choose_starttime("活动开始时间")
        self.admin.common.choose_endtime("活动结束时间")
        self.admin.common.select_button("运费策略")
        time.sleep(0.5)
        click("编辑商品")
        self.admin.market.common.input("活动价", random.randint(1, 100))
        self.admin.market.common.input("配额", random.randint(10, 50))
        self.admin.market.common.input("每人限购", random.randint(1, 10))
        time.sleep(1)
        self.admin.market.common.click("保存")
        time.sleep(1)
        self.driver.switch_to_alert().accept()
        # 活动类型的选择
        self.sales.select_checkbox()
        # 活动主页面的编辑
        self.admin.market.common.input("分享标题", u"分享标题-" + self.conf.Utils.rand_str())
        self.admin.market.common.input("分享描述", u"分享描述-" + self.conf.Utils.rand_str())
        time.sleep(0.5)
        self.admin.market.common.click("保存并关闭")
        time.sleep(1)
        self.driver.switch_to_alert().accept()
        time.sleep(1)
        # 页面校验
        #获取修改后的活动名称
        activity_name1 = get_text('修改后秒杀活动名称',self.newname)
        assert self.newname == activity_name1, u"添加秒杀活动失败"
        print("添加秒杀活动成功")
        time.sleep(1)
        self.driver.close()


    def test_second_kill_check(self):

        '''
        用例：
        查看秒杀活动的日志
        查看秒杀活动的二维码
        '''
        click = self.sales.click
        get_text = self.sales.get_text
        self.admin.common.top_menu('微营销')
        #查看活动日志
        click("查看日志按钮",self.newname)
        time.sleep(2)
        note=get_text('操作日志页面')
        assert note=="操作日志","查看操作日志页面校验失败"
        print("查看操作日志校验成功")
        time.sleep(0.5)
        self.driver.back()
        #查看二维码
        now_handle=self.driver.current_window_handle   #获取当前窗口的句柄
        click("查看二维码按钮", self.newname)
        all_handles=self.driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                self.driver.switch_to_window(handle)
                erweimaPage = get_text('二维码页面')
                guishu = get_text('二维码归属')
                assert erweimaPage == "二维码","二维码页面校验失败"
                print("二维码页面校验成功")
                assert guishu == "自动化测试分店","二维码归属栏校验失败"
                print("二维码归属栏校验成功")
                time.sleep(1)
                click("查看二维码")
                time.sleep(3)
                click("关闭二维码")
                time.sleep(1)
                self.driver.close()
        time.sleep(1)
        self.driver.switch_to_window(now_handle)  # 返回主窗口
        time.sleep(1)
        self.driver.close()



    def test_second_kill_del(self):
        '''
        用例:删除秒杀活动
        '''
        # 执行用例
        driver = self.driver
        click = self.sales.click
        self.admin.common.top_menu('微营销')
        click("删除秒杀活动",self.newname)
        time.sleep(1)
        click("删除")
        self.driver.switch_to_alert().accept()
        time.sleep(2)
        assert self.newname not in "活动名称栏","删除秒杀活动失败"
        print("删除秒杀活动成功")
        time.sleep(1)



































