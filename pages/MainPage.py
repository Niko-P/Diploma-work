from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from config import UI_URL


class MainPage:
    def __init__(self, driver: WebDriver):

        # Инициализация главной страницы.

        self._driver: WebDriver = driver
        self._driver.get(UI_URL)
        self._driver.implicitly_wait(5)
        self._driver.maximize_window()

    @allure.step("Перейти в корзину")
    def open_cart(self) -> None:

        cart_button = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/cart']"))
        )
        cart_button.click()

    @allure.step("Перейти на страницу Доставка и оплата")
    def delivery_and_pay(self) -> None:
        delivery_button = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'a[href="/delivery"]'))
        )
        delivery_button.click()

    @allure.step("Перейти на страницу Подарочные сертификаты")
    def gift_card(self) -> None:
        gift_button = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'a[href="/certificate"]')
                )
        )
        gift_button.click()

    @allure.step("Перейти на страницу магазинов")
    def shops(self) -> None:
        shops_button = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'a[href="/shops"]'))
        )
        shops_button.click()

    @allure.step("Поиск книги")
    def find_books(self, value: str):
        self._driver.find_element(
            By.CSS_SELECTOR, "input.header-search__input"
            ).send_keys(value + Keys.RETURN)
