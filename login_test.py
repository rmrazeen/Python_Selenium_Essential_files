import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




# Set up logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)


@pytest.fixture()
def browser():
    # Setup Chrome options
    logger.info("Step 1: Open the browser")
    print("Step 1: Open the browser")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_successful_login(browser):
    """Authentication: Valid Login Test"""
    print("Authentication: Valid Login Test called")
    # Test data
    username = "standard_user"
    password = "secret_sauce"

    logger.info("Step 2: navigate to login page")

    # Navigate to login page
    browser.get("https://www.saucedemo.com/")

    # Example: wait up to 10 seconds for an element to be visible
    wait = WebDriverWait(browser, 10)
    element = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))

    logger.info("Step 3: Input username")

    # Enter credentials and login
    usernamefield = browser.find_element(By.ID,"user-name")
    usernamefield.send_keys(username)

    time.sleep(2)
    logger.info("Step 4: Input password")

    passwordfield = browser.find_element(By.XPATH, "//input[@id='password']")
    passwordfield.send_keys(password)

    logger.info("Step 5: Click login button")

    time.sleep(2)
    loginButton = browser.find_element(By.ID, "login-button")
    loginButton.click()

    time.sleep(2)

    # Verify successful login
    assert "inventory" in browser.current_url


