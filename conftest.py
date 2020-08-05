import pytest

from api.client_api import Client
from model.auth_model import AuthData


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://restful-booker.herokuapp.com",
        help="enter base_url",
    ),
    parser.addoption(
        "--username", action="store", default="admin", help="enter username",
    ),
    parser.addoption(
        "--password", action="store", default="password123", help="enter password",
    ),


@pytest.fixture()
def client(request):
    url = request.config.getoption("--base-url")
    return Client(url=url)


@pytest.fixture()
def get_password(request):
    return request.config.getoption("--password")


@pytest.fixture()
def get_username(request):
    return request.config.getoption("--username")


@pytest.fixture(scope="session")
def auth_client(request):
    url = request.config.getoption("--base-url")
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")
    client = Client(url=url)
    user_data = AuthData(username=username, password=password)
    client.set_cookies(user_data)
    return client
