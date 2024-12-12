from selenium import webdriver
from selenium.webdriver.common.by import By
from pageobjects.page_homepage import page_homepage
from pageobjects.book1_imagepage import book1_imagepage
from pageobjects.account_registration import page_acc_register
import pytest
import time
import os
from utilities import randomstring
from utilities.readproperties import readconfig
from utilities.customlogger import log_gen

class Test_hp_desc():
    logger = log_gen.loggen()   #logger initialisation
    burl = readconfig.get_url() #getting the base url from the configurations file
    def test_desc(self,setup):
        try:
            self.driver = setup
            #log file informations
            self.logger.info('****Testcase4_description Started****')
            self.driver.get(self.burl)
            self.driver.maximize_window()
            time.sleep(30)
            #creating the object for the page_homepage class
            self.hp = page_homepage(self.driver)
            self.hp.image_click()
            #creating the object for the imagepage class
            self.b1p=book1_imagepage(self.driver)
            self.b1p.click_description()
            #calling the method to confirm the required description is there
            self.b1p.check_description()
            #self.driver.close()
            time.sleep(20)
            assert True

        finally:
            self.driver.close()
