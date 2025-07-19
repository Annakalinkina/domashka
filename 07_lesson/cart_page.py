from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, browser):
        self.browser = browser

    def checkout(self):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, "checkout"))).click()

