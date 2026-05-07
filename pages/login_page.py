from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "[data-test='error']")

    def enter_credentials(self, user, pwd):
        self.type(self.USERNAME, user)
        self.type(self.PASSWORD, pwd)

    def submit(self):
        self.click(self.LOGIN_BTN)

    def get_error(self):
        return self.get_text(self.ERROR_MSG)