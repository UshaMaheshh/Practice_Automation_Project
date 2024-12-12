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

class Test_hp_coupon():
    logger = log_gen.loggen()   #for logging
    burl = readconfig.get_url() #for base-url
    def test_coupon(self,setup):
        try:
            self.driver = setup
            self.logger.info('****Testcase9 coupon Started****')
            self.driver.get(self.burl)
            self.driver.maximize_window()
            time.sleep(30)
            self.hp = page_homepage(self.driver) #creating object for page_homepage class
            self.hp.image_click()
            self.b1p = book1_imagepage(self.driver) #object for book1_imagepage class
            self.b1p.arrival_addbasket()
            self.b1p.check_addmsg()
            self.b1p.view_check()
            self.bsktp = basket_page(self.driver)
            self.bsktp.proceed_checkout()
            self.driver.back()  #go to the previous page
            self.bsktp.coupon_check()   #method for checking the coupon
            assert True

        finally:
            self.driver.close()



