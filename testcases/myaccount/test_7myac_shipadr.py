from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys
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

class Test_myacc_shipadr():
    baseURL = readconfig.get_url()  #for getting the base url
    logger = log_gen.loggen()       #for logging
    @pytest.mark.parametrize('uname,pword', [("birla@example.com","pass12$exam")])
    def test_shipadr(self,setup,uname,pword):
        self.logger.info("**** Starting test_shipping address *******")
        self.driver = setup     #chromedriver setup
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

        #explicit wait for linktext"addresses"

        locator=WebDriverWait(self.driver, 10).until(
                      EC.presence_of_element_located((By.LINK_TEXT, "Addresses"))
                        )
        locator.click()
        bill_edit=self.driver.find_element(By.XPATH,"//*[@id='page-36']/div/div[1]/div/div/div[2]/header/a")
        bill_edit.click()
        time.sleep(2)
        #ck_gt = check_gateway_page(self.driver)
        self.driver.find_element(By.ID,"shipping_first_name").send_keys("aaaa")
        self.driver.find_element(By.ID,"shipping_last_name").send_keys("bbbb")

        #ck_gt.enter_firstname("aaaa")
        #ck_gt.enter_lastname("bbbb")
        self.driver.execute_script("window.scrollBy(0, 100);")  #for scrolling
        self.driver.find_element(By.ID, "shipping_company").send_keys("cccc")
        #self.driver.find_element(By.ID, "").send_keys("gggg@gmail.com")
        #self.driver.find_element(By.ID, "").send_keys("111111")

        #ck_gt.enter_company("cccc")
        #ck_gt.enter_email("gggg@gmail.com")
        #ck_gt.enter_phoneno("111111")
        self.driver.execute_script("window.scrollBy(0, 250);")  #for scrolling
        self.driver.find_element(By.XPATH, "//*[@id='select2-chosen-1']").click()
        self.driver.find_element(By.XPATH, "//*[@id='s2id_autogen1_search']").send_keys("Australia" + Keys.ENTER)

        #self.driver.find_element(By.XPATH, "//*[@id='s2id_autogen1_search']").send_keys("India"+Keys.ENTER)
        self.driver.find_element(By.ID, "shipping_address_1").send_keys("dddd")
        self.driver.find_element(By.ID, "shipping_address_2").send_keys("eeee")

        #ck_gt.enter_country()
        #ck_gt.enter_address1("dddd")
        #ck_gt.enter_address2("eeee")
        self.driver.execute_script("window.scrollBy(0, 200);") #for scrolling

        self.driver.find_element(By.ID, "shipping_city").send_keys("ggggg")
        self.driver.find_element(By.XPATH,"//*[@id='s2id_shipping_state']/a/span[2]/b").click()
        self.driver.find_element(By.XPATH, "//input[@id='s2id_autogen2_search']").send_keys("Queensland" + Keys.ENTER)

        #self.driver.find_element(By.ID, "s2id_autogen2_search").send_keys("Tamil Nadu"+Keys.ENTER)
        self.driver.find_element(By.ID, "shipping_postcode").send_keys("222222")

        #ck_gt.enter_towncity("ggggg")
        #ck_gt.enter_stcountry()
        #ck_gt.enter_postcode("222222")
        time.sleep(2)
        #self.driver.execute_script("window.scrollBy(0, 800);") #for scrolling
        #ck_gt.payment_method()
        time.sleep(4)
        save_adr = self.driver.find_element(By.XPATH, "//input[@name='save_address']")
        save_adr.click()
        time.sleep(10)

        assert True
        self.driver.close()



