import time

from behave import given, when, then
from pages.inventory_page import inventoryPage 
from selenium.webdriver.common.by import By
from parse import parse



# @given('I am on the inventory page')
# def step_on_inventory(context):
#     # Assumes login already happened, or navigate directly if authenticated
#     context.driver.get(f"{context.base_url}/inventory.html")
#     context.inventory_page = inventoryPage(context.driver)
#     time.sleep(2)

@then('I should see the inventory dashboard')
def step_dashboard(context):
    assert "inventory" in context.driver.current_url
    context.inventory_page = inventoryPage(context.driver)
    assert context.driver.find_element(By.CSS_SELECTOR, "[data-test='inventory-container']").is_displayed()
    time.sleep(2)
    

@then('I click add to cart for the first item')
def step_add_to_cart(context):
    context.inventory_page.click_add_to_cart()

@then('I click shopping cart button')
def step_click_shopping_cart(context):
    context.inventory_page.click_shopping_cart()
   
@then('I should see the item in the cart')
def step_verify_cart(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "[data-test='inventory-item']").is_displayed()

@when('I click all add to cart buttons')
def step_click_all_add_to_cart(context):
    # """Click every 'Add to Cart' button on the inventory page"""
    context.inventory_page.click_all_add_to_cart_buttons()
    time.sleep(2)  # Allow UI to update cart badge

@then('the cart badge should show "{expected_count}"')
def step_verify_cart_badge(context, expected_count):
    # """Verify the cart badge displays the expected item count"""
    actual_count = context.inventory_page.get_cart_badge_text()
    assert actual_count == expected_count, \
        f"Expected cart badge '{expected_count}', but got '{actual_count}'"