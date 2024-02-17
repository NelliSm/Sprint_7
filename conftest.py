import pytest
import requests
from data.data_user import DataUrl


@pytest.fixture
def creating_courier():
    payload = {"login": "nellog102",
               "password": "nelpass102",
               "firstName": "NelTrauber"}
    response = requests.post(DataUrl.API_URL + DataUrl.NEW_COURIER_URL, json=payload)
    return response
