import json

import pytest
import requests
from test_data import create_data_fixture


class TestLoginAndRegistration:

    @pytest.mark.positive
    def test_registration(self, create_data_fixture):
        url = "https://web.teambooktest.com/api/register/validate"
        data = create_data_fixture
        payload = data[0]
        headers = data[1]
        files = data[2]
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        print(response.text)
        assert response.status_code == 201

    @pytest.mark.positive
    def test_validation(self, create_data_fixture):
        url = "https://web.teambooktest.com/api/register"
        data = create_data_fixture
        payload = data[0]
        headers = data[1]
        files = data[2]
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        print(response.text)
        assert response.status_code == 201

    def test_registration_invalid_password(self, create_data_fixture):
        url = "https://web.teambooktest.com/api/register"
        data = create_data_fixture
        payload = data[0]
        data[0].update({'user[email]': 'metrikalte@'})
        headers = data[1]
        files = data[2]
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        print(response.text)
        assert response.status_code == 422
