import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
class MyTestCase(unittest.TestCase):
    def test_something(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://www.hdfcbank.com/")
        driver.implicitly_wait(15)
        #driver.find_element_by_xpath("//a[@href='/personal/products/demat/demat-account']").click()
        action1=ActionChains(driver)
        action1.move_to_element(driver.find_element_by_xpath("//a[@href='/personal/products']")).move_to_element(driver.find_element_by_xpath("//a[@href='/personal/products/demat']")).perform()
        action1.move_to_element(driver.find_element_by_xpath("//a[@href='/personal/products/demat/demat-account']")).click().perform()
        title1=driver.title
        self.assertEqual(title1,"Demat Account - Open Demat Account Online in India with HDFC Bank")
        time.sleep(10)


