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
    burl = readconfig.get_url()     #for getting the base url
    logger = log_gen.loggen()       #for logging
    def test_homepage(self,setup):
        try:
            self.driver = setup     #chrome driver setup
            self.logger.info('****Testing Started shop add,view through link*****')
            self.driver.get(self.burl)
            self.driver.maximize_window()
            time.sleep(30)
            self.hp = page_homepage(self.driver)    #object for page_homepage
            self.hp.image_click()
            self.b1p = book1_imagepage(self.driver) #object for book1_imagepage
            self.b1p.arrival_addbasket()
            self.b1p.check_addmsg()
            self.b1p.view_check()
            self.driver.find_element(By.XPATH,"//img[@class='attachment-shop_thumbnail size-shop_thumbnail wp-post-image']").click()
            if self.driver.find_element(By.XPATH,"//h1[@class='product_title entry-title']"):
                print("Not proceed to checkout page!, It is Product Description Page")
                #saving the screenshot file
                self.driver.save_screenshot(os.path.abspath("C:\\Users\\usha5\\PycharmProjects\\PracticeProject2\\screenshots\\testshop_view_link.png"))
            time.sleep(20)

        finally:
            self.driver.close()



