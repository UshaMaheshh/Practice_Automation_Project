from selenium import webdriver
from selenium.webdriver.common.by import By
from pageobjects.page_homepage import page_homepage
from pageobjects.book1_imagepage import book1_imagepage
from pageobjects.basket_page import basket_page
from pageobjects.checkout_gatewaypage import check_gateway_page
from pageobjects.account_registration import page_acc_register
import pytest
import time
import os
from utilities import randomstring
from utilities.readproperties import readconfig
from utilities.customlogger import log_gen


class Test_homepage():
    burl = readconfig.get_url() #for getting the base url
    logger = log_gen.loggen()   #for logging
    def test_homepage(self,setup):
        try:                    #try....finally block for exception handling
            self.driver = setup #chrome driver setup
            self.logger.info('******* Testing Started add & view basket ********')
            self.driver.get(self.burl)
            self.driver.maximize_window()
            time.sleep(30)
            self.hp = page_homepage(self.driver)    #object for page_homepage class
            self.hp.image_click()
            self.b1p = book1_imagepage(self.driver) #object for book1_imagepage class
            self.b1p.arrival_addbasket()
            self.b1p.check_addmsg()
            self.b1p.view_check()
            self.bsktp = basket_page(self.driver)   #object for basket_page
            self.bsktp.subtotal_check()
            self.bsktp.proceed_checkout()
            ck_gt = check_gateway_page(self.driver) #object for check_gateway_page
            ck_gt.enter_firstname("aaaa")
            ck_gt.enter_lastname("bbbb")
            self.driver.execute_script("window.scrollBy(0, 100);")  #for scrolling
            ck_gt.enter_company("cccc")
            ck_gt.enter_email("gggg@gmail.com")
            ck_gt.enter_phoneno("111111")
            self.driver.execute_script("window.scrollBy(0, 250);")  #for scrolling
            ck_gt.enter_country("India")
            ck_gt.enter_address1("dddd")
            ck_gt.enter_address2("eeee")
            self.driver.execute_script("window.scrollBy(0, 200);")  #for scrolling
            ck_gt.enter_towncity("ggggg")
            ck_gt.enter_stcountry("Sikkim")
            ck_gt.enter_postcode("222222")
            time.sleep(2)
            self.driver.execute_script("window.scrollBy(0, 800);")  #for scrolling
            ck_gt.payment_method()
            ck_gt.place_order()     #calls method for placing order
            time.sleep(20)
            assert True

        finally:
            self.driver.close()



