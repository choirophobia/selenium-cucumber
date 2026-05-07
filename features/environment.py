from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import os

def before_all(context):
    browser = context.config.userdata.get('browser', 'chrome').lower()
    headless = context.config.userdata.get('headless', 'false').lower() == 'true'
    context.base_url = context.config.userdata.get('base_url', 'https://saucedemo.com')
    
    os.makedirs('reports/screenshots', exist_ok=True)
    os.makedirs('reports/allure-results', exist_ok=True)
    
    options = Options() if browser == 'chrome' else FirefoxOptions()
    if headless:
        options.add_argument('--headless=new')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    
    context.driver = webdriver.Chrome(options=options) if browser == 'chrome' else webdriver.Firefox(options=options)
    context.driver.implicitly_wait(5)

def after_scenario(context, scenario):
    if scenario.status == 'failed':
        context.driver.save_screenshot(f"reports/screenshots/{scenario.name.replace(' ', '_')}.png")
    context.driver.delete_all_cookies()

def after_all(context):
    context.driver.quit()