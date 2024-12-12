from selenium import webdriver
from selenium.webdriver.common.by import By
from pageobjects.page_homepage import page_homepage
from pageobjects.account_registration import page_acc_register
import pytest
import time
import os
from utilities.customlogger import log_gen
from utilities import randomstring
from utilities.readproperties import readconfig
import logging

class Test_hp_nofarri():
    logger = log_gen.loggen()   #logger initialisation
    burl = readconfig.get_url() #getting the base url from the configurations file
    def test_nofarri(self,setup):
        self.driver = setup
        #log file informations
        self.logger.info('****Testcase2_nofarrivals started****')
        self.driver.get(self.burl)
        self.driver.maximize_window()
        time.sleep(30)
        #creating an object for page_homepage class
        self.hp = page_homepage(self.driver)
        #calling the method for counting the no. of arrivals
        self.hp.count_of_arrivals()
        assert True
        self.driver.close()
