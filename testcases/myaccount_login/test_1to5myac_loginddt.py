from platform import uname

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from pageobjects.page_homepage import page_homepage
from pageobjects.account_register import acc_registerpage
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

class Test_Login_Ddt():
    baseURL = readconfig.get_url()  #for getting url
    logger = log_gen.loggen()       #for logging
    path = os.path.abspath("C:\\Users\\usha5\\PycharmProjects\\PracticeProject2\\testdata\\homepage_logindata.xlsx")

    def test_login_ddt(self,setup):

        self.logger.info("**** Starting tes_myaccount loginddt *******")
        self.rows=XLUtility.getRowCount(self.path,"Sheet1-Login")
        self.driver = setup     #setting up the chromedriver
        self.driver.get(self.baseURL)
        self.driver.maximize_window()


        self.hp = page_homepage(self.driver)  # HomePage Page Object Class
            #self.reg = page_acc_register(self.driver)  # LoginPage Page Object Class
        self.lp = acc_loginpage(self.driver)  # MyAccount Page Object class
        self.hp.myaccount_click()

        #accessing datas from the excel file
        for r in range(2,self.rows+1):
            print(self.rows)
            time.sleep(5)
            #self.driver.refresh()
            self.uname=XLUtility.readData(self.path,"Sheet1-Login",r,1)
            self.pword = XLUtility.readData(self.path, "Sheet1-Login", r, 2)
            self.expr = XLUtility.readData(self.path, "Sheet1-Login", r, 3)
            print(self.uname ,  self.pword )
            time.sleep(2)
            self.lp.user_pword_clear()

            #checking from the excel file
            if self.expr == "valid":
                self.lp.set_username(self.uname)
                self.lp.set_password(self.pword)
                time.sleep(10)
                self.lp.login_click()

            #explicit wait for the linktext "logout"

                logout_link = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.LINK_TEXT, "Logout"))
                    )
                logout_link.click()

            else:
                self.lp.user_pword_clear()
                self.lp.set_username(self.uname)
                self.lp.set_password(self.pword)
                time.sleep(10)
                self.lp.login_click()
                time.sleep(10)
                self.driver.execute_script("window.scrollBy(0, 200);")  #for scrolling

        self.driver.close()
        assert True
