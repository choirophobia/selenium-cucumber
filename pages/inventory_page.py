from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class inventoryPage(BasePage):
    addToCartBTN = (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']")
    shoppingCartBTN = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    yourCartPage = (By.CSS_SELECTOR, "[data-test='inventory-item']")


    def click_add_to_cart(self):
        self.click(self.addToCartBTN)

    def click_shopping_cart(self):
        self.click(self.shoppingCartBTN)