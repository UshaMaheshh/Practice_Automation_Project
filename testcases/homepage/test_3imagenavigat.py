from selenium import webdriver
from selenium.webdriver.common.by import By
from pageobjects.page_homepage import page_homepage
from pageobjects.account_registration import page_acc_register
import pytest
import time
import os
from utilities import randomstring
from utilities.readproperties import readconfig
from utilities.customlogger import log_gen

class Test_hp_imagenv():
    logger = log_gen.loggen()   #logger initilisation
    burl = readconfig.get_url() #getting the base url from the configuration file
    def test_imagenv(self,setup):
        self.driver = setup
        #log file informations
        self.logger.info('****Testcase3_imagenavigation Started****')
        self.driver.get(self.burl)
        self.driver.maximize_window()
        time.sleep(30)
        #creating the object for the page_homepage class
        self.hp = page_homepage(self.driver)
        #calling the method for checking the image navigation
        book1title=self.hp.image_navigate()
        if book1title == "Selenium Ruby":
            print("Navigation is successful")
            assert True
        #go back to the previous page
        self.driver.find_element(By.LINK_TEXT,"Home").click()
        time.sleep(30)
        self.driver.close()