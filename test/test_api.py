import allure
from pages.SearchApi import SearchApi
from config import API_URL, BEARER_TOKEN


@allure.title("Тест: Добавление продукта в корзину")
@allure.description("Тест проверяет успешное добавление книги в корзину через"
                    "API и корректность содержимого корзины после добавления.")
@allure.severity(allure.severity_level.NORMAL)
def test_add_book_to_cart():
    search_api = SearchApi(API_URL, BEARER_TOKEN)

    product_data = {
        "id": 2570683,
        "adData": {
            "item_list_name": "search",
            "product_shelf": ""
        }
    }

    with allure.step("Добавление продукта в корзину"):
        response = search_api.add_product_to_cart(product_data)

    with allure.step("Проверка кода состояния ответа"):
        assert response.status_code == 200, "Ожидался статус код 200 OK"

    with allure.step("Проверка содержимого корзины"):
        cart_response = search_api.get_cart_contents()
        assert cart_response.status_code == 200
        assert len(cart_response.json()) > 0, "Корзина должна содержать товары"


@allure.title("Тест: Получение содержимого корзины")
@allure.description("Тест проверяет корректность получения"
                    "содержимого корзины через API.")
@allure.feature("Управление корзиной")
@allure.severity(allure.severity_level.NORMAL)
def test_basket_contents():
    search_api = SearchApi(API_URL, BEARER_TOKEN)

    with allure.step("Получение содержимого корзины"):
        response = search_api.get_cart_contents()

    with allure.step("Проверка кода состояния ответа"):
        assert response.status_code == 200

    with allure.step("Проверка, что тело ответа не пустое"):
        assert response.json(), "Корзина пуста!"


@allure.title("Тест: Очистка корзины")
@allure.description("Тест проверяет успешную очистку корзины через API.")
@allure.feature("Управление корзиной")
@allure.severity(allure.severity_level.NORMAL)
def test_clear_cart():
    search_api = SearchApi(API_URL, BEARER_TOKEN)

    with allure.step("Очистка корзины"):
        response = search_api.clear_cart()

    with allure.step("Проверка статус кода ответа"):
        assert response.status_code == 204

    with allure.step("Проверка тела ответа"):
        assert response.text == '', "Тело ответа должно быть пустым"


@allure.title("Тест: Получение списка магазинов")
@allure.description("Тест проверяет успешное получение"
                    "списка магазинов через API.")
@allure.severity(allure.severity_level.MINOR)
def test_shops():
    search_api = SearchApi(API_URL, BEARER_TOKEN)

    with allure.step("Получение списка магазинов"):
        response = search_api.get_shops()

    with allure.step("Проверка кода состояния ответа"):
        assert response.status_code == 200


@allure.title("Тест: Получение списка книг по названию")
@allure.description("Тест проверяет успешное получение списка книг"
                    "по названию через API.")
@allure.severity(allure.severity_level.MINOR)
def test_books_by_name():
    search_api = SearchApi(API_URL, BEARER_TOKEN)

    with allure.step("Получение списка книг по названию"):
        response = search_api.search_book_by_name()

    with allure.step("Проверка кода состояния ответа"):
        assert response.status_code == 200

    with allure.step("Проверка тела ответа на наличие данных"):
        assert response.json(), "Ответ должен содержать данные о книгах"
