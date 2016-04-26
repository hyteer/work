from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.maximize_window()
driver.get("http://localhost/wp")

