# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import random
import string
import random

g = lambda a, b : "".join(random.sample(string.letters, a)) + "".join(random.sample(string.digits, b))

randomTxt = g(5,9)
print randomTxt

class WpPost(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(8)
        self.base_url = "http://localhost/wp"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_wp_post(self):
        driver = self.driver
        driver.get(self.base_url + "/wp/")
        driver.find_element_by_name("s").clear()
        driver.find_element_by_name("s").send_keys("test")
        driver.find_element_by_css_selector("button.search-submit").click()
        driver.find_elements_by_class_name("more-link")[0].click()
        driver.find_element_by_id("comment").clear()
        driver.find_element_by_id("comment").send_keys(randomTxt)
        author = driver.find_element_by_id("author")
        email = driver.find_element_by_id("email")
        author.clear()
        email.clear()
        author.send_keys(randomTxt)
        email.send_keys(randomTxt + "@qq.com")

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
     #   self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
