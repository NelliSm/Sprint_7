import pytest
import requests
import random
import allure
from data.data_user import DataUrl


@allure.title('Тестирование создания заказа с различными тестовыми данными')
class TestOrder:

    @allure.description('Создание заказа с проверкой параметра color')
    @pytest.mark.parametrize('firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color',
                             [
                                 (f"Name{random.randint(1, 50)}", f"Lastname{random.randint(1, 50)}", f"Moscow, st.1905,{random.randint(1, 99)}", "Лубянка", f"79000000{random.randint(100, 999)}", 1, "2024-03-01", "Hi", ['BLACK']),
                                 (f"Name{random.randint(1, 50)}", f"Lastname{random.randint(1, 50)}", f"Moscow, st.1905,{random.randint(1, 99)}", "Строгино", f"79000000{random.randint(100, 999)}", 1, "2024-03-02", "Hi", ['GREY']),
                                 (f"Name{random.randint(1, 50)}", f"Lastname{random.randint(1, 50)}", f"Moscow, st.1905,{random.randint(1, 99)}", "Кузнецкий мост", f"79000000{random.randint(100, 999)}", 1, "2024-03-03", "Hi", ['BLACK ', 'GREY']),
                                 (f"Name{random.randint(1, 50)}", f"Lastname{random.randint(1, 50)}", f"Moscow, st.1905,{random.randint(1, 99)}", "Бауманская", f"79000000{random.randint(100, 999)}", 1, "2024-03-04", "Hi", [''])
                                 ])
    def test_make_order(self, firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color):

        response = requests.post(f"{DataUrl.API_URL}/api/v1/orders")
        assert response.status_code == 201
        assert "track" in response.text
        print(response.status_code)
        print(response.json())
