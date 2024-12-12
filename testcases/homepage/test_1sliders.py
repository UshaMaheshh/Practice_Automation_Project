from selenium import webdriver
from selenium.webdriver.common.by import By
from pageobjects.page_homepage import page_homepage
from pageobjects.account_registration import page_acc_register
import pytest
import time
import os
from utilities import randomstring
from utilities.readproperties import readconfig
import logging
from utilities.customlogger import log_gen

class Test_hp_sliders():
    logger = log_gen.loggen()   #logger intialisation
    burl= readconfig.get_url()  #getting the base url of the configuration file
    def test_sliders(self,setup):
        self.driver = setup
        #log file informations
        self.logger.info('****Testcase1_sliders Started****')
        self.driver.get(self.burl)
        self.driver.maximize_window()
        time.sleep(30)
        # creating object for page_homepage class
        self.hp = page_homepage(self.driver)
        self.hp.count_of_sliders()
        # saving the screenshot in a .png file
        self.driver.save_screenshot(os.path.abspath("C:\\Users\\usha5\\PycharmProjects\\PracticeProject2\\screenshots\\testsliders.png"))
        assert True
        self.driver.close()
