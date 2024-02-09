import unittest
from selenium import webdriver

class MyTestCase(unittest.TestCase):

    def test_login(self):
        #webdriver.Chrome('C:\Selenium\Drivers\chromedriver.exe')
        driver=webdriver.Chrome()
        driver.get("http://demowebshop.tricentis.com/login")
        driver.find_element_by_id("Email").send_keys('aswani.kumar.avilala@accenture.com')
        driver.find_element_by_id("Password").send_keys('3423243243')
        driver.find_element_by_css_selector("input[value='Log in']").click()
        mytitle=driver.title
        self.assertEqual(mytitle,'Demo Web Sh')
        """if title=='Demo Web':
            print('success')
        else:
            print('failure')"""
        print('continue with test code')

if __name__ == '__main__':
    unittest.main()
