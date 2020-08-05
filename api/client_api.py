import requests

from model.auth_model import AuthData
from model.booking_model import BookingData


class Client:
    s = requests.Session()

    def __init__(self, url: str):
        self.url = url

    def auth(self, user_data: AuthData):
        data = user_data.__dict__
        return self.s.post(self.url + "/auth", json=data)

    def set_cookies(self, user_data: AuthData):
        response = self.auth(user_data)
        token = response.json().get("token")
        cookie = requests.cookies.create_cookie("token", token)
        self.s.cookies.set_cookie(cookie)

    def create_booking(self, booking_data: BookingData):
        booking = booking_data.object_to_dict()
        return self.s.post(self.url + "/booking", json=booking)
