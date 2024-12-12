from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pageobjects.account_login import  acc_loginpage
from pageobjects.page_homepage import page_homepage
from utilities.customlogger import log_gen

class Test_case_check():
    logger = log_gen.loggen()   #for logging
    def test_casecheck(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://practice.automationtesting.in/")
        self.driver.maximize_window()
        self.logger.info("******** starting test_myaccount case sensitivity check*******")
        self.hp = page_homepage(self.driver)  # HomePage Page Object Class
        # self.reg = page_acc_register(self.driver)  # LoginPage Page Object Class
        self.lp = acc_loginpage(self.driver)  # MyAccount Page Object class
        self.hp.myaccount_click()
        self.uname="ALICE@EXAMPLE.COM"
        self.pword="PASS$!EXAM"
        self.lp.set_username(self.uname)
        self.lp.set_password(self.pword)
        self.lp.login_click()
        self.error_xpath = self.driver.find_element(By.XPATH,"//*[@id='page-36']/div/div[1]/ul/li")
        self.error_msg="A user could not be found with this"

        #checks the case sensitivity of the message
        if self.error_msg in self.error_xpath.text:
            print("Case sensitivity is not Working")
            assert False
            #self.driver.close()
        else:
            print("Case sensitivity is Working")
            assert True
            #self.driver.close()
