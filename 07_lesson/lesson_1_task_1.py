import pytest
from selenium import webdriver
from time import sleep
from calculator_page import CalculatorPage

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def test_calculator(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    calculator_page = CalculatorPage(browser)
    calculator_page.enter_delay(45)
    calculator_page.click_button('7')
    calculator_page.click_button('+')
    calculator_page.click_button('8')
    calculator_page.click_button('=')
    sleep(45)
    result = calculator_page.get_result()
    assert result == "15", f"Expected result to be '15', but got '{result}'"