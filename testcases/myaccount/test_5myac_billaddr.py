from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from pageobjects.myaccount_page import myacc_page
from pageobjects.checkout_gatewaypage import check_gateway_page
from pageobjects.page_homepage import page_homepage
from pageobjects.account_registration import page_acc_register
from pageobjects.account_login import acc_loginpage
from utilities import XLUtility
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import time
from utilities import randomstring
from utilities.readproperties import readconfig
import logging
import os
from utilities.customlogger import log_gen

class Test_myacc_billadr():
    baseURL = readconfig.get_url()  #for getting baseurl
    logger = log_gen.loggen()       #for logging

    #pytest parametrization for username and password

    @pytest.mark.parametrize('uname,pword', [("birla@example.com","pass12$exam")])
    def test_billadr(self,setup,uname,pword):
        logging.info("**** Starting test_myaccount billing address *******")
        self.driver = setup #chromedriver setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = page_homepage(self.driver)  # HomePage Page Object Class
        #self.reg = page_acc_register(self.driver)  # LoginPage Page Object Class
        self.mc = myacc_page(self.driver)  # MyAccount Page Object class
        self.hp.myaccount_click()
        time.sleep(2)
        #self.driver.find_element(By.ID, "username").clear()
        self.driver.find_element(By.ID, "username").send_keys(uname)
        #self.lp.set_username(self.uname)
        time.sleep(2)
        #self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "password").send_keys(pword)
        #self.lp.set_password(self.pword)
        time.sleep(10)
        self.mc.login_click()
        locator=WebDriverWait(self.driver, 20).until(
                      EC.presence_of_element_located((By.LINK_TEXT, "Addresses"))
                        )
        locator.click()
        bill_edit=self.driver.find_element(By.XPATH,"//*[@id='page-36']/div/div[1]/div/div/div[1]/header/a")
        bill_edit.click()
        time.sleep(2)
        ck_gt = check_gateway_page(self.driver) #object creation for check_gateway_page
        ck_gt.enter_firstname("aaaa")
        ck_gt.enter_lastname("bbbb")
        self.driver.execute_script("window.scrollBy(0, 100);")  #for scrolling
        ck_gt.enter_company("cccc")
        #ck_gt.enter_email("gggg@gmail.com")
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
        #self.driver.execute_script("window.scrollBy(0, 800);") #for scrolling
        #ck_gt.payment_method() #calls method for payment method
        time.sleep(4)
        save_adr = self.driver.find_element(By.XPATH, "//input[@name='save_address']")
        save_adr.click()
        time.sleep(30)

        assert True
        self.driver.close()



