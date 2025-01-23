from .base_page import BasePage
from .locators import *
from .main_page import MainPage

class LoginPage(BasePage):
    def should_be_login_page(self,driver):
        self.driver = driver
        self.current_url = "http://selenium1py.pythonanywhere.com"
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.driver.current_url(MainPageLocators.LOGIN_LINK), "Login link is not correct"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
