from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import allure


class ResultPage:
    def __init__(self, driver: WebDriver):

        # Инициализация страницы результатов.

        self._driver: WebDriver = driver

    @allure.step("Получить содержимое корзины")
    def get_cart_text(self) -> str:

        cart_text = WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h1"))
        )
        return cart_text.text

    @allure.step("Получить текст Доставка и оплата")
    def get_delivery_text(self) -> str:

        delivery_text = WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h1"))
        )
        return delivery_text.text

    @allure.step("Получить текст Книга - лучший подарок")
    def get_gift_text(self) -> str:

        gift_text = WebDriverWait(self._driver, 40).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h1"))
        )
        return gift_text.text

    @allure.step("Получить текст страницы магазинов")
    def get_shops_text(self) -> str:

        shops_text = WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h1"))
        )
        return shops_text.text

    @allure.step("Получить заголовок первой книги в списке после поиска")
    def get_book_title(self) -> str:

        book_element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH,
                 '//*[@id="__layout"]/div/div[3]/div[1]/div/div/'
                 'div[1]/section/section/div/article[1]/div[2]/a/div/div[1]')
            )
        )
        return book_element.text
