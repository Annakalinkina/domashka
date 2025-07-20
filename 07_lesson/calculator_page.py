from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_delay(self, delay):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(delay))

    def click_button(self, button_text):
        button = self.driver.find_element(By.XPATH, f"//button[text()='{button_text}']")
        button.click()

    def wait_until_result_is_displayed(self, timeout):
        result_field = self.driver.find_element(By.CSS_SELECTOR, ".top input#result")
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element_value((By.ID, "result"), "15")
        )
        assert result_field.get_attribute("value") == "15"

