from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class basket_page():
    pro_chkout_xpath = "//*[@id='page-34']/div/div[1]/div/div/div/a"
    chk_msg_xpath = "//*[@id='customer_details']/div[1]/div/h3"
    price_xpath="//*[@id='page-34']/div/div[1]/div[2]/div/table/tbody/tr[1]/td/span"
    tax_xpath="//*[@id='page-34']/div/div[1]/div[2]/div/table/tbody/tr[3]/td/span"
    total_xpath="//*[@id='page-34']/div/div[1]/div[2]/div/table/tbody/tr[4]/td/strong/span"
    discount_xpath ="// *[ @ id = 'page-34'] / div / div[1] / div / div / table / tbody / tr[2] / td"
    coupon_xpath = "//*[@id='page-34']/div/div[1]/div[1]"
    add_coupon_xpath = "//*[@id='page-34']/div/div[1]/form/table/tbody/tr[2]/td/div/input[2]"
    apply_coupon_xpath="// *[ @ id = 'page-34'] / div / div[1] / form / table / tbody / tr[3] / td / div / input[2]"
    coupon_code_xpath = "//*[@id='coupon_code']"
    add_element_xpath="//*[@id='text-22-sub_row_1-0-2-1-0']/div/ul/li/a[2]"
    view_element_xpath="//*[@id='text-22-sub_row_1-0-2-1-0']/div/ul/li/a[3]"
    coupon_msg_xpath= "//*[@id='page-34']/div/div[1]/ul/li"
    remove_xpath="//*[@id='page-34']/div/div[1]/form/table/tbody/tr[1]/td[1]/a"
    remove_msg_xpath="//*[@id='page-34']/div/div[1]"
    inputbox_xpath="//*[@id='page-34']/div/div[1]/form/table/tbody/tr[1]/td[5]/div/input"
    table_xpath="//*[@id='page-34']/div/div[1]/form/table"
    update_xpath="//*[@id='page-34']/div/div[1]/form/table/tbody/tr[2]/td/input[1]"
    total_price_xpath="// *[ @ id = 'order_review'] / table / tfoot / tr[3] / td / strong / span"
    subtotal_xpath="//*[@id='page-34']/div/div[1]/div/div/table/tbody/tr[1]/td/span"
    tprice=0.0
    subprice=0.0


    def __init__(self, driver):
        self.driver = driver

    def proceed_checkout(self):
        proceed_chkout = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,self.pro_chkout_xpath))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", proceed_chkout)
        self.driver.execute_script("arguments[0].click();", proceed_chkout)
        time.sleep(3)
        if self.driver.find_element(By.XPATH,self.chk_msg_xpath).text == "Billing Details":
            print("It is Payment Gateway Checkout Page")

    def coupon_check(self):
        self.driver.find_element(By.XPATH,self.coupon_code_xpath).send_keys("krishnasakinala")
        add_coupon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH,self.add_coupon_xpath))
        )
        self.driver.execute_script("arguments[0].click();", add_coupon)

        time.sleep(30)
        coupon_msg = self.driver.find_element(By.XPATH,self.coupon_xpath).text
        print(coupon_msg)
        if "Coupon code applied successfully." == coupon_msg:
            print("Successfully Coupon Added")
        discount = self.driver.find_element(By.XPATH,self.discount_xpath).text
        if "50.00" in discount:
            print("Discount price is 50.00")
        price_text = self.driver.find_element(By.XPATH,self.price_xpath).text
        tax_text = self.driver.find_element(By.XPATH,self.tax_xpath).text
        total_text = self.driver.find_element(By.XPATH,self.total_xpath).text
        price = price_text.replace('₹', '')
        tax = tax_text.replace('₹', '')
        final_total = float(price) + float(tax) - float(50.00)
        total = total_text.replace('₹', '')
        if final_total == float(total):
            print("Coupon price subtracted")
            print("Final total price is :  ₹", float(total))
            #tprice=float(total)
    def gohome(self):
        shopvar=WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, "Shop"))
        )
        shopvar.click()
        self.driver.refresh()
        homevar= WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, "Home"))
        )
        homevar.click()
        time.sleep(2)

    def coupon_chk450(self):
        add_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,self.add_element_xpath))
        )
        # driver.execute_script("arguments[0].scrollIntoView();", add_element)
        self.driver.execute_script("arguments[0].click();", add_element)
        time.sleep(60)
        # Click on 'View Cart' using WebDriverWait
        view_element = self.driver.find_element(By.XPATH,self.view_element_xpath)
        self.driver.execute_script("arguments[0].click();", view_element)

        # Check if the item is successfully added
        if WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Thinking in HTML"))):
            print("Successfully Added to Basket")
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.coupon_code_xpath).send_keys("krishnasakinala")
        apply_coupon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH,self.apply_coupon_xpath))
        )
        self.driver.execute_script("arguments[0].click();", apply_coupon)
        time.sleep(30)
        coupon_msg=WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, self.coupon_msg_xpath))
        )
        print(coupon_msg.text)
        #if "Sorry, this coupon is not valid for sale items." == coupon_msg:
        #    print("Sorry, this coupon is not valid for sale items.")

    def remove_book(self):
        remove_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.LINK_TEXT,"×"))
        )
        remove_button.click()
        time.sleep(30)
        #self.driver.refresh()
        # Wait for the removal confirmation
        disp_text = "Selenium Ruby removed."
        ori_text_element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH,self.remove_msg_xpath))
        )

        # Check if the partial text is in the element's text
        if disp_text in ori_text_element.text:
            print("Removed!")

    def basket_update(self):
        table = WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located((By.XPATH,self.table_xpath)))

        quantity_cell = table.find_element(By.CSS_SELECTOR, ".product-quantity")

        # Locate the input box within the quantity cell
        input_box = quantity_cell.find_element(By.XPATH,self.inputbox_xpath)
        input_box.clear()
        input_box.send_keys("10")
        print("working")
        input_box.send_keys(Keys.UP)
        time.sleep(20)
        input_box.send_keys(Keys.DOWN)
        time.sleep(20)
        self.driver.find_element(By.XPATH, self.update_xpath).click()
        print("Updated")

    def total_price(self):
        total_price = WebDriverWait(self.driver,60).until(
            EC.presence_of_element_located((By.XPATH, self.total_price_xpath)) )
        self.driver.execute_script("arguments[0].scrollIntoView();", total_price)
        print("Total Price =", total_price.text)
        #tprice = float(total_price.text)
        #return(t_price.text)

    def subtotal_check(self):
        Total_price = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[@id='page-34']/div/div[1]/div/div/table/tbody/tr[3]/td/strong/span"))
        )
        print("Total Price =", Total_price.text)

        sub_total = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[@id='page-34']/div/div[1]/div/div/table/tbody/tr[1]/td/span"))
        )
        print("SubTotal Price =", sub_total.text)

        sub_total = sub_total.text.replace('₹', '')
        total = Total_price.text.replace('₹', '')
        if float(sub_total) < float(total):
            print("Subtotal is less than Total")
        self.subprice = float(sub_total)

    def tax_calculation(self,country):
        t_text=self.driver.find_element(By.XPATH,"//*[@id='order_review']/table/tfoot/tr[3]/td/strong/span").text
        t = float(t_text.replace('₹', '').strip())  # Convert to float after cleaning
        #print(t)
        ta_text = self.driver.find_element(By.XPATH, "//*[@id='order_review']/table/tfoot/tr[2]/td/span").text
        ta = float(t_text.replace('₹', '').strip())  # Convert to float after cleaning
        #print(ta)

        #selected_country = self.driver.find_element(By.ID, "select2-chosen-1").text
        selected_country = country
        #print(selected_country)
        #print(self.subprice)
        india_tax= t -((2 / 100) * self.subprice)
        foreign_tax = t -((5 / 100) * self.subprice)
        #print(india_tax)
        #print(foreign_tax)
        if selected_country == "India":
            if india_tax == self.subprice:
                print("Correct 2% tax for India")
        elif (selected_country != "India") and foreign_tax == self.subprice:
            print("Correct 5% tax for Foreign country")

    #     tax = self.subprice * (5/100)
        #self.driver.execute_script("windows.scrollBy(0,300);")

        #if (self.driver.find_element(By.XPATH,"//*[@id='order_review']/table/tfoot/tr[2]/td/span/text()").text)=="'₹"+"self.tax":
         #   print("Correct Tax")

        #self.tprice = self.subprice+tax
        #self.driver.find_element(By.XPATH,"//*[@id='order_review']/table/tfoot/tr[3]/td/strong/span").text=="₹"+"self.tprice"



