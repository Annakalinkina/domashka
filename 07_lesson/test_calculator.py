
import pytest
from selenium import webdriver
from calculator_page import CalculatorPage

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def test_calculator(browser):
    timeout = 45
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    calculator_page = CalculatorPage(browser)
    calculator_page.enter_delay(timeout)
    calculator_page.click_button('7')
    calculator_page.click_button('+')
    calculator_page.click_button('8')
    calculator_page.click_button('=')
    calculator_page.wait_until_result_is_displayed(timeout)
