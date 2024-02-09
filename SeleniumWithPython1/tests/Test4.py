import unittest
from selenium import webdriver
import time
class MyTestCase(unittest.TestCase):
    def test_something(self):
        driver=webdriver.Chrome()
        driver.get("http://www.google.co.in/")
        driver.maximize_window()
        driver.find_element_by_css_selector("a[title='Google apps']").click()
        ul=driver.find_element_by_css_selector("div[aria-label='Google apps']>*:first-child")
        listofli=ul.find_elements_by_tag_name("li")
        self.assertEqual(len(listofli),13)
        time.sleep(5)

    def test_lang_links(self):
        driver=webdriver.Chrome()
        driver.get("http://www.google.co.in/")
        driver.maximize_window()
        div=driver.find_element_by_css_selector("div#SIvCob")
        listoflinks=div.find_elements_by_tag_name("a")
        self.assertEqual(len(listoflinks),9)
        time.sleep(5)
if __name__ == '__main__':
    unittest.main()
