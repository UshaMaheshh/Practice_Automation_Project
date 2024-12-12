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
    logger = log_gen.loggen()   # for logging
    pword=""
    def test_casecheck(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://practice.automationtesting.in/")
        self.driver.maximize_window()
        self.logger.info("********* starting test_myaccount Authentication ********")
        self.hp = page_homepage(self.driver)  # HomePage Page Object Class
        # self.reg = page_acc_register(self.driver)  # LoginPage Page Object Class
        self.lp = acc_loginpage(self.driver)  # MyAccount Page Object class
        self.hp.myaccount_click()
        self.uname="alexa@example.com"
        self.pword="pass$!exam"
        self.lp.set_username(self.uname)
        self.lp.set_password(self.pword)
        self.lp.login_click()
        print(self.pword)

        #explicit wait for "sign out"
        self.sign_out = WebDriverWait(self.driver,10).until(
                    EC.presence_of_element_located((By.LINK_TEXT, "Sign out"))
                    )
        self.sign_out.click()
        self.driver.back()      #go to the previous page
        if self.driver.find_element(By.XPATH,"//*[@id='customer_login']/div[1]/h2").text=="Login":
            print("It is Login Page, Back button doesnt sign in")
            assert True
        self.driver.close()
