from selenium import webdriver
from selenium.webdriver.common.by import By
from pageobjects.page_homepage import page_homepage
from pageobjects.account_registration import page_acc_register
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import os
from utilities import randomstring
from utilities.readproperties import readconfig
from utilities.customlogger import log_gen

class Test_hp_abaskt():
    logger = log_gen.loggen()   #logger initialisation
    burl = readconfig.get_url() #from the configuration file getting the base url
    def test_abaskt(self,setup):
        # try....finally for handling the exceptions
        try:
            self.driver = setup
            self.logger.info('****Testcase6_abasket Started****')
            self.driver.get(self.burl)
            self.driver.maximize_window()
            time.sleep(30)
            self.hp = page_homepage(self.driver) #object for the page_homepage class
            self.hp.add_basket()
            self.hp.view_basket()
            #explicit wait for finding the linktext "Selenium Ruby"
            if WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Selenium Ruby"))):
                print("Successfully Added to Basket")
                assert True
        finally:
                time.sleep(3)
                self.driver.close()
