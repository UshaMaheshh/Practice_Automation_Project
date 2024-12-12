from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


class acc_registerpage():
    register_xpath = "//*[@id='customer_login']/div[2]/form/p[3]/input[3]"
    email_id = "reg_email"
    password_id = "reg_password"
    pword_msg_xpath="// *[ @ id = 'customer_login'] / div[2] / form / p[2] / div"

    def __init__(self, driver):
        self.driver = driver

    def set_email_id(self,eid):
        if eid == "None":
            self.driver.find_element(By.ID,self.email_id).send_keys('')
        else:
            self.driver.find_element(By.ID, self.email_id).clear()
            self.driver.find_element(By.ID,self.email_id).send_keys(eid)
            print(eid)

    def set_password(self,pid):
        if pid == "None":
            self.driver.find_element(By.ID,self.password_id).send_keys('')
        else:
            self.driver.find_element(By.ID, self.password_id).clear()
            self.driver.find_element(By.ID,self.password_id).send_keys(pid)
            print(pid,"\n")

    def register_click(self):
           #if WebDriverWait(self.driver,5).until(presence_of_element_located(By.XPATH,self.pword_msg_xpath)):
            #    if "Weak" not in self.pword_msg_xpath.text:
                #    print("Weak password,try another")
                #    time.sleep(20)
                #else:
                    self.driver.find_element(By.XPATH,self.register_xpath).click()
                    time.sleep(2)

    def email_pword_clear(self):
        self.driver.find_element(By.ID, self.email_id).clear()
        self.driver.find_element(By.ID, self.password_id).clear()









