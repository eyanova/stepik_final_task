from .base_page import BasePage
from .locators import *
from selenium.common.exceptions import NoAlertPresentException
import math
import time


class CartPage(BasePage):
    def go_to_cart(self):
        cart_link = self.browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
        cart_link.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
            time.sleep(1)
        except NoAlertPresentException:
            print("No second alert presented")

    def test2(self):
        # названия книг совпадают
        booknamecart = self.browser.find_element(By.CSS_SELECTOR,"div.alert.alert-safe.alert-noicon.alert-success.fade.in div.alertinner strong")
        booknamebook = self.browser.find_element(By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
        booknamecart_text = booknamecart.text
        booknamebook_text = booknamebook.text
        assert booknamecart_text == booknamebook_text


    def test3(self):
        # цена совпадает
        sumbook = self.browser.find_element(By.CSS_SELECTOR, "p.price_color")
        sumcart = self.browser.find_element(By.CSS_SELECTOR,"div.alert-info p strong")
        sumbook_text=sumbook.text
        sumcart_text=sumcart.text
        assert sumbook_text == sumcart_text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappear, but should be"







