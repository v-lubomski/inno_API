from model.auth_model import AuthData


def test_login(client, get_username, get_password):
    response = client.auth(AuthData(username=get_username, password=get_password))
    assert response.status_code == 200
