'''Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import HtmlTestRunner

class pukk(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="C:\\Python\\chrome_driver\\chromedriver.exe")
        cls.driver.get("../index.html")

    def test_loginCMS(self):

        self.driver.implicitly_wait(5)
        
        #LOGIN
        
        self.user = self.driver.find_element_by_id("user")
        self.password = self.driver.find_element_by_id("password")
        self.submit = self.driver.find_element_by_id("login_btn")
        
        self.user.send_keys("something@something.hu")
        self.password.send_keys("PASSWORD")
        self.submit.click()
        
        #LOGIN END

    '''def test_selectVG(self):

        self.driver.implicitly_wait(5)
        
        #selectVG

        #self.driver.get("http://cms.app.content.private/domain-select")
        
        self.vg = self.driver.find_element_by_xpath("//p[text()='Világgazdaság']")

        self.vg.click()
        
        #selectVG END'''



if __name__ == '__main__':
    
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/testreport'))

