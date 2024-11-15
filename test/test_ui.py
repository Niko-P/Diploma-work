import pytest
import allure
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.MainPage import MainPage
from pages.ResultPage import ResultPage


# Фикстура для инициализации браузера
@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тестирование Корзины")
@allure.description("Проверка текста заголовка страницы Корзины")
@allure.severity(allure.severity_level.MINOR)
def test_open_cart(browser):
    main_page = MainPage(browser)
    main_page.open_cart()

    cart_page = ResultPage(browser)
    cart_text = cart_page.get_cart_text()

    with allure.step("Проверка текста заголовка Корзины"):
        assert cart_text == "КОРЗИНА", (
            f"Expected 'Корзина' but got '{cart_text}'"
        )


@allure.title("Тестирование открытия страницы Доставка и оплата")
@allure.description("Проверка текста заголовка страницы Доставка и оплата.")
@allure.severity(allure.severity_level.MINOR)
def test_delivery_and_pay(browser):
    main_page = MainPage(browser)
    main_page.delivery_and_pay()

    delivery_page = ResultPage(browser)
    delivery_text = delivery_page.get_delivery_text()

    with allure.step("Проверка текста заголовка Доставка и оплата"):
        assert delivery_text == "ДОСТАВКА И ОПЛАТА", (
            f"Expected 'ДОСТАВКА И ОПЛАТА' but got '{delivery_text}'"
        )


@allure.title("Тестирование страницы Подарочные сертификаты")
@allure.description("Проверка текста заголовка стр Подарочные сертификаты")
@allure.severity(allure.severity_level.MINOR)
def test_gift_certificate(browser):
    main_page = MainPage(browser)
    main_page.gift_card()

    gift_page = ResultPage(browser)
    gift_text = gift_page.get_gift_text()

    with allure.step("Проверка текста заголовка"):
        assert gift_text == "Книга – лучший подарок", (
            f"Expected 'Книга – лучший подарок' but got '{gift_text}'"
        )


@allure.title("Тестирование страницы Магазинов")
@allure.description("Проверка текста заголовка страницы магазинов")
@allure.severity(allure.severity_level.MINOR)
def test_shops(browser):
    main_page = MainPage(browser)
    main_page.shops()

    shops_page = ResultPage(browser)
    shops_text = shops_page.get_shops_text()

    with allure.step("Проверка текста заголовка Магазинов"):
        assert shops_text == "НАШИ МАГАЗИНЫ", (
            f"Expected 'НАШИ МАГАЗИНЫ' but got '{shops_text}'"
        )


@allure.title("Проверка соответствия заголовка книги поиску")
@allure.description("Проверка соответствия заголовка книги поиску")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize(
    "search_value", ["Колобок", "Война и мир", "Преступление и наказание"]
    )
def test_find_book(browser, search_value):
    main_page = MainPage(browser)
    main_page.find_books(search_value)

    result_page = ResultPage(browser)
    first_book_title = result_page.get_book_title()

    # Используем регулярные выражения для очистки названия книги
    clean_title = re.sub(r"\s*\(.*\)\s*", "", first_book_title).strip()

    assert clean_title == search_value, (
        f"Expected '{search_value}' "
        f"but got '{first_book_title}'"
    )
