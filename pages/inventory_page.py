from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class inventoryPage(BasePage):
    click_add_to_cart_first_item = (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']")


    def click_add_to_cart_first_item(self):
        self.click(self.click_add_to_cart_first_item)