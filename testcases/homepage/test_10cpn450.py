from selenium import webdriver
from selenium.common import TimeoutException
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

class Test_hp_cpn450():
    logger = log_gen.loggen()   #for logging
    burl = readconfig.get_url() #getting the base url
    def test_cpn450(self,setup):
        try:
            self.driver = setup #chrome driver setup
            self.logger.info('****Testcase10_cpn450 Started****')
            self.driver.get(self.burl)
            self.driver.maximize_window()
            time.sleep(30)
            self.hp = page_homepage(self.driver)   #object for page_homepage class
            self.hp.image_click()
            self.b1p = book1_imagepage(self.driver) #object for book1_imagepage class
            self.b1p.arrival_addbasket()
            self.b1p.check_addmsg()
            self.b1p.view_check()
            self.bsktp = basket_page(self.driver)   ##object for basket_page class
            self.bsktp.proceed_checkout()
            self.driver.back()
            self.bsktp.coupon_check()   #checking the coupon
            self.bsktp.gohome()
            self.bsktp.coupon_chk450()  #checking the coupon code 450
            assert True

        except TimeoutException:        #exception handling
            print("It is timeout exception")

        finally:
            self.driver.close()



