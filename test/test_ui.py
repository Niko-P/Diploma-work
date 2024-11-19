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


@allure.title("Тест: Проверка текста заголовка страницы 'Корзина'")
@allure.description(
    "Тест проверяет корректность текста заголовка на странице корзины."
    )
@allure.severity(allure.severity_level.MINOR)
def test_open_cart(browser):
    main_page = MainPage(browser)
    main_page.open_cart()

    cart_page = ResultPage(browser)
    cart_text = cart_page.get_cart_text()

    with allure.step("Проверка текста заголовка страницы корзины"):
        assert cart_text == "КОРЗИНА", (
            f"Ожидалось 'КОРЗИНА', но получено '{cart_text}'"
        )


@allure.title("Тест: Проверка текста заголовка страницы 'Доставка и оплата'")
@allure.description("Тест проверяет корректность текста заголовка на странице"
                    "'Доставка и оплата'.")
@allure.severity(allure.severity_level.MINOR)
def test_delivery_and_pay(browser):
    main_page = MainPage(browser)
    main_page.delivery_and_pay()

    delivery_page = ResultPage(browser)
    delivery_text = delivery_page.get_delivery_text()

    with allure.step("Проверка текста заголовка страницы 'Доставка и оплата'"):
        assert delivery_text == "ДОСТАВКА И ОПЛАТА", (
            f"Ожидалось 'ДОСТАВКА И ОПЛАТА', но получено '{delivery_text}'"
        )


@allure.title("Тест проверяет корректность текста заголовка на странице"
              "'Подарочные сертификаты'.")
@allure.description("Тест проверяет корректность текста заголовка на странице"
                    "'Подарочные сертификаты'.")
@allure.severity(allure.severity_level.MINOR)
def test_gift_certificate(browser):
    main_page = MainPage(browser)
    main_page.gift_card()

    gift_page = ResultPage(browser)
    gift_text = gift_page.get_gift_text()

    with allure.step(
         "Проверка текста заголовка страницы 'Подарочные сертификаты'"):
        assert gift_text == "Книга – лучший подарок", (
            f"Ожидалось 'Книга – лучший подарок', но получено '{gift_text}'"
        )


@allure.title("Тест: Проверка текста заголовка страницы 'Наши магазины'")
@allure.description(
    "Тест проверяет корректность текста заголовка на странице 'Наши магазины'."
    )
@allure.severity(allure.severity_level.MINOR)
def test_shops(browser):
    main_page = MainPage(browser)
    main_page.shops()

    shops_page = ResultPage(browser)
    shops_text = shops_page.get_shops_text()

    with allure.step("Проверка текста заголовка страницы 'Наши магазины'"):
        assert shops_text == "НАШИ МАГАЗИНЫ", (
            f"Ожидалось 'НАШИ МАГАЗИНЫ', но получено '{shops_text}'"
        )


@allure.title("Тест: Проверка соответствия заголовка книги запросу поиска")
@allure.description("Тест проверяет, соответствует ли заголовок первой книги"
                    "результату поиска.")
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

    with allure.step(
         f"Проверка соответствия заголовка книги запросу '{search_value}'"):
        assert clean_title == search_value, (
            f"Ожидалось '{search_value}', но получено '{first_book_title}'"
        )
