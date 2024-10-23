import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogInMsb:

    # Locator for Login Page
    msb_phone_number = (By.ID, "mobileNumber")
    msb_password = (By.ID, "password")
    msb_login_button = (By.XPATH, "//button[@type='submit']")

    # Initializing Driver
    def __init__(self, driver):
        self.driver = driver

    # Method for Wait for Elements (Explicitly)
    def wait_explicitly_for_visibility_element(self, element):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.visibility_of_element_located(element))

    # Enter the Phone Number for Login Page
    def enter_phone_number(self, phone_number):
        self.wait_explicitly_for_visibility_element(LogInMsb.msb_phone_number).send_keys(phone_number)

    # Enter the Password for Login Page
    def enter_password(self, password):
        self.wait_explicitly_for_visibility_element(LogInMsb.msb_password).send_keys(password)

    # Clicking on Button for Login Page
    def click_login_button(self):
        self.wait_explicitly_for_visibility_element(LogInMsb.msb_login_button).click()

    # Get the Page Title after Login Page
    def get_home_page_title(self):
        time.sleep(2)
        return self.driver.title
