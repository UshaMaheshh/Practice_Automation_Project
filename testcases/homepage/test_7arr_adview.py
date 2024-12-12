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

class Test_hp_adview():
    logger = log_gen.loggen()   #logger initialisation
    burl = readconfig.get_url() #from the configuration file getting the base url
    def test_adview(self,setup):
        #try .... finally for handling the exceptions
        try:
            self.driver = setup
            self.logger.info('****Testcase7_arr_adview Started****')
            self.driver.get(self.burl)
            self.driver.maximize_window()
            time.sleep(30)
            self.hp = page_homepage(self.driver) #creating the object for page_homepage class
            self.hp.image_click()
            self.b1p = book1_imagepage(self.driver) #creating the object for book1_imagepage class
            self.b1p.arrival_addbasket()    #adding the book
            self.b1p.check_addmsg()         #check the message
            self.b1p.view_check()           #check the view
            assert True
        finally:
            self.driver.close()