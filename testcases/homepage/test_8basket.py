from selenium import webdriver
from selenium.webdriver.common.by import By
from pageobjects.page_homepage import page_homepage
from pageobjects.book1_imagepage import book1_imagepage
from pageobjects.basket_page import basket_page
from pageobjects.account_registration import page_acc_register
import pytest
import time
import os
from utilities import randomstring
from utilities.readproperties import readconfig
from utilities.customlogger import log_gen

class Test_hp_basket():
    logger = log_gen.loggen() #logger initialisation
    burl = readconfig.get_url() #getting the base url from the configurations file
    def test_basket(self,setup):
        try:
            self.driver = setup
            #informations for the log file
            self.logger.info('****Testcase8_basket Started****')
            self.driver.get(self.burl)
            self.driver.maximize_window()
            time.sleep(30)
            self.hp = page_homepage(self.driver)    #object creation for the page_homepage class
            self.hp.image_click()
            self.b1p = book1_imagepage(self.driver) #object creation for the book1_imagepage class
            self.b1p.arrival_addbasket()            #adding the book
            self.b1p.check_addmsg()                 #checking the msg
            self.b1p.view_check()                   #check the view
            self.bsktp = basket_page(self.driver)   #object for the basket_page class
            self.bsktp.proceed_checkout()           #calling the method for proceed to checkout
            assert True

        finally:
            self.driver.close()



