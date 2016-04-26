# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class LocalPost(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/wp"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_local_post(self):
        driver = self.driver
        driver.get(self.base_url + "/?gws_rd=ssl")
        driver.find_element_by_id("lst-ib").clear()
        driver.find_element_by_id("lst-ib").send_keys("github")
        driver.find_element_by_link_text(u"How people build software · GitHub").click()
        driver.find_element_by_name("s").clear()
        driver.find_element_by_name("s").send_keys("test")
        driver.find_element_by_css_selector("button.search-submit").click()
        driver.find_element_by_link_text(u"继续阅读“Test-Products”").click()
        driver.find_element_by_id("comment").clear()
        driver.find_element_by_id("comment").send_keys("Hello1..")
        driver.find_element_by_id("author").clear()
        driver.find_element_by_id("author").send_keys("test1")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("test@qq.com")
        driver.find_element_by_id("submit").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
