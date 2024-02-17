import requests
import allure
from data.data_user import DataUrl


class TestListOrders:

    @allure.title('Получение списка заказов')
    @allure.description('Проверка, что в тело ответа возвращается список заказов')
    def test_get_order_list(self):
        response = requests.get(DataUrl.API_URL + DataUrl.ORDER_LIST_URL)
        assert response.status_code == 200
        assert "orders" in response.text
        print(response.json())
