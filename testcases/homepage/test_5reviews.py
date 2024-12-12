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

class Test_hp_reviews():
    logger = log_gen.loggen()   #logger initialisation
    burl = readconfig.get_url() #getting the base url from the configurations file
    def test_reviews(self,setup):
        self.driver = setup
        #informtions for the log file
        self.logger.info('****Testcase5_reviews Started****')
        self.driver.get(self.burl)
        self.driver.maximize_window()
        time.sleep(30)
        #using try......finally  to handle the exceptions
        try:
            self.hp = page_homepage(self.driver)
            self.hp.image_click()
            self.b1p=book1_imagepage(self.driver)
            # click the description and check if it is there
            self.b1p.click_description()
            self.b1p.check_description()
            # click the review and the check, reviews are there
            self.b1p.click_reviews()
            self.b1p.check_reviews()

            time.sleep(20)
            assert True
        finally:
            self.driver.close()
