from .pages.product_page import CartPage
import pytest
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = CartPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открыть страницу в браузере
    page.go_to_cart()  # положить товар в корзину
    page.solve_quiz_and_get_code()  # решить загадку
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = CartPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открыть страницу в браузере
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = CartPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открыть страницу в браузере
    page.go_to_cart()  # положить товар в корзину
    page.solve_quiz_and_get_code()  # решить загадку
    page.should_not_be_disappear()
