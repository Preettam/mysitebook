import pytest
import pytest_check as check
from pageObjects.login_msb import LogInMsb
from pageObjects.billing_page_msb import BillingPage
from utilities.readproperties import Readconfig
from utilities.loggers import LoggingClass

class TestMsb:

    # Reading value from Config File for Login
    test_home_page_title = Readconfig.get_homepage_title()
    test_url = Readconfig.get_url()
    test_phone = Readconfig.get_phone_number()
    test_password = Readconfig.get_password()

    # Reading value from Config File for Billing
    test_select_project = Readconfig.get_sample_project_name()
    test_check_out_page = Readconfig.get_check_out_title()

    # Generating Loggers
    log = LoggingClass.log_generator()

    @pytest.fixture
    def login_msb(self, setup):
        self.driver = setup
        self.log.info("Setting up the browser ")
        self.driver.get(self.test_url)
        self.log.info("Opening the URL -----> " + self.test_url)
        self.log.info("Creating object for login ")
        self.msb_lg_in = LogInMsb(self.driver)
        self.log.info("Entering the PHONE NUMBER -----> " + self.test_phone)
        self.msb_lg_in.enter_phone_number(TestMsb.test_phone)
        self.log.info("Clicking on CONTINUE BUTTON ")
        self.msb_lg_in.click_login_button()
        self.log.info("Entering the PASSWORD -----> " + self.test_password)
        self.msb_lg_in.enter_password(TestMsb.test_password)
        self.log.info("Clicking on LOGIN BUTTON ")
        self.msb_lg_in.click_login_button()

    def test_home_page(self, login_msb):
        self.log.info("Testing the PAGE TITLE -----> " + self.test_home_page_title + " = " + self.msb_lg_in.get_home_page_title())
        assert self.msb_lg_in.get_home_page_title() == TestMsb.test_home_page_title

    def test_bill_page(self, login_msb):
        self.log.info("Setting up the browser ")
        self.bill_pg = BillingPage(self.driver)
        self.log.info("Selecting the PROJECT -----> " + self.test_select_project)
        self.bill_pg.select_project(self.test_select_project)
        self.log.info("Selecting the CHECKOUT -----> " + self.test_check_out_page)
        self.bill_pg.select_check_out_page(self.test_check_out_page)
        self.log.info("Company Details -----> " + self.bill_pg.get_company_details())
        self.bill_pg.get_company_details()
        self.log.info("Getting Details for Calculations ")
        # time.sleep(2)
        self.bill_pg.billing_calculations()
        self.log.info("Getting Length of all items -----> " + str(len(self.bill_pg.item_sr_no_list)))
        for i in range(len(self.bill_pg.item_sr_no_list)):
            actual_result = self.bill_pg.item_total_amount_fetch(i)
            self.log.info("Actual Result: " + str(actual_result))
            expected_result = self.bill_pg.item_quantity_fetch(i) * self.bill_pg.item_rate_fetch(i)
            self.log.info("Expected Result: " + str(expected_result))
            self.log.info("Comparing the Test ----->" + str(actual_result) + " vs " + str(expected_result))
            if actual_result == expected_result:
                self.log.info("Test Result -----> " + str(actual_result) + " is Equal " + str(expected_result) + "-----> TEST PASSED")
                check.is_true(actual_result == expected_result, "TEST PASSED")
            else:
                self.log.info("Test Result -----> " + str(actual_result) + " is NOT Equal " + str(expected_result) + "-----> TEST FAILED")
                check.is_false(actual_result == expected_result, "TEST FAILED")
                self.log.info("Total should be -----> " + str(expected_result))
                path_screen_shot = f"D:\\Peettam\\MySiteBook\\Screenshots\\{self.bill_pg.item_sr_no_fetch(i)}_{self.bill_pg.item_name_fetch(i)}.png"
                self.bill_pg.content_for_screen_shot(i).screenshot(path_screen_shot)
            self.log.info("*************************************************************************************************")
