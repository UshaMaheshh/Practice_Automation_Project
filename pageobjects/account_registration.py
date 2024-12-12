from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class page_acc_register():

    email_name = "email"
    password_name = "password"


    def __init__(self, driver):
        self.driver = driver


    def set_email_name(self, ename):
        self.driver.find_element(By.NAME,self.email_name).clear()
        self.driver.find_element(By.NAME,self.email_name).send_keys(ename)

    def set_password_name(self, pword):
        self.driver.find_element(By.NAME,self.password_name).clear()
        self.driver.find_element(By.NAME,self.password_name).send_keys(pword)



