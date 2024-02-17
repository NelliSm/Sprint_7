import requests
import random
import allure
from data.data_user import DataUrl, DataUser


class TestLoginCourier:

    @allure.title('Тестирование авторизации курьера с различными параметрами')
    @allure.description('Авторизация курьера с полными валидными данными. Ожидание в ответе id курьера')
    def test_login_a_courier_success(self):
        payload = {
            "login": DataUser.LOGIN,
            "password": DataUser.PASSWORD
        }
        response = requests.post(DataUrl.API_URL + DataUrl.LOGIN_COURIER_URL, data=payload)
        assert response.status_code == 200
        assert "id" in response.text
        print(response.json())

    @allure.description('Попытка авторизации курьера без полного набора данных. Ожидание в ответе кода с сообщением об ошибке')
    def test_login_a_courier_missing_data_error(self):
        payload = {
            "password": DataUser.PASSWORD
        }
        response = requests.post(DataUrl.API_URL + DataUrl.LOGIN_COURIER_URL, data=payload)
        assert response.status_code == 400
        assert response.text == '{"code":400,"message":"Недостаточно данных для входа"}'
        print(response.json())

    @allure.description('Попытка авторизации курьера с использованием несуществующих данных. Ожидание в ответе кода с сообщением об ошибке')
    def test_login_a_courier_fake_data_error(self):
        login = f"Courier{random.randint(1, 100)}"
        password = f"Pass{random.randint(1, 100)}"
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(DataUrl.API_URL + DataUrl.LOGIN_COURIER_URL, data=payload)
        assert response.status_code == 404
        assert response.text == '{"code":404,"message":"Учетная запись не найдена"}'
        print(response.json())
