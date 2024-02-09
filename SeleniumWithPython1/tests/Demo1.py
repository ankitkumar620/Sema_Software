from selenium import webdriver
x=5
y=5
print(x+y)
#selenium code here
driver = webdriver.Chrome()
driver.get("http://demowebshop.tricentis.com/login")
driver.find_element_by_id("Email").send_keys('aswani.kumar.avilala@accenture.com')
driver.find_element_by_id("Password").send_keys('3423243243')
driver.find_element_by_css_selector("input[value='Log in']").click()