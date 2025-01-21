from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import pytest

# Добавляем аргумент командной строки
def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default="en"
    )

# Фикстура для получения значения аргумента
@pytest.fixture
def language(request):
    return request.config.getoption("--language")


@pytest.fixture
def browser(language):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
