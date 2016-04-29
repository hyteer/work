# encoding: utf-8
import unittest
import time
from selenium import webdriver
from args import global_args, elements

g = global_args
e = elements

class zfmsForm(unittest.TestCase):
    def setUp(self):
        # create a new firefox session
        self.driver = webdriver.Firefox()
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get(g.HOME)
        driver.find_element_by_name('username').clear()
        driver.find_element_by_name('username').send_keys(g.username)
        driver.find_element_by_name('password').clear()
        driver.find_element_by_name('password').send_keys(g.password)
        driver.find_element_by_link_text('登录').click()
        url = self.driver.current_url
        print "Url: ",self.driver.current_url
        self.assertEqual('http://192.168.31.237:8090/bw_sms/platform/console/main.ht',url)
        print "Login successfully."
        time.sleep(2)

    def test_process(self):
        driver = self.driver
        driver.find_element_by_id('80').click()
        str_process = driver.find_element_by_id('leftTree_1_span').text
        print "Assert Text: ",str_process
        self.assertEqual(u'表单管理', str_process)

        # 添加表
        driver.find_element_by_id('leftTree_2_span').click()
        time.sleep(2)
        driver.switch_to.frame('83')
        driver.find_element_by_xpath(e.add).click()

        # 输入表信息
        driver.find_element_by_id('comment').send_keys('Test table1')
        tbName = driver.find_element_by_id('name')
        tbName.clear()
        tbName.send_keys('auto_test_table1')
        driver.find_element_by_xpath("//label[contains(text(),'主表')]/input").click()

        # 添加列
        driver.find_element_by_xpath("//div[@class='panel-toolbar']//a[@onclick='clickAddRow()']").click()
        driver.switch_to.parent_frame()
        pop_frame = driver.find_element_by_xpath("//div[@ligeruiid='Dialog1001']//iframe")
        driver.switch_to.frame(pop_frame)
        driver.find_element_by_id('fieldDesc').send_keys('test field remark')
        fieldName = driver.find_element_by_id('fieldName')
        fieldName.clear()
        fieldName.send_keys('com_name')
        time.sleep(1)
        driver.find_element_by_id('dataFormSave')
        driver.find_elements_by_xpath("//div[@class='panel-toolbar']//a[@onclick='dialog.close();']")





    def tearDown(self):
        print "Test finished successfully."
        time.sleep(4)
        #self.driver.quit()



'''
class zfmsProcess(unittest.TestCase):
    def setUp(self):
        login = zfmsLogin(self)
        login.setUp()
        self.driver = webdriver.Firefox()

    def tempTest(self):
        driver = webdriver.Firefox()
        driver.find_element_by_name('username').clear()
        driver.find_element_by_name('username').send_keys('tony')
        driver.find_element_by_name('password').clear()
        driver.find_element_by_name('password').send_keys('sa')
        driver.find_element_by_link_text('登录').click()

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
        '''


if __name__ == "__main__":
    unittest.main(verbosity=2)








