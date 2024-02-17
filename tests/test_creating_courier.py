import pytest
import requests
import random
import allure
from data.data_user import DataUrl


class TestAddCourier:

    @allure.title('Тестирование создания курьера с различными параметрами')
    @allure.description('Создание курьера с полными валидными данными. Ожидание ответа Ок: Тrue')
    def test_create_a_courier_success(self):
        payload = {
            "login": f"Courier{random.randint(1, 1000)}",
            "password": f"password{random.randint(1, 1000)}",
            "firstName": f"Alex{random.randint(1, 1000)}"
        }
        response = requests.post(DataUrl.API_URL + DataUrl.NEW_COURIER_URL, data=payload)
        assert response.status_code == 201
        assert response.text == '{"ok":true}'
        print(response.json())

    @allure.description('Попытка создания курьера без полного набора обязательных данных. '
                        'Ожидание в ответе кода с сообщением об ошибке')
    @pytest.mark.parametrize('login, password, firstName', [
                             ("Cour020", "", "Ivan"),
                             ("", "Pass020", "Ivan"),
                             ("", "", "Ivan")])
    def test_create_courier_missing_data_error(self, login, password, firstName):
        payload = {
            "login": login,
            "password": password,
            "firstName": firstName
        }
        response = requests.post(DataUrl.API_URL + DataUrl.NEW_COURIER_URL, data=payload)
        assert response.status_code == 400
        assert response.text == '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'
        print(response.json())

    @allure.description('Попытка создания второго курьера с данными, которые уже были использованы при создании курьера в фикстуре')
    def test_create_double_courier_error(self, creating_courier):
        payload = {"login": "nellog102",
                   "password": "nelpass102",
                   "firstName": "NelTrauber"}
        response = requests.post(DataUrl.API_URL+DataUrl.NEW_COURIER_URL, json=payload)
        assert response.status_code == 409
        assert response.text == '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'
        print(response.text)
