from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

class check_gateway_page:
            # Locators for Home Page
    firstname_id = "billing_first_name"
    lastname_id = "billing_last_name"
    company_id = "billing_company"
    email_id = "billing_email"
    phone_id = "billing_phone"
    address1_id="billing_address_1"
    address2_id = "billing_address_2"
    towncity_id = "billing_city"
    postcode_id = "billing_postcode"
    stcountry_xpath= "//*[@id='s2id_billing_state']"
    country_xpath ="//*[@id='select2-chosen-1']"
    billingtext_xpath= "//*[@id='customer_details']/div[1]/div/h3"

    def __init__(self, driver):
        self.driver = driver


                # Actions on Home Page
    def enter_firstname(self, fname):
        self.driver.find_element(By.ID, self.firstname_id).clear()
        self.driver.find_element(By.ID,self.firstname_id).send_keys(fname)

    def enter_lastname(self,lname):
        self.driver.find_element(By.ID, self.lastname_id).clear()
        self.driver.find_element(By.ID,self.lastname_id).send_keys(lname)

    def enter_company(self,company):
        self.driver.find_element(By.ID,self.company_id).clear()
        self.driver.find_element(By.ID, self.company_id).send_keys(company)

    def enter_email(self, email):
        self.driver.find_element(By.ID,self.email_id).clear()
        self.driver.find_element(By.ID, self.email_id).send_keys(email)

    def enter_phoneno(self, phone):
        self.driver.find_element(By.ID,self.phone_id).clear()
        self.driver.find_element(By.ID, self.phone_id).send_keys(phone)

    def enter_address1(self,address1):
        self.driver.find_element(By.ID,self.address1_id).clear()
        self.driver.find_element(By.ID, self.address1_id).send_keys(address1)

    def enter_address2(self,address2):
        self.driver.find_element(By.ID,self.address2_id).clear()
        self.driver.find_element(By.ID, self.address2_id).send_keys(address2)

    def enter_towncity(self,towncity):
        self.driver.find_element(By.ID,self.towncity_id).clear()
        self.driver.find_element(By.ID, self.towncity_id).send_keys(towncity)

    def enter_postcode(self,postcode):
        self.driver.find_element(By.ID,self.postcode_id).clear()
        self.driver.find_element(By.ID, self.postcode_id).send_keys("22222")

    def enter_country(self,country):
        ddn = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.country_xpath))
        )
        ddn.click()
        search_box = self.driver.find_element(By.XPATH, "//*[@id='s2id_autogen1_search']")
        search_box.send_keys(country)
        time.sleep(1)
        # Wait for the options to be visible
        options = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='select2-results']/li"))
        )

        # Flag to check if a matching option is found
        match_found = False

        for option in options:
          #   Check if the option text starts with the country name
            if option.text.strip().startswith(country):
                option.click()  # Click the matched option
                match_found = True
                break

        if not match_found:
           print(f'No match for {"India"} found in the dropdown.')



    def enter_stcountry(self,state):
            dropdown = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, self.stcountry_xpath))
              )
            dropdown.click()

            self.driver.find_element(By.XPATH, "//input[@id='s2id_autogen2_search']").send_keys(state + Keys.ENTER)

    def payment_method(self):
        self.driver.find_element(By.XPATH,"//*[@id='payment_method_cod']").click()
        time.sleep(20)

    def place_order(self):
        self.driver.find_element(By.XPATH, "//*[@id='place_order']").click()
        try:
            message_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'woocommerce-thankyou-order-received'))
            )
            print(message_element.text)  # Should print: Thank you. Your order has been received.
        except Exception as e:
            print(f"Error: {e}")


