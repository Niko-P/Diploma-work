import allure
from pages.SearchApi import SearchApi
from config import API_URL, BEARER_TOKEN


@allure.title("Добавить продукт в Корзину")
@allure.description("Проверка добавления книги в Корзину")
@allure.severity(allure.severity_level.NORMAL)
def test_add_book_to_cart_test():
    search_api = SearchApi(API_URL, BEARER_TOKEN)

    product_data = {
        "id": 2570683,
        "adData": {
            "item_list_name": "search",
            "product_shelf": ""
        }
    }

    with allure.step("Добавление продукта в Корзину"):
        response = search_api.add_product_to_cart(product_data)

    with allure.step("Проверка кода состояния ответа"):
        assert response.status_code == 200, "Ожидался статус код 200 OK"

    # Проверка содержимого корзины после добавления товара
    with allure.step("Проверка содержимого корзины"):
        cart_response = search_api.get_cart_contents()
        assert cart_response.status_code == 200
        assert len(cart_response.json()) > 0, "Корзина должна содержать товары"


@allure.title("Получить содержимое Корзины")
@allure.description("Тест проверяет содержимое Корзины")
@allure.feature("Управление Корзиной")
@allure.severity(allure.severity_level.NORMAL)
def test_basket_contents_test():
    search_api = SearchApi(API_URL, BEARER_TOKEN)

    with allure.step("Получение содержимого Корзины"):
        response = search_api.get_cart_contents()

    with allure.step("Проверка кода состояния ответа"):
        assert response.status_code == 200

    with allure.step("Проверка, что тело ответа не пустое"):
        assert response.json(), "Корзина пуста!"


@allure.title("Очистить Корзину")
@allure.description("Тест проверяет функциональность очистки Корзины")
@allure.feature("Управление Корзиной")
@allure.severity(allure.severity_level.NORMAL)
def test_clear_cart_test():
    search_api = SearchApi(API_URL, BEARER_TOKEN)

    with allure.step("Очистка Корзины"):
        response = search_api.clear_cart()

    with allure.step("Проверка статус кода: 204 No Content"):
        assert response.status_code == 204

    with allure.step("Проверка тела ответа"):
        assert response.text == '', "Тело ответа должно быть пустым"


@allure.title("Получить список Магазинов")
@allure.description("Получить список Магазинов")
@allure.severity(allure.severity_level.MINOR)
def test_shops_test():
    search_api = SearchApi(API_URL, BEARER_TOKEN)

    with allure.step("Получение списка Магазинов"):
        response = search_api.get_shops()

    with allure.step("Проверка кода состояния ответа (200 OK)"):
        assert response.status_code == 200


@allure.title("Получить список книг по названию")
@allure.description("Получить список книг по названию")
@allure.severity(allure.severity_level.MINOR)
def test_books_by_name_test():
    search_api = SearchApi(API_URL, BEARER_TOKEN)

    with allure.step("Получение списка книг по названию"):
        response = search_api.search_book_by_name()

    with allure.step("Проверка кода состояния ответа (200 OK)"):
        assert response.status_code == 200

    with allure.step("Проверка тела ответа на наличие данных"):
        assert response.json(), "Ответ должен содержать данные о книгах"
