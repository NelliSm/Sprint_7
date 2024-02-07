#import pytest
import requests
import allure
from data.data_user import DataUrl, DataUser


@allure.title('Получение списка заказов')
class TestListOrders:

    @allure.description('Проверка, что в тело ответа возвращается список заказов')
    def test_get_order_list(self):
        response = requests.get(f"{DataUrl.API_URL}/api/v1/orders")
        assert response.status_code == 200
        assert "orders" in response.text
        print(response.status_code)
        print(response.json())
