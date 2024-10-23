from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BillingPage:

    # Locator for BILLING PAGE
    select_project_locator = (By.XPATH, "//div/mbc-projects-card")
    select_check_out_page_locator = (By.XPATH, "//datatable-row-wrapper[@class='datatable-row-wrapper']")
    company_name_locator = (By.XPATH, "//div[@class='quote-details-data flex-grow-1']/label[@class='name']")
    company_address_Locator = (By.XPATH, "//div[@class='quote-details-data flex-grow-1']/label[@class='name']/following-sibling::label[1]")
    company_contact_locator = (By.XPATH, "//div[@class='quote-details-data flex-grow-1']/label[@class='name']/following-sibling::label[2]")
    all_content = (By.XPATH, "//tr[@class='empty-row text-danger']/following-sibling::tr")

    # Creating list to store the values fetched
    item_content_list = []
    item_sr_no_list = []
    item_name_list = []
    item_quantity_list = []
    item_rate_list = []
    item_total_list = []

    # Initializing driver
    def __init__(self, driver):
        self.driver = driver

    # Method for WAIT for element (Explicitly)
    def wait_explicitly_for_visibility_of_element(self, element):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.visibility_of_element_located(element))

    # Method for WAIT for elements (Explicitly)
    def wait_explicitly_for_visibility_of_elements(self, elements):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.visibility_of_all_elements_located(elements))

    # To store the element to get Screenshot
    def content_for_screen_shot(self, index_c_ss):
        return BillingPage.item_content_list[index_c_ss]

    # To store the value for item Serial no.
    def item_sr_no_fetch(self, index_sr_no):
        return BillingPage.item_sr_no_list[index_sr_no]

    # To store the value for item Name
    def item_name_fetch(self, index_i_name):
        return BillingPage.item_name_list[index_i_name]

    # To store the value for item Quantity
    def item_quantity_fetch(self, index_i_quantity):
        return BillingPage.item_quantity_list[index_i_quantity]

    # To store the value for item Rate
    def item_rate_fetch(self, index_i_rate):
        return BillingPage.item_rate_list[index_i_rate]

    # To store the value for item Total Amount
    def item_total_amount_fetch(self, index_i_total):
        return BillingPage.item_total_list[index_i_total]

    # Selecting the Project Name to land on Billing Page
    def select_project(self, project_name):
        # Getting all the Project Names to land on Billing Page
        projects = self.wait_explicitly_for_visibility_of_elements(BillingPage.select_project_locator)
        # Looping all the Project Names to Project Name to land on Billing Page
        for p_c in range(1, len(projects)+1):
            # Getting Project Name to land to Billing Page
            project = self.driver.find_element(By.XPATH, "//div/mbc-projects-card["+str(p_c)+"]/div/div/div[1]/div/h6[1]/span").text
            # Selecting the Project Name to land to Billing Page
            if project == project_name:
                self.driver.find_element(By.XPATH, "//div/mbc-projects-card[" + str(p_c) + "]").click()
                break

    # Selecting the Bill Type to land on Billing Page
    def select_check_out_page(self, check_out_name):
        # Getting all the Bill types to land on Billing Page
        check_out_pages = self.wait_explicitly_for_visibility_of_elements(BillingPage.select_check_out_page_locator)
        # Looping all the Bill Types to Bill Type to land on Billing Page
        for cop_c in range(1, len(check_out_pages)+1):
            # Getting Bill Type to land to Billing Page
            check_out_page = self.driver.find_element(By.XPATH, "//datatable-row-wrapper[@class='datatable-row-wrapper']["+str(cop_c)+"]/datatable-body-row/div[2]/datatable-body-cell[2]").text
            # Selecting the Bill Type to land to Billing Page
            if check_out_page == check_out_name:
                self.driver.find_element(By.XPATH,"//datatable-row-wrapper[@class='datatable-row-wrapper']["+str(cop_c)+"]").click()
                break

    # Getting the Company Details on Billing Page
    def get_company_details(self):
        company_name = self.wait_explicitly_for_visibility_of_element(BillingPage.company_name_locator).text
        company_contact = self.wait_explicitly_for_visibility_of_element(BillingPage.company_contact_locator).text
        company_address = self.wait_explicitly_for_visibility_of_element(BillingPage.company_address_Locator).text
        return f"{company_name} , {company_contact}, {company_address}"

    # Calculation on the Billing Page
    def billing_calculations(self):
        # Getting all the content on Billing Page
        all_content = self.driver.find_elements(By.XPATH, "//tr[@class='empty-row text-danger']/following-sibling::tr")
        # Looping all the contents to get the content on Billing Page
        for all_c in range(1, len(all_content) + 1):
            item_sr_no_s = self.wait_explicitly_for_visibility_of_element((By.XPATH, "//tr/following-sibling::tr[" + str(all_c) + "]/td[@id='sr-no']"))
            self.driver.execute_script("arguments[0].scrollIntoView();", item_sr_no_s)
            # Getting content for Screenshot on Billing Page
            content_c = self.driver.find_element(By.XPATH, "//tr/following-sibling::tr[" + str(all_c) + "]")
            # Getting all the Item Serial Numbers on Billing Page
            item_sr_no_c = self.driver.find_element(By.XPATH, "//tr/following-sibling::tr[" + str(all_c) + "]/td[@id='sr-no']").text
            # Getting all the Item Names on Billing Page
            item_name_c = self.driver.find_element(By.XPATH, "//tr/following-sibling::tr[" + str(all_c) + "]/td[@id='item-name']").text.split('\n')[0]
            # Getting all the Item Quantities  on Billing Page
            item_quantity_c = self.driver.find_element(By.XPATH, "//tr/following-sibling::tr[" + str(all_c) + "]/td[@id='quantity']").text
            # Getting all the Item Rates on Billing Page
            item_rate_c = self.driver.find_element(By.XPATH, "//tr/following-sibling::tr[" + str(all_c) + "]/td[@id='rate']").text.replace(',', '')
            # Getting all the Item totals on Billing Page
            item_total_c = self.driver.find_element(By.XPATH, "//tr/following-sibling::tr[" + str(all_c) + "]/td[@id='total']").text.replace(',', '')
            # Getting all the Items if Serial Number is a Digit
            if item_sr_no_c.isdigit():
                # Getting all the Item Content in the List
                BillingPage.item_content_list.append(content_c)
                # Getting all the Item Serial Number in the List
                BillingPage.item_sr_no_list.append(item_sr_no_c)
                # Getting all the Item Name in the List
                BillingPage.item_name_list.append(item_name_c)

                # Converting the Item Quantity from String to Float
                item_quantity_f = float(item_quantity_c)
                # Rounding the Float for Item Quantity value upto 2 decimal value
                item_quantity_r = round(item_quantity_f, 2)
                # Getting all the Item Quantity in the List
                BillingPage.item_quantity_list.append(item_quantity_r)

                # Converting the Item Rate from String to Float
                item_rate_f = float(item_rate_c)
                # Rounding the Float for Item Rate value upto 2 decimal value
                item_rate_r = round(item_rate_f, 2)
                # Getting all the Item Rate in the List
                BillingPage.item_rate_list.append(item_rate_r)

                # Converting the Item Total from String to Float
                item_total_f = float(item_total_c)
                # Rounding the Float for Item Total value upto 2 decimal value
                item_total_r = round(item_total_f, 2)
                # Getting all the Item Total in the List
                BillingPage.item_total_list.append(item_total_r)
