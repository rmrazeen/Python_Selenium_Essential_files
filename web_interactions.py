from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time


def setup_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver


def fill_text_inputs(driver):
    driver.get("https://demoqa.com/text-box")
    time.sleep(1)
    name_text = driver.find_element(By.ID, "userName")
    name_text.send_keys("Ehsanul Haque")
    time.sleep(1)
    email_text = driver.find_element(By.ID, "userEmail")
    email_text.send_keys("ehsan@example.com")
    time.sleep(1)
    driver.find_element(By.ID, "currentAddress").send_keys("Dhaka, Bangladesh")
    time.sleep(1)
    address = driver.find_element(By.ID, "permanentAddress")
    address.send_keys("Dhaka, Bangladesh")
    driver.find_element(By.ID, "submit").click()
    time.sleep(1)

    output_name = driver.find_element(By.ID, "name")
    assert "123" in output_name.text, "Name not found in output"

    print(" Text input filled and submitted.")


def handle_radio(driver):
    # Radio Button
    driver.get("https://demoqa.com/radio-button")
    time.sleep(2)
    radio_btn = driver.find_element(By.XPATH, "//*[@for='yesRadio']")
    radio_btn.click()
    output = driver.find_element(By.XPATH, "//span[@class='text-success']").text
    assert output == "Yes1", "Radio button selection failed"
    print(" Radio button selected.")
    time.sleep(1)


def handle_checkbox(driver):
    # Checkbox
    driver.get("https://demoqa.com/checkbox")
    time.sleep(1)
    checkbox = driver.find_element(By.XPATH, "//input[@id='tree-node-home']/parent::label")
    checkbox.click()
    time.sleep(1)
    result = driver.find_element(By.ID, "result").text
    assert "desktop" in result.lower(), "Checkbox selection failed"
    time.sleep(1)
    print(" Checkbox selected.")


def handle_buttons(driver):
    driver.get("https://demoqa.com/buttons")
    time.sleep(1)
    action = ActionChains(driver) #ActionChains is a Selenium utility that allows you to perform advanced user interactions

    double_btn = driver.find_element(By.ID, "doubleClickBtn")
    right_btn = driver.find_element(By.ID, "rightClickBtn")

    time.sleep(1)
    action.double_click(double_btn).perform()
    time.sleep(1)
    action.context_click(right_btn).perform()

    dbl_msg = driver.find_element(By.ID, "doubleClickMessage").text
    rgt_msg = driver.find_element(By.ID, "rightClickMessage").text

    assert "double click" in dbl_msg, " Double click failed"
    assert "right click" in rgt_msg, " Right click failed"
    time.sleep(1)

    print(" Double-click and right-click handled.")


def hover_action(driver):
    driver.get("https://demoqa.com/tool-tips")
    time.sleep(1)
    hover_btn = driver.find_element(By.ID, "toolTipButton")
    action = ActionChains(driver) #ActionChains is a Selenium utility that allows you to perform advanced user interactions
    action.move_to_element(hover_btn).perform()
    time.sleep(1)
    print(" Mouse hover performed successfully.")


def upload_file(driver):
    driver.get("https://demoqa.com/upload-download")
    file_input = driver.find_element(By.ID, "uploadFile")
    time.sleep(1)
    file_input.send_keys(__file__)
    uploaded_path = driver.find_element(By.ID, "uploadedFilePath").text
    assert uploaded_path.endswith("web_interactions.py"), " File not uploaded"
    # Uploads this script file itself
    print(" File uploaded.")


def handle_simple_alert(driver):
    driver.get("https://demoqa.com/alerts")
    alert_btn = driver.find_element(By.ID, "alertButton")
    alert_btn.click()
    time.sleep(1)
    # WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert "You clicked a button" in alert.text, "Alert not found"
    alert.accept()
    print("Simple alert handled.")


def handle_timed_alert(driver):
    driver.get("https://demoqa.com/alerts")
    alert_btn = driver.find_element(By.ID, "timerAlertButton")
    alert_btn.click()
    time.sleep(10)
    # wait = WebDriverWait(driver,10)
    # wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert "This alert appeared after 5 seconds" in alert.text
    time.sleep(1)
    alert.accept()
    print("Timed alert handled.")


def handle_confirm_alert(driver):
    driver.get("https://demoqa.com/alerts")
    alert_btn = driver.find_element(By.ID, "confirmButton")
    alert_btn.click()
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert "Do you confirm action?" in alert.text
    time.sleep(1)
    # alert.dismiss()
    alert.accept()
    result = driver.find_element(By.ID, "confirmResult").text
    # assert "Cancel" in result
    assert "Ok" in result
    print("Confirmation alert handled with Cancel.")


def handle_prompt_alert(driver):
    driver.get("https://demoqa.com/alerts")
    driver.find_element(By.ID, "promtButton").click()
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert "Please enter your name" in alert.text
    alert.send_keys("Ehsan")
    time.sleep(2) #For better visualization of the alert for a student
    alert.accept()
    result = driver.find_element(By.ID, "promptResult").text
    assert "Ehsan" in result
    print("Prompt alert handled with input.")


def wait_for_enable_button(driver):
    driver.get("https://demoqa.com/dynamic-properties")

    # Wait until the button becomes enabled
    enable_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "enableAfter"))
    )
    assert enable_btn.is_enabled(), "Button did not become enabled."
    enable_btn.click()
    print("Enable After 5 Seconds' button clicked.")


def wait_for_visible_button(driver):
    driver.get("https://demoqa.com/dynamic-properties")

    # Wait until the button becomes visible
    visible_btn = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "visibleAfter"))
    )
    assert visible_btn.is_displayed(), "Button did not appear."
    time.sleep(1) #For better visualization of the alert for a student
    visible_btn.click()
    print("'Visible After 5 Seconds' button appeared.")


def check_color_change(driver):
    driver.get("https://demoqa.com/dynamic-properties")

    # Get color before change
    color_btn = driver.find_element(By.ID, "colorChange")
    initial_class = color_btn.get_attribute("class")

    time.sleep(6)  # Wait more than 5s for the change to happen
    updated_class = color_btn.get_attribute("class")

    assert initial_class != updated_class, "Button color did not change."
    print("'Color Change' button")


def navigation_example(driver):
    driver.get("https://demoqa.com")
    time.sleep(2)  #for better visibility for student
    driver.get("https://demoqa.com/text-box")


    time.sleep(1)   #for better visibility for student
    driver.back()
    assert driver.current_url == "https://demoqa.com/", driver.current_url+" is the current url"
    print(driver.current_url)
    time.sleep(2)   #for better visibility for student


    driver.forward()
    print(driver.current_url)
    assert driver.current_url == "https://demoqa.com/text-box", driver.current_url+" is the current url"
    time.sleep(2)   #for better visibility for student


    driver.refresh()
    print(driver.current_url)
    time.sleep(2)   #for better visibility for student
    assert driver.current_url == "https://demoqa.com/text-box", driver.current_url+" is the current url"
    print(" Browser navigation complete.")



def take_screenshot(driver):
    driver.get("https://demoqa.com")
    driver.save_screenshot("full_page_demoqa.png")
    print(" Screenshot saved as 'full_page_demoqa.png'")


# ================== Dropdown =================================
def select_value_dropdown(driver):
    driver.get("https://demoqa.com/select-menu")
    dropdown = driver.find_element(By.XPATH, "//div[@id='withOptGroup']")
    dropdown.click()
    # //div[contains(@class,'placeholder')]
    option = driver.find_element(By.XPATH, "//div[text()='Group 2, option 1']")
    option.click()
    print(" Selected value from 'Select Value' dropdown.")


def select_one_dropdown(driver):
    driver.get("https://demoqa.com/select-menu")
    dropdown = driver.find_element(By.XPATH, "//div[@id='selectOne']//div[contains(@class,'placeholder')]")
    dropdown.click()
    option = driver.find_element(By.XPATH, "//div[text()='Dr.']")
    option.click()
    print("Selected value from 'Select One' dropdown.")


def old_style_select(driver):
    driver.get("https://demoqa.com/select-menu")
    select_element = Select(driver.find_element(By.ID, "oldSelectMenu"))
    select_element.select_by_visible_text("Magenta")
    selected_option = select_element.first_selected_option.text
    assert selected_option == "Magenta"
    print("Selected from old-style select dropdown.")


def multiselect_custom(driver):
    driver.get("https://demoqa.com/select-menu")
    multi_dropdown = driver.find_element(By.XPATH, "//div[contains(text(), 'Select...') and contains(@class, 'placeholder')]")
    multi_dropdown.click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[text()='Green']").click()
    driver.find_element(By.XPATH, "//div[text()='Black']").click()
    print("Selected multiple items from custom multi-select dropdown.")

# =============== Modal ============================================
def handle_small_modal(driver):
    driver.get("https://demoqa.com/modal-dialogs")
    time.sleep(1) #For better visualization of the alert for a student

    # Click the button to open small modal
    driver.find_element(By.ID, "showSmallModal").click()

    # Wait for modal to appear
    modal_title = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-sm"))
    )
    assert modal_title.text == "Small Modal", " Small modal title incorrect"
    print(" Small modal is visible with title: ", modal_title.text)

    # Close the modal
    time.sleep(1) #For better visualization of the alert for a student
    driver.find_element(By.ID, "closeSmallModal").click()

    # Optionally wait for modal to close (using invisibility_of_element)
    WebDriverWait(driver, 5).until(
        EC.invisibility_of_element_located((By.ID, "example-modal-sizes-title-sm"))
    )
    print("Small modal closed.")


def handle_large_modal(driver):
    driver.get("https://demoqa.com/modal-dialogs")
    time.sleep(1) #For better visualization of the alert for a student

    # Click the button to open large modal
    driver.find_element(By.ID, "showLargeModal").click()

    # Wait for modal to appear
    modal_title = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
    )
    assert modal_title.text == "Large Modal", " Large modal title incorrect"
    print(" Large modal is visible with title:", modal_title.text)

    # Close the modal
    time.sleep(1) #For better visualization of the alert for a student
    driver.find_element(By.ID, "closeLargeModal").click()

    # Optionally wait for modal to close
    WebDriverWait(driver, 5).until(
        EC.invisibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
    )
    print(" Large modal closed.")


# ======================== Browser Windows Handling ========================
def handle_new_tab(driver):
    driver.get("https://demoqa.com/browser-windows")
    time.sleep(1) #For better visualization of the alert for a student

    original_window = driver.current_window_handle
    newtab_btn = driver.find_element(By.ID, "tabButton")
    newtab_btn.click()
    time.sleep(1) #For better visualization of the alert for a student

    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

    # Switch to the new tab
    for handle in driver.window_handles:
        if handle != original_window:
            driver.switch_to.window(handle)
            break

    # Check content
    text = driver.find_element(By.ID, "sampleHeading").text
    assert "This is a sample page" in text, "Tab content incorrect"
    print(" New tab opened and verified.")

    driver.close()
    driver.switch_to.window(original_window)
    assert driver.current_url == "https://demoqa.com/browser-windows", "Current URL incorrect"
    print("Current URL:", driver.current_url)


# =================== Date picker ================================
def select_date(driver):
    driver.get("https://demoqa.com/date-picker")
    date_input = driver.find_element(By.ID, "datePickerMonthYearInput")
    date_input.click()

    # Select month
    month_dropdown = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
    month_dropdown.select_by_visible_text("May")

    # Select year
    year_dropdown = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
    year_dropdown.select_by_visible_text("2025")

    time.sleep(3)

    # Select day
    day_xpath = "//div[text()='11']"
    day_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, day_xpath)))
    day_element.click()

    # Assertion
    selected_date = date_input.get_attribute("value")
    assert selected_date == "05/11/2025", f"Date not selected properly: {selected_date}"
    print(" Date selected: ", selected_date)


def main():
    driver = setup_driver()
    try:
        # fill_text_inputs(driver)
        # handle_radio(driver)
        # handle_checkbox(driver)
        # handle_buttons(driver)
        # hover_action(driver)
        # upload_file(driver)
        # handle_simple_alert(driver)
        # handle_timed_alert(driver)
        # handle_confirm_alert(driver)
        # handle_prompt_alert(driver)
        # wait_for_enable_button(driver)
        # wait_for_visible_button(driver)
        # check_color_change(driver)
        # navigation_example(driver)
        # take_screenshot(driver)
        # select_value_dropdown(driver)
        # select_one_dropdown(driver)
        # old_style_select(driver)
        # multiselect_custom(driver)
        # handle_small_modal(driver)
        # handle_large_modal(driver)
        handle_new_tab(driver)
        # select_date(driver)
        print("All tests completed successfully.")
    finally:
        time.sleep(2)
        driver.quit()
        print("Browser closed.")


if __name__ == "__main__":
    main()
