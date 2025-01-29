from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class Addtocart():
    ADD_BUTTON = (By.CSS_SELECTOR, "#btn-add-to-basket")

class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_TOTAL = (By.CSS_SELECTOR, "basket_summary") #блок покупок
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner>p") #сообщение про пустоту

class RegistrationLocators():
    LOGIN = (By.ID, "id_registration-email")
    PASS1 = (By.ID, "id_registration-password1")
    PASS2 = (By.ID, "id_registration-password2")
    KNOPKA = (By.NAME, "registration_submit")
