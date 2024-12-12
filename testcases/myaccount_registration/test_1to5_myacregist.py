from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from utilities.customlogger import log_gen
from pageobjects.page_homepage import page_homepage
from pageobjects.account_login import acc_loginpage
from pageobjects.account_register import acc_registerpage
from utilities import XLUtility
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import time
from utilities import randomstring
from utilities.readproperties import readconfig
import logging
import os


class Test_Login_Ddt():     #class for data driven test
    baseURL = readconfig.get_url()
    path = os.path.abspath("C:\\Users\\usha5\\PycharmProjects\\PracticeProject2\\testdata\\homepage_logindata.xlsx")
    logger = log_gen.loggen()
    def test_login_ddt(self,setup):
        self.logger.info("**** Starting test_ 1 to 5 myaccount registration *******")
        self.rows=XLUtility.getRowCount(self.path,"Sheet2-Register")
        self.driver = setup     #chrome driver setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.debug('******Testing*****is*****going on******')

        self.hp = page_homepage(self.driver)  # HomePage Page Object Class
        #self.reg = page_acc_register(self.driver)  # LoginPage Page Object Class
        self.rp = acc_registerpage(self.driver)  # MyAccount Page Object class
        self.hp.myaccount_click()

        #accessing datas from the excel files
        for r in range(2,self.rows+1):
            print(self.rows)
            time.sleep(5)

            if r==2:
                email_name = randomstring.generate_random_string() + "@gmail.com"
                self.email=email_name
                #self.pword = XLUtility.readData(self.path, "Sheet2-Register", r, 1)
                self.pword = XLUtility.readData(self.path, "Sheet2-Register", r, 2)
                self.expr = XLUtility.readData(self.path, "Sheet2-Register", r, 3)
                time.sleep(2)
            else:
                self.email = XLUtility.readData(self.path, "Sheet2-Register", r, 1)
                self.pword = XLUtility.readData(self.path, "Sheet2-Register", r, 2)
                self.expr = XLUtility.readData(self.path, "Sheet2-Register", r, 3)

            if self.expr == "valid":
                self.rp.set_email_id(self.email)
                self.rp.set_password(self.pword)
                time.sleep(10)
                self.rp.register_click()
                logout_link = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.LINK_TEXT, "Logout"))
                    )
                logout_link.click()

            else:
                self.rp.email_pword_clear()
                self.rp.set_email_id(self.email)
                self.rp.set_password(self.pword)
                time.sleep(10)
                self.rp.register_click()
                time.sleep(10)
                self.driver.execute_script("window.scrollBy(0, 200);")  #for scrolling

        self.driver.close()
        assert True
