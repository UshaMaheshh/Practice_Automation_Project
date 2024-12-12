from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class page_homepage():

    sliders_xpath="//*[contains(@class, 'slider-')]"
    arrival_xpath="//img[@class='attachment-shop_catalog size-shop_catalog wp-post-image']"
    book1_xpath="//*[@id='text-22-sub_row_1-0-2-0-0']/div/ul/li/a[1]/img"
    book1_title_xpath="//h1[@class='product_title entry-title']"
    book1_image_xpath="//*[@id='text-22-sub_row_1-0-2-0-0']/div/ul/li/a[1]/img"
    desc_xpath="//*[@id='product-160']/div[3]/ul/li[1]/a"
    desc_text_xpath="//*[@id='tab-description']/h2"
    rev_xpath="//*[@id='product-160']/div[3]/ul/li[2]/a"
    rev_text_xpath="//*[@id='comments']/h2"
    add_book_xpath = "//*[@id='text-22-sub_row_1-0-2-0-0']/div/ul/li/a[2]"
    view_book_xpath ="//*[@id='text-22-sub_row_1-0-2-0-0']/div/ul/li/a[3]"

    def __init__(self, driver):
        self.driver = driver

    def count_of_sliders(self):
        sliders = self.driver.find_elements(By.XPATH, self.sliders_xpath)
        time.sleep(30)
        num_sliders = len(sliders)
        print(f'Number of sliders found: {num_sliders}')

    def count_of_arrivals(self):
        arrivals = self.driver.find_elements(By.XPATH,self.arrival_xpath)

        for book in arrivals:
            book.find_element(By.XPATH,self.arrival_xpath)
            print("BookName =", book.get_attribute("title"))
        time.sleep(10)
        print("No. of book arrivals:  ", len(arrivals))

    def image_navigate(self):
        book1 = self.driver.find_element(By.XPATH,self.book1_xpath)
        book1.click()
        btitle = self.driver.find_element(By.XPATH,self.book1_title_xpath).text
        return btitle

    def image_click(self):
        book1 = self.driver.find_element(By.XPATH,self.book1_image_xpath)
        book1.click()
        time.sleep(10)

    def add_basket(self):
            add_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='text-22-sub_row_1-0-2-0-0']/div/ul/li/a[2]"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", add_element)
            self.driver.execute_script("arguments[0].click();", add_element)

    def view_basket(self):
            view_element = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='text-22-sub_row_1-0-2-0-0']/div/ul/li/a[3]"))
            )
            self.driver.execute_script("arguments[0].click();", view_element)

    def myaccount_click(self):
            self.driver.find_element(By.LINK_TEXT,"My Account").click()

    def shop_click(self):
        self.driver.find_element(By.LINK_TEXT,"Shop").click()