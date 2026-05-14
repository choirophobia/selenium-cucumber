import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class inventoryPage(BasePage):
    productContainer = (By.CLASS_NAME, "inventory_item")
    addToCartBTN = (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']")
    shoppingCartBTN = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    yourCartPage = (By.CSS_SELECTOR, "[data-test='inventory-item']")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")




    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def click_add_to_cart(self):
        self.click(self.addToCartBTN)

    def click_shopping_cart(self):
        self.click(self.shoppingCartBTN)

    def wait_for_products(self, timeout=10):
        """Wait for product items to be visible"""
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(self.productContainer)
        )

    def get_add_to_cart_buttons(self):
        """Return list of all 'Add to Cart' buttons"""
        return self.driver.find_elements(*self.addToCartBTN)

    def click_all_add_to_cart_buttons(self):
        # """Click every 'Add to Cart' button on the page"""
        # Wait for products to load first
        self.wait_for_products()
        
        # Get all buttons
        buttons = self.get_add_to_cart_buttons()
        
        # Click each one
        for i, button in enumerate(buttons, 1):
            # Wait until button is clickable
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(button)
            )
            button.click()
            # Optional: small delay between clicks for stability
            time.sleep(0.3)
        
        # Wait for cart badge to appear/update
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.CART_BADGE)
        )

    def get_cart_badge_text(self):
        """Get the text from the cart badge (number of items)"""
        try:
            badge = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.CART_BADGE)
            )
            return badge.text
        except:
            # If badge doesn't exist, cart is empty
            return "0"

    def get_cart_count(self):
        """Get cart count as integer"""
        badge_text = self.get_cart_badge_text()
        return int(badge_text) if badge_text.isdigit() else 0