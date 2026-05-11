import time

from behave import given, when, then
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from parse import parse

@given('I navigate to the login page')
def step_navigate(context):
    context.driver.get(context.base_url)
    context.login_page = LoginPage(context.driver)

@when('I enter valid credentials')
def step_valid_creds(context):
    context.login_page.enter_credentials("standard_user", "secret_sauce")
    time.sleep(2)

@when('I enter username "{username}" and password "{password}"')
def step_creds(context, username, password):
    context.login_page.enter_credentials(username, password)
    time.sleep(2)

@when('I submit the form')
def step_submit(context):
    context.login_page.submit()
    time.sleep(5)



@then('I should see error "{message}"')
def step_error(context, message):
    assert message.lower() in context.login_page.get_error().lower()