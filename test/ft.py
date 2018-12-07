#! /usr/bin/python3
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        #self.browser.implicitly_wait(3)
        self.browser.get('http://localhost:8888')


    def tearDown(self):
        pass
        #self.browser.quit()
    
    def test_is_title_ok(self):
        
        self.assertIn('Hello', self.browser.title)
        #self.fail('Finish the test!')
    
    def test_login(self):
        login = self.browser.find_element_by_id("login")
        password = self.browser.find_element_by_id("password")
        login.send_keys('admin0')
        password.send_keys('12')
        password.send_keys(Keys.ENTER)
        alert = self.browser.find_element_by_id("alert-message")
        self.assertEqual('Error!!!!', alert.text)
        #time.sleep(10)


if __name__ == '__main__':
    unittest.main()