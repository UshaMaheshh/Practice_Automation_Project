from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pageobjects.account_login import  acc_loginpage
from pageobjects.page_homepage import page_homepage
from utilities.customlogger import log_gen

class Test_pwordmask():
    logger = log_gen.loggen()   #for logging
    def test_pwordcheck(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://practice.automationtesting.in/")
        self.driver.maximize_window()
        self.logger.info("****** starting test_myaccount password mask ********")
        self.hp = page_homepage(self.driver)  # HomePage Page Object Class
        # self.reg = page_acc_register(self.driver)  # LoginPage Page Object Class
        self.lp = acc_loginpage(self.driver)  # MyAccount Page Object class
        self.hp.myaccount_click()
        self.password="abcd34ijkl"
        self.lp.set_password(self.password)

        #checking the password is masked
        password_field = self.driver.find_element(By.ID, "password")  # Change to your field's locator
        field_type = password_field.get_attribute('type')

        # If the type is 'password', it is masked
        if field_type == 'password':
            print("The password field is masked.")
            assert True         #test pass
            self.driver.close()
        else:
            print("The password field displays original text.")
            assert False        #test fail
            self.driver.close()