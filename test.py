from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Maximize the browser window
    driver.maximize_window()
    
    # Open the Python website
    driver.get("http://www.python.org")
    
    # Set an implicit wait
    driver.implicitly_wait(10)
    
    # Perform any additional actions here if needed

finally:
    # Ensure the browser is closed
    driver.quit()