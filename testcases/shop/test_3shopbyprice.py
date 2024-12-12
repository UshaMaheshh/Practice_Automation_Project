from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobjects.page_homepage import page_homepage
import pytest
import time
from utilities.readproperties import readconfig
from utilities.customlogger import log_gen



class TestHomepage:
    logger = log_gen.loggen()   #for logging
    burl = readconfig.get_url() #for getting the base url

    def test_homepage(self, setup):
        self.driver = setup     #for chromedriver setup
        self.logger.info('****Testcase shop_by_price Started****')

        # Open the URL and maximize the window
        self.driver.get(self.burl)
        self.driver.maximize_window()

        # Wait for the page to load
        time.sleep(5)

        # Click on the Shop Menu
        self.hp = page_homepage(self.driver)
        self.hp.shop_click()

        # Wait for the shop page to load
        time.sleep(5)

        # Refresh the page if necessary
        #self.driver.refresh()

        # Wait for the slider handles to be visible
        min_slider_handle = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(@class, 'ui-slider-handle ui-corner-all ui-state-default')][1]"))
        )
        max_slider_handle = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(@class, 'ui-slider-handle ui-corner-all ui-state-default')][2]"))
        )

        action = ActionChains(self.driver)

        # Move the minimum price slider (set as needed, e.g., to 150)
        action.click_and_hold(min_slider_handle).move_by_offset(0, 0).release().perform()  # Adjust offset as needed
        time.sleep(1)  # Wait for the slider to update

        # Move the maximum price slider to 400
        # You'll need to calculate the offset based on the slider's design
        # For example, if the total width of the slider is 500 pixels and 400 is the target:
        max_offset = -28 # Adjust this offset based on the actual UI behavior
        action.click_and_hold(max_slider_handle).move_by_offset(max_offset, 0).release().perform()
        time.sleep(1)  # Wait for the slider to update

        # Print the current maximum price after moving the slider
        max_price_display = self.driver.find_element(By.XPATH,
                                                     "//span[contains(@class, 'to')]")  # Update to correct XPath for displayed max price
        print("Max price set to:", max_price_display.text)

        # Optionally click the filter button
        filter_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Filter')]")
        filter_button.click()

        time.sleep(30)
        self.driver.close()

