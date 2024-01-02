import pytest


@pytest.fixture()
def create_data_fixture():
    payload = {'account_name': 'test',
               'user[first_name]': 'test',
               'user[last_name]': 'test',
               'user[email]': 'giknifakni@gufum.com',
               'user[password]': '1234qwer',
               'user[password_confirmation]': '1234qwer',
               'user[marketing_emails]': 'false',
               'user[time_zone]': 'Europe/Warsaw',
               'user[timezone]': 'Europe/Warsaw',
               'language': 'en'}
    headers = {}
    files = []
    user = [payload, headers, files]
    return user
