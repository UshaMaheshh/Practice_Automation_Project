from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from pageobjects.myaccount_page import myacc_page
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
from utilities.customlogger import log_gen
import os


class Test_myacc_orders():
    baseURL = readconfig.get_url()  #for getting base url
    logger = log_gen.loggen()       #for logging

    #pytest parametrization for username and password

    @pytest.mark.parametrize('uname,pword', [("birla@example.com","pass12$exam")])
    def test_orders(self,setup,uname,pword):
        self.logger.info("**** Starting test_myaccount orders *******")
        self.driver = setup     #chromedriver setup
        self.driver.get(self.baseURL)   #for getting the base url
        self.driver.maximize_window()

        self.hp = page_homepage(self.driver)  # HomePage Page Object Class
        #self.reg = page_acc_register(self.driver)  # LoginPage Page Object Class
        self.mc = myacc_page(self.driver)  # MyAccount Page Object class
        self.hp.myaccount_click()
        time.sleep(2)
        #self.driver.find_element(By.ID, "username").clear
        self.driver.find_element(By.ID, "username").send_keys(uname)
        #self.lp.set_username(self.uname)
        time.sleep(2)
        #self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "password").send_keys(pword)
        #self.lp.set_password(self.pword)
        time.sleep(10)
        self.mc.login_click()

        #explicit wait for linktext "orders"

        locator=WebDriverWait(self.driver, 30).until(
                      EC.presence_of_element_located((By.LINK_TEXT, "Orders"))
                        )
        if locator.text=="Orders":
            print("It is Myaccount - Orders page")
            assert True
        self.driver.close()
        time.sleep(2)
