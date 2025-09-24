"""
SELENIUM ERROR HANDLING AND WAIT CONDITIONS GUIDE
=================================================

This guide covers try-except blocks and WebDriverWait with Expected Conditions (EC)
- When to use them
- Where to use them  
- How to use them effectively
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException, 
    TimeoutException, 
    ElementClickInterceptedException,
    StaleElementReferenceException,
    WebDriverException
)
import time

# ============================================================================
# 1. TRY-EXCEPT: WHEN, WHERE, HOW TO USE
# ============================================================================

def basic_try_except_example():
    """
    WHEN TO USE: Always wrap risky operations
    WHERE TO USE: Around any operation that might fail
    """
    driver = webdriver.Chrome()
    
    try:
        # Risky operation - page might not load
        driver.get("https://example.com")
        
        # Risky operation - element might not exist
        element = driver.find_element(By.ID, "some-id")
        element.click()
        
    except NoSuchElementException:
        print("Element not found!")
    except TimeoutException:
        print("Page took too long to load!")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        # ALWAYS runs - cleanup resources
        driver.quit()

# ============================================================================
# 2. EXPECTED CONDITIONS (EC): WHEN, WHERE, HOW TO USE
# ============================================================================

def expected_conditions_examples():
    """
    WHEN TO USE: Instead of time.sleep() - wait for specific conditions
    WHERE TO USE: Before interacting with elements
    """
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
    
    try:
        driver.get("https://testautomationpractice.blogspot.com/")
        
        # ===== COMMON EXPECTED CONDITIONS =====
        
        # 1. PRESENCE_OF_ELEMENT_LOCATED - Element exists in DOM
        # WHEN: When you need element to be present (not necessarily visible)
        element = wait.until(EC.presence_of_element_located((By.ID, "name")))
        print("✓ Element is present in DOM")
        
        # 2. VISIBILITY_OF_ELEMENT_LOCATED - Element is visible
        # WHEN: When you need element to be visible to user
        visible_element = wait.until(EC.visibility_of_element_located((By.ID, "email")))
        print("✓ Element is visible")
        
        # 3. ELEMENT_TO_BE_CLICKABLE - Element can be clicked
        # WHEN: Before clicking any element
        clickable_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']")))
        print("✓ Element is clickable")
        
        # 4. TEXT_TO_BE_PRESENT_IN_ELEMENT - Wait for specific text
        # WHEN: Waiting for dynamic text to appear
        wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Automation"))
        print("✓ Expected text is present")
        
        # 5. INVISIBILITY_OF_ELEMENT - Wait for element to disappear
        # WHEN: Waiting for loading spinners to disappear
        # wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "loading")))
        
    except TimeoutException:
        print("✗ Condition not met within timeout period")
    finally:
        driver.quit()

# ============================================================================
# 3. COMPREHENSIVE EXAMPLE: REAL-WORLD USAGE
# ============================================================================

def comprehensive_selenium_example():
    """
    Real-world example showing proper error handling and waits
    """
    driver = None
    
    try:
        # Initialize driver with error handling
        try:
            driver = webdriver.Chrome()
            print("✓ Driver initialized successfully")
        except WebDriverException as e:
            print(f"✗ Failed to initialize driver: {e}")
            return
        
        # Set up wait
        wait = WebDriverWait(driver, 10)
        
        # Navigate with error handling
        try:
            driver.get("https://testautomationpractice.blogspot.com/")
            print("✓ Page loaded successfully")
        except Exception as e:
            print(f"✗ Failed to load page: {e}")
            return
        
        # Wait for and interact with elements
        try:
            # Wait for name field to be clickable
            name_field = wait.until(EC.element_to_be_clickable((By.ID, "name")))
            name_field.clear()
            name_field.send_keys("John Doe")
            print("✓ Name field filled")
            
            # Wait for email field with multiple conditions
            email_field = wait.until(EC.all_of([
                EC.presence_of_element_located((By.ID, "email")),
                EC.element_to_be_clickable((By.ID, "email"))
            ]))
            email_field.clear()
            email_field.send_keys("john@example.com")
            print("✓ Email field filled")
            
            # Wait for dropdown to be clickable
            country_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "country")))
            from selenium.webdriver.support.ui import Select
            select = Select(country_dropdown)
            select.select_by_visible_text("United States")
            print("✓ Country selected")
            
        except TimeoutException:
            print("✗ Element not found within timeout period")
        except ElementClickInterceptedException:
            print("✗ Element click was intercepted")
        except StaleElementReferenceException:
            print("✗ Element reference is stale, need to re-find element")
        
        # Handle dynamic content
        try:
            # Wait for specific text to appear (simulating dynamic content)
            wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "title"), "Practice"))
            print("✓ Page title contains expected text")
        except TimeoutException:
            print("✗ Expected text did not appear")
        
    except Exception as e:
        print(f"✗ Unexpected error in main execution: {e}")
    
    finally:
        # Cleanup - ALWAYS close driver
        if driver:
            try:
                driver.quit()
                print("✓ Driver closed successfully")
            except Exception as e:
                print(f"✗ Error closing driver: {e}")

# ============================================================================
# 4. CUSTOM EXPECTED CONDITIONS
# ============================================================================

def custom_expected_conditions():
    """
    Creating custom expected conditions for specific scenarios
    """
    class element_has_css_class:
        """Custom EC: Wait for element to have specific CSS class"""
        def __init__(self, locator, css_class):
            self.locator = locator
            self.css_class = css_class
        
        def __call__(self, driver):
            element = driver.find_element(*self.locator)
            if self.css_class in element.get_attribute("class"):
                return element
            return False
    
    class text_length_to_be(object):
        """Custom EC: Wait for text to have specific length"""
        def __init__(self, locator, length):
            self.locator = locator
            self.length = length
        
        def __call__(self, driver):
            element = driver.find_element(*self.locator)
            if len(element.text) >= self.length:
                return element
            return False
    
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("https://testautomationpractice.blogspot.com/")
        
        # Use custom expected condition
        element = wait.until(custom_expected_conditions.text_length_to_be(
            (By.TAG_NAME, "h1"), 5
        ))
        print(f"✓ Found element with text length >= 5: {element.text}")
        
    except TimeoutException:
        print("✗ Custom condition not met")
    finally:
        driver.quit()

# ============================================================================
# 5. BEST PRACTICES SUMMARY
# ============================================================================

def best_practices_summary():
    """
    Summary of when, where, and how to use try-except and EC
    """
    print("""
    
    🎯 TRY-EXCEPT BEST PRACTICES:
    ============================
    
    WHEN TO USE:
    • Always wrap driver.get()
    • Always wrap find_element operations
    • Always wrap click operations
    • Always wrap form submissions
    • Always wrap driver initialization
    
    WHERE TO USE:
    • Around any Selenium operation that might fail
    • At the start of test methods
    • Around driver initialization and cleanup
    • In page object methods
    
    HOW TO USE:
    • Use specific exceptions (NoSuchElementException, TimeoutException)
    • Always include finally block for cleanup
    • Log meaningful error messages
    • Don't catch and ignore - handle appropriately
    
    
    🎯 EXPECTED CONDITIONS (EC) BEST PRACTICES:
    ==========================================
    
    WHEN TO USE:
    • Instead of time.sleep() (NEVER use time.sleep!)
    • Before interacting with any element
    • When waiting for page state changes
    • When dealing with dynamic content
    
    WHERE TO USE:
    • Before find_element operations
    • Before click operations
    • Before sending text to fields
    • After page navigation
    • When waiting for AJAX requests
    
    MOST COMMON EC CONDITIONS:
    • presence_of_element_located() - Element exists
    • visibility_of_element_located() - Element is visible
    • element_to_be_clickable() - Element can be clicked
    • text_to_be_present_in_element() - Text appears
    • invisibility_of_element() - Element disappears
    
    
    🚫 WHAT NOT TO DO:
    ==================
    • Don't use time.sleep() - use explicit waits
    • Don't catch Exception and do nothing
    • Don't forget finally block for cleanup
    • Don't use overly long timeout periods
    • Don't ignore TimeoutException
    
    ✅ WHAT TO DO:
    ==============
    • Use WebDriverWait with appropriate timeout (5-15 seconds)
    • Use specific expected conditions
    • Handle specific exceptions appropriately
    • Always clean up resources in finally block
    • Log meaningful error messages
    • Use descriptive variable names
    """)

# ============================================================================
# RUN EXAMPLES
# ============================================================================

if __name__ == "__main__":
    print("🔍 SELENIUM ERROR HANDLING AND WAIT CONDITIONS EXAMPLES")
    print("=" * 60)
    
    print("\n1. Running comprehensive example...")
    comprehensive_selenium_example()
    
    print("\n2. Best practices summary:")
    best_practices_summary()
    
    # Uncomment to run other examples:
    # basic_try_except_example()
    # expected_conditions_examples()
    # custom_expected_conditions()