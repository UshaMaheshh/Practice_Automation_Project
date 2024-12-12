import mysql.connector
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

class Test_hp_gatewaydb():
    logger = log_gen.loggen()   #for logging
    burl = readconfig.get_url() #for base url
    def test_gatewaydb(self,setup):
        try:    #for try....finally exception handling
            self.driver = setup #for chromedriver setup
            self.logger.info('****Testcase17_gateway_database Started****')
            self.driver.get(self.burl)
            self.driver.maximize_window()
            time.sleep(30)
            self.hp = page_homepage(self.driver) #object for page_hoepage class
            self.hp.image_click()
            self.b1p = book1_imagepage(self.driver)
            self.b1p.arrival_addbasket()
            self.b1p.check_addmsg()
            self.b1p.view_check()
            self.bsktp = basket_page(self.driver)   #object for basket_page class
            self.bsktp.subtotal_check()
            self.bsktp.proceed_checkout()
            ck_gt = check_gateway_page(self.driver) #object for check_gateway_page

            #creating connection for database

            connection = mysql.connector.connect(
                host='localhost',
                port='3306',
                user='root',
                password='root',
                database='contactdb'
            )

            # getting the contact details from contacts dtabase
            cursor = connection.cursor()
            query = "SELECT * FROM contacts WHERE country='india';"
            cursor.execute(query)

            self.columns = cursor.fetchone()
            #print(results[0])

            ck_gt.enter_firstname(self.columns[0])
            ck_gt.enter_lastname(self.columns[1])
            self.driver.execute_script("window.scrollBy(0, 100);")  #for scrolling
            ck_gt.enter_company(self.columns[2])
            ck_gt.enter_email(self.columns[3])
            ck_gt.enter_phoneno(self.columns[4])
            self.driver.execute_script("window.scrollBy(0, 250);")  #for scrolling
            ck_gt.enter_country(self.columns[5])
            ck_gt.enter_address1(self.columns[6])
            ck_gt.enter_address2(self.columns[7])
            self.driver.execute_script("window.scrollBy(0, 200);") #for scrolling
            ck_gt.enter_towncity(self.columns[8])
            ck_gt.enter_stcountry(self.columns[9])
            ck_gt.enter_postcode(self.columns[10])
            time.sleep(2)
            self.driver.execute_script("window.scrollBy(0, 800);")  #for scrolling
            ck_gt.payment_method()  #gateway payment method
            assert True

        finally:
            cursor.close()  #closing the database
            self.driver.close()



