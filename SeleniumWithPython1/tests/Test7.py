import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.common.by import By
import time
class MyTestCase(unittest.TestCase):
    def test_something(self):
        driver=webdriver.Chrome()
        driver.get("http://hdfcbank.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)
        driver.find_element_by_id("loginsubmit").click()
        home=driver.current_window_handle
        windows=driver.window_handles

        driver.switch_to.window(windows[1])
        driver.maximize_window()
        self.assertEqual(driver.title, 'NetBanking')

        #WDW(driver,10).until(EC.element_to_be_clickable(driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/a")))
        WDW(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[4]/div[2]/div[1]/a")))
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/a").click()

        driver.switch_to.frame("login_page")
        driver.find_element_by_css_selector("img[alt='continue']").click()
        time.sleep(5)
        alertbox=driver.switch_to.alert
        print("The Alert Message ",alertbox.text)
        alertbox.accept()
        time.sleep(5)
        driver.find_element_by_name("fldLoginUserId").send_keys("3123232")

        driver.switch_to.window(home)
        #driver.find_element_by_id("creditcardlogin").click()
        driver.execute_script("document.getElementById('creditcardlogin').click()")
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
