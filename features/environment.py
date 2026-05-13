# features/environment.py
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
    
    # Create options object
    if browser == 'chrome':
        options = Options()
        
        # 👇 ADD THESE LINES TO DISABLE PASSWORD MANAGER POPUP 👇
        options.add_argument("--disable-save-password-bubble")
        options.add_argument("--disable-features=PasswordManager")
        options.add_argument("--safebrowsing-disable-download-protection")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-infobars")
        
        # Disable password-related preferences
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
            "safebrowsing.enabled": False,
            "profile.default_content_setting_values.notifications": 2,
        }
        options.add_experimental_option("prefs", prefs)
        # 👆 END PASSWORD MANAGER DISABLE OPTIONS 👆
        
    else:
        options = FirefoxOptions()
        # Firefox doesn't have the same password popup issue, but you can add prefs if needed
    
    if headless:
        options.add_argument('--headless=new')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    
    # Create driver with configured options
    if browser == 'chrome':
        context.driver = webdriver.Chrome(options=options)
    else:
        context.driver = webdriver.Firefox(options=options)
    
    context.driver.implicitly_wait(5)

def after_scenario(context, scenario):
    if scenario.status == 'failed':
        context.driver.save_screenshot(f"reports/screenshots/{scenario.name.replace(' ', '_')}.png")
    context.driver.delete_all_cookies()

def after_all(context):
    context.driver.quit()