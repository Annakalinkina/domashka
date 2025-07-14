from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_delay(self, delay):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_button(self, button_text):
        button = self.driver.find_element(By.XPATH, f"//span[text()='{button_text}']")
        button.click()

    def wait_until_result_is_displayed(self, timeout: int):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//div[text()="15"]')))

