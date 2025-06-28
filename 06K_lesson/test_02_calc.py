import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class CalculatorTest(unittest.TestCase):
def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_calculator_addition(self):

        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")


        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.send_keys("45")


        self.driver.find_element(By.CSS_SELECTOR, "button[value='7']").click()
        self.driver.find_element(By.CSS_SELECTOR, "button[value='+']").click()
        self.driver.find_element(By.CSS_SELECTOR, "button[value='8']").click()
        self.driver.find_element(By.CSS_SELECTOR, "button[value='='").click()


        time.sleep(50)


        result = self.driver.find_element(By.CSS_SELECTOR, "#result").text
        self.assertEqual(result, "15", f"Expected result to be 15, but got {result}")

    def tearDown(self):

        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

