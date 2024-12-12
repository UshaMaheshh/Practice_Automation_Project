from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.dom import scroll_into_view_if_needed
from selenium.webdriver.support.wait import WebDriverWait

from utilities.customlogger import log_gen
from pageobjects.page_homepage import page_homepage
from pageobjects.shop_page import shoppage_elements
from pageobjects.account_registration import page_acc_register
import pytest
import time
import os
from utilities.customlogger import log_gen
from utilities import randomstring
from utilities.readproperties import readconfig
import logging
from selenium.webdriver.support import expected_conditions as EC



class Test_shoppage():
    logger = log_gen.loggen()   #for logging
    burl = readconfig.get_url() #for getting the base url
    def test_homepage(self,setup):
        self.driver = setup     #for chromedriver setup

        self.logger.info('****Testcase_shop by product categary****')
        self.driver.get(self.burl)
        self.driver.maximize_window()
        time.sleep(5)

        # try...finally block for exception handling
        try:
    # 2. Click on Shop Menu
            shop_menu = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Shop"))
                )
            shop_menu.click()
            time.sleep(3)  # Allow time for the page to load

            self.driver.execute_script("window.scrollTo(0,300)")
    # 3. Click on the Sale product
            sale_product = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//span[text()='Sale!']"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", sale_product)

            sale_product.click()
            time.sleep(30)  # Allow time for the page to load

    # 4. Verify the pricing details
            actual_price = self.driver.find_element(By.XPATH, "//*[@id='product-169']//ins/span").text

            old_price = self.driver.find_element(By.XPATH, "//*[@id='product-169']//del/span").text

            print(f"Actual Price: {actual_price}")
            print(f"Old Price: {old_price}")
            #old_price=driver.find_element(By.XPATH,"//*[@id='product-169']/div[2]/div[2]/p/del/span/text()")
            old_pri = self.driver.find_element(By.XPATH, "//*[@id='product-169']//del/span")

            #line - through
            oldprice= old_pri.value_of_css_property("-webkit-text-decorations-in-effect")
            print(oldprice)

            # Check if the old price is stricken through
            if 'line-through' in oldprice:
                print("The old price is correctly stricken through.")
            else:
                print("The old price is not stricken through.")
            # print(driver.find_element(By.XPATH, "//*[@id='product-169']//del/span").get_attribute("outerHTML"))
        finally:
            time.sleep(5)  # Wait to see the results
            self.driver.close()
            # Close the browser
