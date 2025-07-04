import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def browser():

    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_shopping_cart(browser):

    browser.get("https://www.saucedemo.com/")


    username_field = browser.find_element(By.CSS_SELECTOR, "#user-name")
    password_field = browser.find_element(By.CSS_SELECTOR, "#password")
    login_button = browser.find_element(By.CSS_SELECTOR, "#login-button")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()


    browser.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']//following-sibling::button").click()
    browser.find_element(By.XPATH, "//div[text()='Sauce Labs Bolt T-Shirt']//following-sibling::button").click()
    browser.find_element(By.XPATH, "//div[text()='Sauce Labs Onesie']//following-sibling::button").click()


    cart_button = browser.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
    cart_button.click()


    checkout_button = browser.find_element(By.CSS_SELECTOR, "#checkout")
    checkout_button.click()


    first_name_field = browser.find_element(By.CSS_SELECTOR, "#first-name")
    last_name_field = browser.find_element(By.CSS_SELECTOR, "#last-name")
    postal_code_field = browser.find_element(By.CSS_SELECTOR, "#postal-code")
    continue_button = browser.find_element(By.CSS_SELECTOR, "#continue")

    first_name_field.send_keys("Иван")
    last_name_field.send_keys("Петров")
    postal_code_field.send_keys("12345")
    continue_button.click()

    total_element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".summary_total_label"))
    )


    total_text = total_element.text
    assert total_text == "Total: $58.29", f"Expected total to be $58.29, but got {total_text}"