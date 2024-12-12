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


class Test_Login_Dboard():
    uname=""
    pword=""
    baseURL = readconfig.get_url()  #for getting the base url
    logger = log_gen.loggen()       #for logging

    #pytest parametrization for name, password

    @pytest.mark.parametrize('uname,pword', [("birla@example.com","pass12$exam")])
    def test_login_dboard(self,setup,uname,pword):
        self.logger.info("**** Starting test_Myaccount_Dashboard *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = page_homepage(self.driver)  # HomePage Page Object Class
        self.mc = myacc_page(self.driver)  # MyAccount Page Object class
        self.hp.myaccount_click()
        time.sleep(2)
        self.driver.find_element(By.ID, "username").send_keys(uname)
        time.sleep(2)
        #self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "password").send_keys(pword)
        time.sleep(10)
        self.mc.login_click()

        #explicit wait for accessing the linktext "dashboard"
        locator=WebDriverWait(self.driver, 30).until(
                      EC.presence_of_element_located((By.LINK_TEXT, "Dashboard"))
                        )
        if locator.text=="Dashboard":
            print("It is Myaccount - Dashboard page")
            assert True
        self.driver.close()
        time.sleep(2)
