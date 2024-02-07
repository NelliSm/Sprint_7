import requests
import random
import allure
from data.data_user import DataUrl, DataUser


@allure.title('Тестирование создания курьера с различными параметрами')
class TestAddCourier:

    @allure.description('Создание курьера с полными валидными данными. Ожидание ответа Ок: Тrue')
    def test_create_a_courier_success(self):
        payload = {
            "login": f"Courier{random.randint(1, 100)}",
            "password": f"password{random.randint(1, 100)}",
            "firstName": f"Alex{random.randint(1, 100)}"
        }
        response = requests.post(f"{DataUrl.API_URL}/api/v1/courier", data=payload)
        assert response.status_code == 201
        assert response.text == '{"ok":true}'
        print(response.status_code)
        print(response.json())

    @allure.description('Попытка создания двух одинаковых курьеров. Ожидание в ответе кода с сообщением об ошибке')
    def test_create_double_courier_error(self):
        payload = {
            "login": DataUser.LOGIN,
            "password": DataUser.PASSWORD,
            "firstName": "Ivan"
        }
        response = requests.post(f"{DataUrl.API_URL}/api/v1/courier", data=payload)
        assert response.status_code == 409
        assert response.text == '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'
        print(response.status_code)
        print(response.json())

    @allure.description('Попытка создания курьера без полного набора данных. '
                        'Ожидание в ответе кода с сообщением об ошибке')
    def test_create_courier_missing_data_error(self):
        payload = {
            "login": "Cour02",
            "firstName": "Ivan"
        }
        response = requests.post(f"{DataUrl.API_URL}/api/v1/courier", data=payload)
        assert response.status_code == 400
        assert response.text == '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'
        print(response.status_code)
        print(response.json())
