from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_delay(self, delay):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_button(self, button_text):
        button = self.driver.find_element(By.XPATH, f"//button[text()='{button_text}']")
        ActionChains(self.driver).move_to_element(button).click().perform()

    def get_result(self):
        result = self.driver.find_element(By.CSS_SELECTOR, "#result")
        return result.text



