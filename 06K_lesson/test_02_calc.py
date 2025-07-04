import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def browser():

    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculator_addition(browser):

    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")


    delay_input = browser.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.send_keys("45")


    browser.find_element(By.CSS_SELECTOR, "button[value='7']").click()
    browser.find_element(By.CSS_SELECTOR, "button[value='+']").click()
    browser.find_element(By.CSS_SELECTOR, "button[value='8']").click()
    browser.find_element(By.CSS_SELECTOR, "button[value='='").click()


    result_element = WebDriverWait(browser, 60).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#result"))
    )


    result = result_element.text
    assert result == "15", f"Expected result to be 15, but got {result}"

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()