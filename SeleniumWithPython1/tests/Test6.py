import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
class MyTestCase(unittest.TestCase):
    def test_something(self):
        driver=webdriver.Chrome()
        driver.get("http://cleartrip.com/")
        driver.maximize_window()
        fromcity=driver.find_element_by_id("FromTag")
        actions1=ActionChains(driver)
        actions1.key_down(Keys.SHIFT,fromcity).send_keys("h").key_up(Keys.SHIFT).perform()
        time.sleep(5)
        actions1.send_keys("yd").perform()
        time.sleep(5)
        actions1.send_keys(Keys.ENTER).perform()
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
