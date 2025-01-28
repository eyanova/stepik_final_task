from .base_page import BasePage
from .locators import *
import time

class BasketPage(BasePage):
    def should_not_items(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "Надпись что корзина пуста"

    def should_zero_total(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "Надпись что корзина пуста"



