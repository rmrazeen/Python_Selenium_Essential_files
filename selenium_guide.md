# Complete Selenium with Python Guide

## Table of Contents
1. [Setup and WebDriver](#setup-and-webdriver)
2. [Input Fields](#input-fields)
3. [Radio Buttons](#radio-buttons)
4. [Checkboxes](#checkboxes)
5. [Buttons](#buttons)
6. [Hovers](#hovers)
7. [File Upload](#file-upload)
8. [Alerts](#alerts)
9. [Time/Dates](#timedates)
10. [WebDriver Waits](#webdriver-waits)
11. [Button Enable/Disable](#button-enabledisable)
12. [Navigation](#navigation)
13. [Screenshots](#screenshots)
14. [Modals](#modals)

## Setup and WebDriver

First, install Selenium:
```bash
pip install selenium
```

Basic setup:
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

# Initialize driver
driver = webdriver.Chrome()  # Make sure chromedriver is in PATH
driver.maximize_window()
```

## 1. Input Fields

**When**: Use when you need to fill forms, search boxes, text areas
**Where**: Login pages, registration forms, search functionality
**How**: Using `send_keys()` method

```python
# Real-world example: Filling a login form
driver.get("https://the-internet.herokuapp.com/login")

# Find and fill username
username_field = driver.find_element(By.ID, "username")
username_field.clear()  # Clear existing text
username_field.send_keys("tomsmith")

# Find and fill password
password_field = driver.find_element(By.ID, "password")
password_field.clear()
password_field.send_keys("SuperSecretPassword!")

# Different ways to find input fields
# By ID
driver.find_element(By.ID, "email")
# By Name
driver.find_element(By.NAME, "username")
# By CSS Selector
driver.find_element(By.CSS_SELECTOR, "input[type='text']")
# By XPath
driver.find_element(By.XPATH, "//input[@placeholder='Enter email']")

# Handling different input types
text_input = driver.find_element(By.ID, "text-input")
text_input.send_keys("Sample text")

# For number inputs
number_input = driver.find_element(By.ID, "number-input")
number_input.send_keys("12345")

# For email inputs
email_input = driver.find_element(By.ID, "email-input")
email_input.send_keys("test@example.com")
```

## 2. Radio Buttons

**When**: Single selection from multiple options
**Where**: Forms with exclusive choices (gender, payment method)
**How**: Click the radio button element

```python
# Real-world example: Selecting payment method
driver.get("https://the-internet.herokuapp.com/radio_buttons")

# Select by value
credit_card_radio = driver.find_element(By.CSS_SELECTOR, "input[value='credit_card']")
credit_card_radio.click()

# Check if radio button is selected
if credit_card_radio.is_selected():
    print("Credit card option selected")

# Select by label text (more reliable)
radio_buttons = driver.find_elements(By.NAME, "payment_method")
for radio in radio_buttons:
    if radio.get_attribute("value") == "paypal":
        radio.click()
        break

# Handling radio button groups
def select_radio_by_text(driver, group_name, option_text):
    radios = driver.find_elements(By.NAME, group_name)
    for radio in radios:
        label = radio.find_element(By.XPATH, "following-sibling::label")
        if option_text in label.text:
            radio.click()
            break
```

## 3. Checkboxes

**When**: Multiple selections allowed
**Where**: Terms & conditions, feature selections, filters
**How**: Click to toggle state

```python
# Real-world example: Selecting multiple interests
driver.get("https://the-internet.herokuapp.com/checkboxes")

# Basic checkbox interaction
checkbox1 = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']:nth-of-type(1)")
if not checkbox1.is_selected():
    checkbox1.click()

checkbox2 = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']:nth-of-type(2)")
if checkbox2.is_selected():
    checkbox2.click()  # Uncheck if already checked

# Handling multiple checkboxes
def toggle_checkbox(element, should_be_checked):
    if element.is_selected() != should_be_checked:
        element.click()

# Select multiple checkboxes by labels
interests = ["Music", "Sports", "Reading"]
for interest in interests:
    checkbox = driver.find_element(By.XPATH, f"//label[contains(text(), '{interest}')]/input")
    if not checkbox.is_selected():
        checkbox.click()

# Get all selected checkboxes
selected_checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']:checked")
print(f"Number of selected checkboxes: {len(selected_checkboxes)}")
```

## 4. Buttons

**When**: Submitting forms, triggering actions
**Where**: All interactive web pages
**How**: Click method with various locators

```python
# Real-world example: E-commerce interactions
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

# Different ways to click buttons
# By text content
add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
add_button.click()

# By CSS class
submit_btn = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
submit_btn.click()

# By ID
login_btn = driver.find_element(By.ID, "login-button")
login_btn.click()

# Handling different button states
def safe_click(driver, locator, by_type=By.ID):
    try:
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((by_type, locator))
        )
        button.click()
        return True
    except:
        print(f"Button with {by_type}='{locator}' not clickable")
        return False

# Click multiple buttons
add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
for i in range(3):
    add_button.click()
    time.sleep(0.5)

# Remove buttons (dynamic elements)
delete_buttons = driver.find_elements(By.CSS_SELECTOR, ".added-manually")
for button in delete_buttons:
    button.click()
    time.sleep(0.5)
```

## 5. Hovers

**When**: Revealing hidden menus, tooltips
**Where**: Navigation menus, interactive elements
**How**: ActionChains for mouse movements

```python
from selenium.webdriver.common.action_chains import ActionChains

# Real-world example: Navigation menu hover
driver.get("https://the-internet.herokuapp.com/hovers")

# Basic hover action
element_to_hover = driver.find_element(By.CSS_SELECTOR, ".figure:nth-child(3)")
ActionChains(driver).move_to_element(element_to_hover).perform()

# Wait for hover effect to appear
hover_text = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".figcaption"))
)
print(hover_text.text)

# Complex hover sequences
def hover_and_click(driver, hover_element, click_element):
    actions = ActionChains(driver)
    actions.move_to_element(hover_element)
    actions.click(click_element)
    actions.perform()

# Hover over multiple elements
figures = driver.find_elements(By.CSS_SELECTOR, ".figure")
for i, figure in enumerate(figures):
    ActionChains(driver).move_to_element(figure).perform()
    time.sleep(1)
    
    # Check if caption is visible
    try:
        caption = figure.find_element(By.CSS_SELECTOR, ".figcaption")
        if caption.is_displayed():
            print(f"Figure {i+1}: {caption.text}")
    except:
        print(f"No caption for figure {i+1}")
```

## 6. File Upload

**When**: Uploading documents, images, attachments
**Where**: Forms requiring file input
**How**: send_keys() with file path

```python
import os

# Real-world example: Profile picture upload
driver.get("https://the-internet.herokuapp.com/upload")

# Prepare file path
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "test_file.txt")

# Create a test file if it doesn't exist
if not os.path.exists(file_path):
    with open(file_path, 'w') as f:
        f.write("This is a test file for Selenium upload.")

# Upload file
file_input = driver.find_element(By.ID, "file-upload")
file_input.send_keys(file_path)

# Click upload button
upload_button = driver.find_element(By.ID, "file-submit")
upload_button.click()

# Verify upload success
success_message = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "uploaded-files"))
)
print(f"Upload result: {success_message.text}")

# Handle multiple file uploads
def upload_multiple_files(driver, file_paths):
    file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file'][multiple]")
    # Join all file paths with newline for multiple selection
    all_files = "\n".join(file_paths)
    file_input.send_keys(all_files)

# Drag and drop file upload (advanced)
def drag_drop_upload(driver, file_path):
    # This requires JavaScript injection for drag-drop simulation
    js_script = """
    var input = arguments[0];
    var file = arguments[1];
    var dataTransfer = new DataTransfer();
    dataTransfer.items.add(file);
    input.files = dataTransfer.files;
    input.dispatchEvent(new Event('change', {bubbles: true}));
    """
    driver.execute_script(js_script, file_input, file_path)
```

## 7. Alerts

**When**: Handling JavaScript popups
**Where**: Confirmation dialogs, warning messages
**How**: switch_to.alert

```python
# Real-world example: Handling confirmation dialogs
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Alert (OK only)
alert_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
alert_button.click()

# Switch to alert and accept
alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
print(f"Alert text: {alert.text}")
alert.accept()

# Confirm (OK/Cancel)
confirm_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
confirm_button.click()

alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
alert.dismiss()  # Click Cancel
# or alert.accept() for OK

# Prompt (input required)
prompt_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']")
prompt_button.click()

alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
alert.send_keys("Hello Selenium!")
alert.accept()

# Generic alert handler
def handle_alert(driver, action="accept", text_to_send=None):
    try:
        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert_text = alert.text
        
        if text_to_send:
            alert.send_keys(text_to_send)
            
        if action == "accept":
            alert.accept()
        elif action == "dismiss":
            alert.dismiss()
            
        return alert_text
    except:
        return None
```

## 8. Time/Dates

**When**: Handling date pickers, time inputs
**Where**: Booking systems, scheduling forms
**How**: Various approaches depending on implementation

```python
from datetime import datetime, timedelta

# Method 1: Direct input (if date picker accepts keyboard input)
date_input = driver.find_element(By.ID, "date-picker")
date_input.clear()
date_input.send_keys("12/25/2023")

# Method 2: Using JavaScript to set value
future_date = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
driver.execute_script(f"arguments[0].value = '{future_date}';", date_input)

# Method 3: Interacting with custom date pickers
def select_date_from_calendar(driver, target_date):
    # Open calendar
    calendar_trigger = driver.find_element(By.CSS_SELECTOR, ".calendar-trigger")
    calendar_trigger.click()
    
    # Navigate to correct month/year
    while True:
        current_month = driver.find_element(By.CSS_SELECTOR, ".calendar-month").text
        if target_date.strftime("%B %Y") == current_month:
            break
        
        next_button = driver.find_element(By.CSS_SELECTOR, ".calendar-next")
        next_button.click()
    
    # Select day
    day_element = driver.find_element(By.XPATH, f"//td[@data-day='{target_date.day}']")
    day_element.click()

# Time input handling
time_input = driver.find_element(By.CSS_SELECTOR, "input[type='time']")
time_input.send_keys("14:30")  # 2:30 PM

# DateTime input
datetime_input = driver.find_element(By.CSS_SELECTOR, "input[type='datetime-local']")
datetime_value = datetime.now().strftime("%Y-%m-%dT%H:%M")
datetime_input.send_keys(datetime_value)
```

## 9. WebDriver Waits

**When**: Dealing with dynamic content, AJAX calls
**Where**: Essential for stable automation
**How**: Explicit waits, implicit waits, custom conditions

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Implicit Wait (applies to all elements)
driver.implicitly_wait(10)  # Wait up to 10 seconds for elements

# Explicit Waits (recommended approach)
wait = WebDriverWait(driver, 10)

# Wait for element to be present
element = wait.until(EC.presence_of_element_located((By.ID, "my-element")))

# Wait for element to be clickable
clickable_element = wait.until(EC.element_to_be_clickable((By.ID, "button")))

# Wait for text to be present
wait.until(EC.text_to_be_present_in_element((By.ID, "status"), "Complete"))

# Wait for element to be visible
visible_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "popup")))

# Wait for element to be invisible
wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "loading")))

# Custom wait conditions
class element_has_css_class:
    def __init__(self, locator, css_class):
        self.locator = locator
        self.css_class = css_class

    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        return self.css_class in element.get_attribute("class")

# Use custom condition
wait.until(element_has_css_class((By.ID, "my-element"), "active"))

# Polling wait with custom logic
def wait_for_condition(driver, condition_func, timeout=10):
    end_time = time.time() + timeout
    while time.time() < end_time:
        if condition_func(driver):
            return True
        time.sleep(0.5)
    return False

# Example usage
def page_loaded(driver):
    return driver.execute_script("return document.readyState") == "complete"

wait_for_condition(driver, page_loaded)
```

## 10. Button Enable/Disable

**When**: Checking form validation, conditional interactions
**Where**: Forms with validation, progressive disclosure
**How**: is_enabled() method and wait conditions

```python
# Real-world example: Form validation
submit_button = driver.find_element(By.ID, "submit-btn")

# Check if button is enabled
if submit_button.is_enabled():
    submit_button.click()
else:
    print("Submit button is disabled")

# Wait for button to become enabled
wait.until(EC.element_to_be_clickable((By.ID, "submit-btn")))

# Wait for button to be disabled
def element_to_be_disabled(locator):
    def _predicate(driver):
        element = driver.find_element(*locator)
        return not element.is_enabled()
    return _predicate

wait.until(element_to_be_disabled((By.ID, "submit-btn")))

# Enable button through form completion
def fill_required_fields_and_check_button(driver):
    # Fill required fields
    driver.find_element(By.ID, "name").send_keys("John Doe")
    driver.find_element(By.ID, "email").send_keys("john@example.com")
    
    # Check if submit button becomes enabled
    submit_btn = driver.find_element(By.ID, "submit-btn")
    
    # Wait up to 5 seconds for button to be enabled
    try:
        wait.until(EC.element_to_be_clickable((By.ID, "submit-btn")))
        return True
    except:
        return False

# Monitor button state changes
def monitor_button_state(driver, button_locator, duration=10):
    end_time = time.time() + duration
    previous_state = None
    
    while time.time() < end_time:
        button = driver.find_element(*button_locator)
        current_state = button.is_enabled()
        
        if current_state != previous_state:
            state_text = "enabled" if current_state else "disabled"
            print(f"Button is now {state_text}")
            previous_state = current_state
            
        time.sleep(0.5)
```

## 11. Navigation

**When**: Moving between pages, browser controls
**Where**: Multi-page workflows, testing navigation
**How**: Various navigation methods

```python
# Basic navigation
driver.get("https://example.com")

# Navigate forward and backward
driver.get("https://example.com/page1")
driver.get("https://example.com/page2")

# Go back
driver.back()

# Go forward
driver.forward()

# Refresh page
driver.refresh()

# Get current URL
current_url = driver.current_url
print(f"Current URL: {current_url}")

# Get page title
title = driver.title
print(f"Page title: {title}")

# Open new tab
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[-1])
driver.get("https://example.com/new-page")

# Switch between tabs/windows
all_windows = driver.window_handles
original_window = driver.current_window_handle

# Switch to specific window
for window in all_windows:
    if window != original_window:
        driver.switch_to.window(window)
        break

# Close current tab and switch back
driver.close()
driver.switch_to.window(original_window)

# Handle new window opened by clicking link
original_windows = driver.window_handles
link = driver.find_element(By.LINK_TEXT, "Open in new window")
link.click()

# Wait for new window
wait.until(lambda driver: len(driver.window_handles) > len(original_windows))

# Switch to new window
new_window = [w for w in driver.window_handles if w not in original_windows][0]
driver.switch_to.window(new_window)
```

## 12. Screenshots

**When**: Debugging, test evidence, visual validation
**Where**: Test automation, error reporting
**How**: Various screenshot methods

```python
import os
from datetime import datetime

# Full page screenshot
screenshot_path = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
driver.save_screenshot(screenshot_path)

# Get screenshot as binary data
screenshot_data = driver.get_screenshot_as_png()

# Save screenshot with custom name
def save_screenshot(driver, filename=None):
    if not filename:
        filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    
    driver.save_screenshot(filename)
    print(f"Screenshot saved as {filename}")
    return filename

# Screenshot on test failure
def screenshot_on_failure(driver, test_name):
    try:
        # Your test code here
        pass
    except Exception as e:
        error_screenshot = f"error_{test_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(error_screenshot)
        print(f"Test failed, screenshot saved: {error_screenshot}")
        raise e

# Element-specific screenshot (requires cropping)
def screenshot_element(driver, element, filename):
    # Take full screenshot
    driver.save_screenshot("temp_full.png")
    
    # Get element location and size
    location = element.location
    size = element.size
    
    # Crop using PIL (requires: pip install Pillow)
    from PIL import Image
    
    image = Image.open("temp_full.png")
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
    
    cropped = image.crop((left, top, right, bottom))
    cropped.save(filename)
    
    # Clean up temp file
    os.remove("temp_full.png")
```

## 13. Modals

**When**: Handling popup dialogs, overlays
**Where**: Confirmations, forms, information displays
**How**: Various strategies depending on modal type

```python
# Real-world example: Handling modal dialogs
driver.get("https://the-internet.herokuapp.com/entry_ad")

# Wait for modal to appear
modal = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".modal"))
)

# Close modal by clicking close button
close_button = driver.find_element(By.CSS_SELECTOR, ".modal-footer .btn")
close_button.click()

# Wait for modal to disappear
wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal")))

# Handle different types of modals
def handle_modal(driver, action="close"):
    try:
        # Wait for modal
        modal = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".modal")))
        
        if action == "close":
            # Try different close methods
            close_selectors = [
                ".modal-close",
                ".close",
                ".btn-close",
                "[data-dismiss='modal']",
                ".modal-footer .btn:last-child"
            ]
            
            for selector in close_selectors:
                try:
                    close_btn = driver.find_element(By.CSS_SELECTOR, selector)
                    close_btn.click()
                    break
                except:
                    continue
        
        elif action == "confirm":
            confirm_btn = driver.find_element(By.CSS_SELECTOR, ".btn-primary, .btn-confirm")
            confirm_btn.click()
            
        # Wait for modal to disappear
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal")))
        
    except Exception as e:
        print(f"Error handling modal: {e}")

# Handle modal with form
def fill_modal_form(driver, form_data):
    # Wait for modal form
    modal_form = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".modal form")))
    
    # Fill form fields
    for field_name, value in form_data.items():
        field = driver.find_element(By.NAME, field_name)
        field.clear()
        field.send_keys(value)
    
    # Submit form
    submit_btn = driver.find_element(By.CSS_SELECTOR, ".modal .btn-submit")
    submit_btn.click()
    
    # Wait for modal to close
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal")))

# Example usage
form_data = {
    "name": "John Doe",
    "email": "john@example.com",
    "message": "Hello from Selenium!"
}
fill_modal_form(driver, form_data)

# Handle overlay/backdrop clicks
def close_modal_by_overlay(driver):
    overlay = driver.find_element(By.CSS_SELECTOR, ".modal-backdrop, .modal-overlay")
    ActionChains(driver).click(overlay).perform()
```

## Complete Real-World Example

Here's a comprehensive example that combines multiple concepts:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def comprehensive_automation_example():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    
    try:
        # 1. Navigate to a demo site
        driver.get("https://demoqa.com/automation-practice-form")
        
        # 2. Fill input fields
        driver.find_element(By.ID, "firstName").send_keys("John")
        driver.find_element(By.ID, "lastName").send_keys("Doe")
        driver.find_element(By.ID, "userEmail").send_keys("john.doe@example.com")
        
        # 3. Select radio button
        gender_radio = driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']")
        gender_radio.click()
        
        # 4. Fill phone number
        driver.find_element(By.ID, "userNumber").send_keys("1234567890")
        
        # 5. Handle date picker
        date_input = driver.find_element(By.ID, "dateOfBirthInput")
        date_input.click()
        
        # Select month and year
        month_dropdown = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
        month_dropdown.select_by_visible_text("May")
        
        year_dropdown = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
        year_dropdown.select_by_visible_text("1990")
        
        # Select day
        day = driver.find_element(By.CSS_SELECTOR, ".react-datepicker__day--015")
        day.click()
        
        # 6. Fill subjects with autocomplete
        subjects_input = driver.find_element(By.ID, "subjectsInput")
        subjects_input.send_keys("Computer Science")
        
        # Wait for autocomplete and select
        autocomplete_option = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='subjects-auto-complete__option']"))
        )
        autocomplete_option.click()
        
        # 7. Select hobbies (checkboxes)
        hobbies = ["Sports", "Music"]
        for hobby in hobbies:
            hobby_checkbox = driver.find_element(By.XPATH, f"//label[text()='{hobby}']")
            hobby_checkbox.click()
        
        # 8. Upload file
        file_upload = driver.find_element(By.ID, "uploadPicture")
        # file_upload.send_keys("/path/to/your/file.jpg")  # Uncomment with actual path
        
        # 9. Fill address
        driver.find_element(By.ID, "currentAddress").send_keys("123 Main Street, City, Country")
        
        # 10. Select state and city (dropdown with search)
        state_dropdown = driver.find_element(By.CSS_SELECTOR, "#state .css-1hwfws3")
        state_dropdown.click()
        
        state_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='NCR']")))
        state_option.click()
        
        city_dropdown = driver.find_element(By.CSS_SELECTOR, "#city .css-1hwfws3")
        city_dropdown.click()
        
        city_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Delhi']")))
        city_option.click()
        
        # 11. Take screenshot before submission
        driver.save_screenshot("before_submit.png")
        
        # 12. Submit form
        submit_button = driver.find_element(By.ID, "submit")
        driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        submit_button.click()
        
        # 13. Handle modal confirmation
        modal = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "modal-content")))
        
        # Take screenshot of results
        driver.save_screenshot("form_submitted.png")
        
        # Close modal
        close_button = driver.find_element(By.ID, "closeLargeModal")
        close_button.click()
        
        print("Form submission completed successfully!")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        driver.save_screenshot("error_screenshot.png")
    
    finally:
        driver.quit()

# Run the example
if __name__ == "__main__":
    comprehensive_automation_example()
```

## Best Practices

1. **Always use explicit waits** instead of time.sleep()
2. **Clean up resources** with driver.quit()
3. **Handle exceptions** gracefully
4. **Use meaningful element locators** (ID > CSS > XPath)
5. **Take screenshots** for debugging
6. **Implement page object pattern** for larger projects
7. **Use configuration files** for test data
8. **Run tests in headless mode** for CI/CD

This guide covers all the major Selenium concepts you'll need for web automation. Each section can be expanded based on your specific use cases and requirements.