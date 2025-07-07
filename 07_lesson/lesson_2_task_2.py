import pytest
from selenium import webdriver
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage

def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_saucedemo(browser):
    browser.get("https://www.saucedemo.com/")

    login_page = LoginPage(browser)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    main_page = MainPage(browser)
    main_page.add_product_to_cart("Sauce Labs Backpack")
    main_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")
    main_page.add_product_to_cart("Sauce Labs Onesie")
    main_page.go_to_cart()
    cart_page = CartPage(browser)
    cart_page.click_checkout()
    checkout_page = CheckoutPage(browser)
    checkout_page.fill_out_form("John", "Doe", "12345")
    total_amount = checkout_page.get_total_amount()
    assert total_amount == "Total: $58.29", f"Expected total to be 'Total: $58.29', but got '{total_amount}'"