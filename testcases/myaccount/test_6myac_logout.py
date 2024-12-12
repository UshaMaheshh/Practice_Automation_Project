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
import logging
import os
from utilities.customlogger import log_gen

class Test_myacc_logout():
    baseURL = readconfig.get_url()  #for getting base url
    logger = log_gen.loggen()       #for logging

    #pytest parametrization for username, password

    @pytest.mark.parametrize('uname,pword', [("birla@example.com","pass12$exam")])
    def test_logout(self,setup,uname,pword):
        self.logger.info("**** Starting test_myaccount logout *******")
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
        time.sleep(30)

        #explicit wait for linktext "dashboard"

        locator=WebDriverWait(self.driver, 40).until(
                      EC.presence_of_element_located((By.LINK_TEXT, "Dashboard"))
                        )
        if locator.text=="Dashboard":
            print("It is Myaccount - Dashboard page")
        self.driver.find_element(By.LINK_TEXT,"Logout").click()

        #checking logged out successfully

        if self.driver.find_element(By.XPATH,"//h2[text()='Login']")=="Login":
            print("Successfully Logged out")
            assert True
        self.driver.close()



