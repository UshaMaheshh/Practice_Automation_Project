from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class book1_imagepage():

    desc_xpath="//*[@id='product-160']/div[3]/ul/li[1]/a"
    desc_text_xpath="//*[@id='tab-description']/h2"
    rev_xpath="//*[@id='product-160']/div[3]/ul/li[2]/a"
    rev_text_xpath="//*[@id='comments']/h2"
    arr_add_xpath="//*[@id='product-160']/div[2]/form/button"
    chk_addmsg_xpath="//*[@id='content']/div[1]"
    view_check_xpath="//*[@id='content']/div[1]/a"


    def __init__(self, driver):
        self.driver = driver

    def click_description(self):
        z = self.driver.find_element(By.XPATH, self.desc_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", z)
        self.driver.execute_script("arguments[0].click();", z)

    def check_description(self):
        e_description = "Product Description"
        d_text = self.driver.find_element(By.XPATH, self.desc_text_xpath).text
        if d_text == e_description:
            print("Description is Found")
        time.sleep(10)

    def click_reviews(self):
        x = self.driver.find_element(By.XPATH,self.rev_xpath)
        # Verify the 'Reviews' text
        self.driver.execute_script("arguments[0].click();", x)
        time.sleep(10)

    def check_reviews(self):
        expected_reviews = "Reviews"
        reviews_text = self.driver.find_element(By.XPATH,self.rev_text_xpath).text
        if reviews_text == expected_reviews:
            # print(reviews_text)
            print("Reviews are Found")

    def arrival_addbasket(self):
        add_to_basket_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,self.arr_add_xpath ))
        )
        add_to_basket_button.click()

    def check_addmsg(self):
        success_message_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,self.chk_addmsg_xpath))
        )

        # Extract the full text from the message element
        full_text = success_message_element.text
        # print(f"Full text from page: {full_text}")
        text2bextract = self.driver.find_element(By.XPATH, "//*[@id='content']/div[1]/a").text

        # The expected message typically follows "VIEW BASKET" and is on the next line
        start_marker = "“Selenium Ruby” has been added to your basket."
        rtext = full_text.replace(text2bextract, '').strip()
        # print(rtext)
        if rtext == start_marker:
            print(rtext)

    def view_check(self):
        view_basket_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.view_check_xpath))
        )
        view_basket_button.click()

        li_text = "Selenium Ruby"
        ltext = self.driver.find_element(By.LINK_TEXT, li_text).text
        if ltext == li_text:
            print("It is there")


