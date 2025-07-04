from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_out_form(self, first_name, last_name, postal_code):
        first_name_input = self.driver.find_element(By.ID, "first-name")
        first_name_input.send_keys(first_name)

        last_name_input = self.driver.find_element(By.ID, "last-name")
        last_name_input.send_keys(last_name)

        postal_code_input = self.driver.find_element(By.ID, "postal-code")
        postal_code_input.send_keys(postal_code)

        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()

    def get_total_amount(self):
        total_amount = self.driver.find_element(By.CLASS_NAME, "summary_subtotal_label")
        return total_amount.text