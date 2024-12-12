from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class myacc_page():
    login_xpath = "//*[@id='customer_login']/div[1]/form/p[3]/input[3]"
   # logout_xpath = "//*[@id='top']/div/div[2]/ul/li[2]/div/ul/li[5]/a"
    username_id = "username"
    password_id = "password"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self,uid):
            self.driver.find_element(By.ID,self.username_id).send_keys(uid)
            #print(uid)

    def set_password(self,pid):
            self.driver.find_element(By.XPATH,"// input[ @ id = 'password']").send_keys(pid)
            #print(pid,"\n")

    def login_click(self):
           self.driver.find_element(By.XPATH,self.login_xpath).click()

    def user_pword_clear(self):
        self.driver.find_element(By.ID, self.username_id).clear()
        self.driver.find_element(By.ID, self.password_id).clear()

