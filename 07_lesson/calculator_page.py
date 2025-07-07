from selenium.webdriver.common.by import By


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

    # ActionChains(self.driver).move_to_element(button).click().perform()

    def get_result(self):
        result = self.driver.find_element(By.CSS_SELECTOR, ".screen")
        return result.text
