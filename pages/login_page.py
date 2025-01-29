from .base_page import BasePage
from .locators import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/" in self.url, "Login link is not correct"


    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = "Apriori11"

        email_input = self.browser.find_element(*RegistrationLocators.LOGIN)
        password_input = self.browser.find_element(*RegistrationLocators.PASS1)
        confirm_password_input = self.browser.find_element(*RegistrationLocators.PASS2)
        register_button = self.browser.find_element(*RegistrationLocators.KNOPKA)

        email_input.send_keys(email)
        password_input.send_keys(password)
        confirm_password_input.send_keys(password)
        register_button.click()


