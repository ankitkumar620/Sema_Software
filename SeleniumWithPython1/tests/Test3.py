import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import  By
class MyTestCase(unittest.TestCase):
    def test_something(self):
        driver=webdriver.Chrome()
        driver.get("http://newtours.demoaut.com/")

       # driver.find_element(By.,"value of id")

        driver.find_element_by_name("userName").send_keys("mercury")
        driver.find_element_by_name("password").send_keys("mercury")
        driver.find_element_by_name("login").click()



        self.assertEqual(driver.title,"Find a Flight: Mercury Tours:")

        driver.find_element_by_css_selector("input[value='oneway']").click()
        driver.find_element_by_name("passCount").send_keys("4")
        #from_port=Select(driver.find_element_by_name('fromPort'))
        myoptions=Select(driver.find_element_by_name('fromPort')).options
        for option in myoptions:
            #print(option.text)
            city=option.get_attribute('value')
            if city=='Paris':
                from_port.select_by_value(city)

        time.sleep(5)

if __name__ == '__main__':
    unittest.main()
