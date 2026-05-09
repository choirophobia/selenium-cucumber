from behave import given, when, then
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from parse import parse

# @given('I navigate to the login page')
# def step_navigate(context):
#     context.driver.get(context.base_url)
#     context.login_page = LoginPage(context.driver)

# @when('I enter valid credentials')
# def step_valid_creds(context):
#     context.login_page.enter_credentials("standard_user", "secret_sauce")

# @when('I enter username "{username}" and password "{password}"')
# def step_creds(context, username, password):
#     context.login_page.enter_credentials(username, password)

@when('I click add to cart for the first item')
def step_add_to_cart(context):
    context.inventory_page.click_add_to_cart_first_item()

# @then('I should see the inventory dashboard')
# def step_dashboard(context):
#     assert "inventory" in context.driver.current_url
#     assert context.driver.find_element(By.CSS_SELECTOR, "[data-test='inventory-container']").is_displayed()

# @then('I should see error "{message}"')
# def step_error(context, message):
#     assert message.lower() in context.login_page.get_error().lower()