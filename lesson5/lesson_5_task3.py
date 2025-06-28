from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Firefox()

driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/inputs") #зайти на сайт
input_selektor = "//input"
input_ = driver.find_element(By.XPATH, input_selektor)
input_.send_keys("Sky")
input_.clear()
input_.send_keys("Pro")
driver.quit()