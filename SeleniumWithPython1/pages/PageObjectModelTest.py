import unittest
from selenium import webdriver
from pages.MyWelcomePage import WelcomePage
from pages.MyRegisterPage import RegisterPage
class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("in setup")
        self.driver=webdriver.Chrome()
        self.driver.get("http://newtours.demoaut.com")
        self.welcome=WelcomePage(self.driver)
        self.register=RegisterPage(self.driver)

    @classmethod
    def tearDownClass(self):
        print("in teardown")
        self.driver.close()

    def test_mercurytours_test2(self):
        mytitle=self.welcome.click_SignIn()
        self.assertTrue(self.driver.title.startswith("Find a Flight:"))

    def test_mercurytours_test1(self):
        self.welcome.click_Register()
        self.register.click_Submit()
        self.register.click_SignOFF()


if __name__ == '__main__':
    unittest.main()
