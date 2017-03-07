'''
Admin UI通用控件库
'''
import sys,time,random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .market import locators as LC
from ..generic import Generic
from .actions import Action
from selenium.webdriver.support.select import Select
from ..conf import *



class Common(Action):

    def __init__(self,conf):
        Action.__init__(self,conf)

    def click(self,name):
        '''
        点击
        '''
        self.G.click(self.conf.wxdriver,LC.COMMON[name])



    def top_menu(self, menu):
        '''主菜单菜单'''
        driver = self.conf.driver
        driver.implicitly_wait(10)
        time.sleep(2)
        xpath = LC.MAIN_MENU[menu]
        element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(xpath=xpath))
        time.sleep(2)
        element.click()
        time.sleep(1)

    def shop_menu(self, menu):
        '''微店铺菜单'''
        driver = self.conf.driver
        driver.implicitly_wait(10)
        time.sleep(2)
        xpath = LC.SHOP_MENU[menu]
        element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(xpath=xpath))
        time.sleep(2)
        element.click()
        time.sleep(1)

    def members_menu(self, menu):
        '''微会员菜单'''
        driver = self.conf.driver
        driver.implicitly_wait(10)
        time.sleep(2)
        xpath = LC.MEMBERS_MENU[menu]
        element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(xpath=xpath))
        time.sleep(2)
        element.click()
        time.sleep(1)

    def market_menu(self, menu):
        '''微营销菜单'''
        driver = self.conf.driver
        driver.implicitly_wait(10)
        time.sleep(2)
        xpath = LC.MARKET_MENU[menu]
        element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(xpath=xpath))
        time.sleep(2)
        element.click()
        time.sleep(1)

    def terminal_menu(self, menu):
        '''微分店菜单栏'''
        driver = self.conf.driver
        driver.implicitly_wait(10)
        time.sleep(2)
        xpath = LC.TERMINAL_MENU[menu]
        element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(xpath=xpath))
        time.sleep(2)
        element.click()
        time.sleep(1)



    def choose_starttime(self, key):
        '''选择开始时间'''
        driver = self.conf.driver
        driver.implicitly_wait(10)
        xpath = LC.COMMON[key]
        starttime = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(xpath=xpath))
        time.sleep(2)
        starttime.click()
        time.sleep(1)
        driver.switch_to.frame(driver.find_element_by_xpath(xpath="//iframe[@hidefocus='true']"))
        # 选择开始的月份
        startmonth = WebDriverWait(driver, 10).until( lambda x: x.find_element_by_xpath(xpath='//*[@id="dpTitle"]/div[6]/a'))
        time.sleep(1)
        startmonth.click()
        # 选择开始的日期
        startdata = WebDriverWait(driver, 10).until( lambda x: x.find_element_by_xpath(xpath='/html/body/div/div[3]/table/tbody/tr[3]/td[2]'))
        time.sleep(1)
        startdata.click()
        sure = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(xpath='//*[@id="dpOkInput"]'))
        sure.click()
        time.sleep(1)
        driver.switch_to.default_content()
        time.sleep(2)

    def choose_endtime(self, key):
        '''选择结束时间'''
        driver = self.conf.driver
        driver.implicitly_wait(10)
        xpath = LC.COMMON[key]
        endtime = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(xpath=xpath))
        time.sleep(2)
        endtime.click()
        time.sleep(2)
        driver.switch_to.frame(driver.find_element_by_xpath(xpath="//iframe[@hidefocus='true']"))
        time.sleep(1)
        # 选择结束的月份
        endmonth = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(xpath='//*[@id="dpTitle"]/div[6]/a'))
        endmonth.click()
        time.sleep(1)
        # 选择结束的日期
        enddata = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(xpath='/html/body/div/div[3]/table/tbody/tr[3]/td[5]'))
        enddata.click()
        time.sleep(1)
        sure = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(xpath='//*[@id="dpOkInput"]'))
        sure.click()
        driver.switch_to.default_content()
        time.sleep(2)

    def choose_product(self, key):
        '''选择商品'''
        index = None
        driver = self.conf.driver
        driver.implicitly_wait(10)
        xpath = LC.COMMON[key]
        # 点击选择商品的按钮
        ele1 = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(xpath=xpath))
        time.sleep(0.5)
        ele1.click()
        # 选择商品列表中的商品
        # import pdb pdb.set_trace()
        els = driver.find_elements_by_xpath(xpath='//tr[@ng-click="showChild(list, $index)"]')
        # eles = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,'//tr[@ng-click="showChild(list, $index)"]')))
        time.sleep(1)
        if index == None:
            index = random.randrange(0, len(els))
        time.sleep(1)
        els[index].click()
        time.sleep(1)
        index1 = index + 1
        time.sleep(0.5)
        # 选择商品的第一个商品规格
        # import pdb pdb.set_trace()
        xpath1 = '//*[@id="product"]/div[1]/table/tbody[' + str(index1) + ']/tr[2]/td/table/tbody/tr[2]'
        ele2 = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(xpath=xpath1))
        time.sleep(1)
        ele2.click()
        # 点击确定按钮
        sure = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(xpath='//a[@ng-click="save()"]'))
        time.sleep(1)
        sure.click()
        time.sleep(2)
        '''
    def choose_page(self,key):
        分页操作
        pange_number=15        #每页展示的数据，默认是15条
        driver = self.conf.driver
        driver.implicitly_wait(10)
        # 获取分页的数量
        xpath = LC.COMMON[key]
        pages=driver.find_elements_by_xpath(xpath=xpath)
        total_pages=len(pages)
        time.sleep(1)
        for page in pages:
            page.click()
            time.sleep(1)
            '''

    def get_matching_xpath_count(self,xpath):
        '''
        获取xpath个数
        '''
        return (super(Common, self).get_matching_xpath_count(xpath))

    def choose_page(self, key):
        '''分页操作'''
        pange_number = 15  # 每页展示的数据，默认是15条
        driver = self.conf.driver
        driver.implicitly_wait(10)
        # 获取分页的数量
        xpath = LC.COMMON[key]
        # 页面总数所在的xpath的路径值
        totle = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath))).text
        totles = int(totle)
        print('totles  is :', totles)
        # 计算页数
        pages = int(totles / pange_number)
        sum0 = driver.find_elements_by_xpath(xpath="//tr[@class='ng-scope']")
        sum = len(sum0)
        time.sleep(1)
        i = 0
        for i in range(0, pages):
            # import pdb
            # pdb.set_trace()
            xpath1 = '//*[@id="main-container"]/div[1]/div[2]/div[2]/div/div/div[4]/ul[1]/li[8]/a'
            ele2 = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(xpath=xpath1))
            ele2.click()
            time.sleep(0.5)
            count0 = driver.find_elements_by_xpath(xpath="//tr[@class='ng-scope']")
            count = len(count0)
            sum = sum + count
            time.sleep(0.5)
            print('sum  is :', sum)
            i = i + 1
        time.sleep(0.5)
        assert sum == totles, "列表总数不正确，分页校验失败"
        print("总条数:%s,页数:%s" % (totles,pages))
        print('列表总数正确，分页校验成功')
















    def choose_picture(self, key):
        '''选择图片'''
        index = None
        driver = self.conf.driver
        driver.implicitly_wait(10)
        # 点击上传图片的地址
        xpath = LC.COMMON[key]
        ele1 = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(xpath=xpath))
        time.sleep(5)
        ele1.click()
        # 任意选择一张图片
        xpath1 = '//a[@ng-click="imageChoose($index, list)"]'
        time.sleep(1)
        # els = WebDriverWait(driver, TIME_OUT).until(EC.presence_of_all_elements_located((By.XPATH, xpath1)))
        els = driver.find_elements_by_xpath(xpath=xpath1)
        if index == None:
            index = random.randrange(0, len(els))
        # import pdb;pdb.set_trace()
        time.sleep(1)
        els[index].click()
        time.sleep(1)
        # 点击确定按钮
        xpath2 = '//*[@id="submitImage"]'
        sure = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(xpath=xpath2))
        time.sleep(1)
        sure.click()
        time.sleep(1)

    def select_button(self, key):
        '''
        运费策略
        '''
        driver = self.conf.driver
        driver.implicitly_wait(10)
        xpath = LC.COMMON[key]
        value = ["0", "1", "2", "3"]
        value0 = random.choice(value)
        number = random.randint(50, 200)
        time.sleep(1)
        ele = Select(driver.find_element_by_xpath(xpath=xpath))
        ele.select_by_value(value0)
        time.sleep(1)
        if value0 == "2":
            # 输入订单的满减金额
            xpath1 = '//*[@id="rule"]/form/div[6]/div/input'
            ele1 = WebDriverWait(driver, 20).until(lambda x: x.find_element_by_xpath(xpath=xpath1))
            time.sleep(1)
            ele1.send_keys(number)
            time.sleep(1)
        elif value0 == "3":
            # 输入订单的满减金额
            xpath2 = '//*[@id="rule"]/form/div[7]/div/input'
            ele1 = WebDriverWait(driver, 20).until(lambda x: x.find_element_by_xpath(xpath=xpath2))
            time.sleep(1)
            ele1.send_keys(number)
            time.sleep(0.5)
        else:
            time.sleep(0.5)















