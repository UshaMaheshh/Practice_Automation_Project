from faulthandler import is_enabled

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from pageobjects.myaccount_page import myacc_page
from pageobjects.page_homepage import page_homepage
from pageobjects.account_registration import page_acc_register
from pageobjects.account_login import acc_loginpage
from pageobjects.checkout_gatewaypage import check_gateway_page
from utilities import XLUtility
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import time
from utilities import randomstring
from utilities.readproperties import readconfig
from utilities.customlogger import log_gen
import os


class Test_myacc_adetails():
    baseURL = readconfig.get_url()  #for getting base url
    logger = log_gen.loggen()       #for logging

    #pytest parametrization for username, password

    @pytest.mark.parametrize('uname,pword', [("birla@example.com","pass12$exam")])
    def test_adetails(self,setup,uname,pword):
        self.logger.info("**** Starting test_myaccount Account details *******")
        try:        #try.....finally exception handling
            self.driver = setup
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
            locator=WebDriverWait(self.driver, 30).until(
                          EC.presence_of_element_located((By.LINK_TEXT, "Account Details"))
                            )
            if locator.text=="Account Details":
                print("It is Myaccount - Account Details page")
            edit_xpath = "//a[contains(text(),'edit your')]"
            self.driver.find_element(By.XPATH,edit_xpath).click()
            time.sleep(20)
            #np = input("Please enter your password: ")
            #time.sleep(30)

            self.driver.find_element(By.ID, "account_first_name").send_keys("aaaa")
            self.driver.find_element(By.ID, "account_last_name").send_keys("bbbb")
            self.driver.execute_script("window.scrollBy(0, 300);")
            self.driver.find_element(By.CSS_SELECTOR,"input#password_current").send_keys(pword)
            x="passexam"
            y="pass12$exam"
            self.driver.find_element(By.ID,"password_1").send_keys(x)
            time.sleep(20)

            #changing the password

            if (self.driver.find_element(By.XPATH, "//div[text()='Weak - Please enter a stronger password.']")):
                self.driver.find_element(By.ID, "password_1").clear()
                self.driver.find_element(By.ID, "password_1").send_keys(y)
                time.sleep(10)
                x = y
            self.driver.find_element(By.ID, "password_2").send_keys(x)
            time.sleep(10)
            #print(x)
            #self.driver.execute_script("window.scrollBy(0, 100);")
            self.driver.find_element(By.XPATH,"//input[@name='save_account_details']").click()
            time.sleep(10)

            #checking that account details are  changed successfully
            if (self.driver.find_element(By.XPATH,"//*[@id='page-36']/div/div[1]/div[1]")):
                print("Account Details are changed Successfully")
        finally:
            time.sleep(4)
            self.driver.close()

