from selenium.webdriver.common.by import By
class WelcomePage(object):
    USER_NAME=(By.NAME,'userName')
    PASSWORD=(By.NAME,'password')
    SIGN_IN=(By.CSS_SELECTOR,"input[value='Login']")
    REGISTER=(By.LINK_TEXT,"REGISTER")

    def click_Register(self):
        self.driver.find_element(*WelcomePage.REGISTER).click()

    def click_SignIn(self):
        self.driver.find_element(*WelcomePage.USER_NAME).send_keys("mercury")
        self.driver.find_element(*WelcomePage.PASSWORD).send_keys("mercury")
        self.driver.find_element(*WelcomePage.SIGN_IN).click()
        return self.driver.title

    def __init__(self,driver):
        self.driver=driver
