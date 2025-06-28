from selenium import webdriver
from selenium.webdriver.common.by import By




driver = webdriver.Firefox()

driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/login") #зайти на сайт
username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")
username_field.send_keys("tomsmith")
password_field.send_keys("SuperSecretPassword!")
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()
success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success").text
print(success_message)
driver.quit()
