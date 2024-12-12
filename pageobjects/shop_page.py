from itertools import count

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class shoppage_elements():
    dropdown_xpath = "//select[@class='orderby']"
    def __init__(self, driver):
        self.driver = driver

    def product_android(self):
        self.driver.find_element(By.LINK_TEXT,"Android").click()
        print("Android")
        time.sleep(2)

    def product_html(self):
        self.driver.find_element(By.LINK_TEXT, "HTML").click()
        print("HTML")
        time.sleep(2)

    def product_javascript(self):
        self.driver.find_element(By.LINK_TEXT, "JavaScript").click()
        print("JavaScript")
        time.sleep(2)

    def product_selenium(self):
        self.driver.find_element(By.LINK_TEXT, "selenium").click()
        print("selenium")
        time.sleep(2)

    def dropdown_click(self):
        for i in range(1, 6):
            # WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//select[@class='orderby']")))

            # Scroll down to make the dropdown visible
            self.driver.execute_script("window.scroll(0,500)")

            # Retrieve all options in the dropdown initially
            dropdown = self.driver.find_element(By.XPATH, "//*[@id='content']/form/select")
            # Refresh the page
            self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", dropdown)

            dropdown.click()
            options = self.driver.find_elements(By.XPATH, "//select[@class='orderby']/option")
            print(options[i].text)
            # Wait for the dropdown to become visible again
            # WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "products")))
            time.sleep(20)  # Adjust based on your needs
            dropdown.send_keys(options[i].text + Keys.ENTER)
            time.sleep(5)
            # dropdown.clear()
            # driver.refresh()
            #self.driver.close()