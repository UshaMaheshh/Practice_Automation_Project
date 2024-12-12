from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.dom import scroll_into_view_if_needed
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


class Test_shoppage():
    logger = log_gen.loggen()   #for logging
    burl = readconfig.get_url() #for getting the base url
    def test_homepage(self,setup):
        self.driver = setup     #for chrome driver setup
        self.logger.info('****Testcase_shop by product categary****')
        self.driver.get(self.burl)
        self.driver.maximize_window()
        time.sleep(5)

        self.hp = page_homepage(self.driver)    #object creation for page_homepage class
        self.hp.shop_click()

        self.sp = shoppage_elements(self.driver) #object creation for shoppage_elements class
        self.sp.product_android()
        time.sleep(10)
        self.sp.product_html()
        time.sleep(10)
        # Scroll the element into view if needed
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(By.XPATH,
                                                                                             "//*[@id='woocommerce_product_categories-2']/ul/li[1]/a"))
        self.sp.product_javascript()
        time.sleep(10)
        # Scroll the window
        self.driver.execute_script("window.scrollBy(0, 200);")
        self.sp.product_selenium()
        time.sleep(10)

        assert True
        self.driver.close()

