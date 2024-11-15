import requests
from requests import Response


class SearchApi:
    def __init__(self, url: str, token: str):
        # url: URL для доступа к API.
        # param token: Токен

        self.url = url
        self.headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }

    def add_product_to_cart(self, product_data: dict) -> Response:
        # Добавление продукта product_data в корзину.
        resp = requests.post(
            self.url + '/cart/product', json=product_data,
            headers=self.headers
            )
        return resp

    def get_cart_contents(self) -> Response:
        # Получает содержимое корзины.
        resp = requests.get(self.url + '/cart', headers=self.headers)
        return resp

    def clear_cart(self) -> Response:
        # Очищает корзину.
        resp = requests.delete(self.url + '/cart', headers=self.headers)
        return resp

    def get_shops(self, params: dict = None) -> Response:
        # Получает список магазинов.
        resp = requests.get(
            self.url + '/shops-cities', params=params, headers=self.headers)
        return resp

    def search_book_by_name(self, params: dict = None) -> Response:
        # Ищет книгу по названию.
        resp = requests.get(
            self.url + '/products/series/voyna-i-mir-46298',
            params=params, headers=self.headers
            )
        return resp
