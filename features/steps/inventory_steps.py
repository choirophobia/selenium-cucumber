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
    time.sleep(5)
