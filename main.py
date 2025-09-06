from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Launch Chrome (Selenium will auto-manage ChromeDriver if v4.6+)
driver = webdriver.Chrome()

# Open python.org
driver.get("http://www.python.org")

# Verify title contains "Python"
assert "Python" in driver.title

# Find the search box
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

# Verify results are found
assert "No results found." not in driver.page_source

# Close the browser window
driver.close()
