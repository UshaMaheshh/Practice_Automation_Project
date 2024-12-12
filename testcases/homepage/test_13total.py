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

class Test_hp_total():
    logger = log_gen.loggen()   #for logging
    burl = readconfig.get_url() #for baseurl
    def test_total(self,setup):
        try:    #try....finally for exception handling
            self.driver = setup #chrome driver setup
            self.logger.info('****Testcase13_total Started****')
            self.driver.get(self.burl)
            self.driver.maximize_window()
            time.sleep(30)
            self.hp = page_homepage(self.driver)    #object for page_page
            self.hp.image_click()
            self.b1p = book1_imagepage(self.driver) #object for book1_imagepage class
            self.b1p.arrival_addbasket()
            self.b1p.check_addmsg()
            self.b1p.view_check()
            self.bsktp = basket_page(self.driver)   #object for basket_page class
            self.bsktp.proceed_checkout()
            self.bsktp.total_price()    #calls the method for totalprice
           # print("Total Price =", float(x))
            assert True

        finally:
            self.driver.close()



