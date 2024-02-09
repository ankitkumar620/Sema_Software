from selenium.webdriver.common.by import By
class RegisterPage(object):
    USER_NAME=(By.NAME,"email")
    PASSWORD=(By.NAME,"password")
    CONF_PASSWORD=(By.NAME,"confirmPassword")
    SUBMIT=(By.NAME,"register")
    SIGN_OFF=(By.LINK_TEXT,"SIGN-OFF")

    def click_SignOFF(self):
        self.driver.find_element(*RegisterPage.SIGN_OFF).click()

    def click_Submit(self):

        self.driver.find_element(*RegisterPage.USER_NAME).send_keys("mercury")
        self.driver.find_element(*RegisterPage.PASSWORD).send_keys("mercury")
        self.driver.find_element(*RegisterPage.CONF_PASSWORD).send_keys("mercury")
        self.driver.find_element(*RegisterPage.SUBMIT).click()
        return self.driver.title

    def __init__(self,driver):
        self.driver=driver

