import pytest
from selenium import webdriver
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_saucedemo(browser):
    browser.get("https://www.saucedemo.com/")
    login_page=LoginPage(browser)
    login_page.login(username="standard_user", password="secret_sauce")
    main_page = MainPage(browser)
    products = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
    for product in products:
        main_page.add_to_cart(product)
    main_page.go_to_cart()
    cart_page = CartPage(browser)
    cart_page.checkout()
    checkout_page = CheckoutPage(browser)
    checkout_page.fill_out_form("John", "Doe", "12345")
    total_amount = checkout_page.get_total_amount()
    assert total_amount == "Total: $58.29", f"Expected total to be 'Total: $58.29', but got '{total_amount}'"