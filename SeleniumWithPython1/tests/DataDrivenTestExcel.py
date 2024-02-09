import unittest
import openpyxl
from selenium import webdriver

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://newtours.demoaut.com/")
        self.readExcel()

    def login(self,username,password):
        self.driver.find_element_by_name("userName").send_keys(username)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_name('login').click()
        mytitle=self.driver.title
        if mytitle.startswith('Find a Flight'):
            self.assertTrue(mytitle.startswith('Find'))
            self.driver.find_element_by_link_text('SIGN-OFF').click()
            return 'VALID USER'
        else:
            self.assertTrue(mytitle.startswith('Sign-on'))
            return 'IN-VALID USER'


    def readExcel(self):
        file='data/Book1.xlsx'
        wb=openpyxl.load_workbook(file)
        sheet1=wb['Sheet1']
        for c1,c2,c3 in sheet1['A2':'C4']:
            c3.value=self.login(c1.value,c2.value)

        wb.save(file)
if __name__ == '__main__':
    unittest.main()
