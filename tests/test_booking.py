import pytest

from model.booking_model import BookingData

# Positive tests


def test_create_booking(auth_client):
    """Проверка успешного бронирования."""
    booking_data = BookingData.random()
    response = auth_client.create_booking(booking_data)
    assert response.status_code == 200


def test_req_res_data_matched(auth_client):
    """Проверка совпадения отправленных и поступивших данных брони."""
    booking_data = BookingData.random()
    response = auth_client.create_booking(booking_data)
    req_dict = booking_data.__dict__
    res_dict = response.json()["booking"]
    req_dict["bookingdates"] = req_dict["bookingdates"].__dict__
    assert res_dict == req_dict


# Negative tests


@pytest.mark.xfail(reason="bug on the service side")
@pytest.mark.parametrize(
    "checkin, checkout",
    [
        ("2006-09-15", "2000-01-04"),
        ("2019-10-10", "2019-03-14"),
        ("2006-09-15", "2000-01-04"),
    ],
)
def test_messed_dates(auth_client, checkin, checkout):
    """Проверка, что невозможно выписаться раньше, чем вписаться."""
    booking_data = BookingData.random()
    booking_data.bookingdates.checkin = checkin
    booking_data.bookingdates.checkout = checkout
    response = auth_client.create_booking(booking_data)
    assert response.status_code != 200


@pytest.mark.xfail(reason="bug on the service side")
@pytest.mark.parametrize(
    "checkin, checkout", [("23-02-1992", "08-03-1992"), ("1945-05-09", "09-05-2020")]
)
def test_wrong_data_format(auth_client, checkin, checkout):
    """Проверка валидации формата дат."""
    booking_data = BookingData.random()
    booking_data.bookingdates.checkin = checkin
    booking_data.bookingdates.checkout = checkout
    response = auth_client.create_booking(booking_data)
    assert response.status_code != 200


@pytest.mark.xfail(reason="bug on the service side")
def test_wrong_type_for_price(auth_client):
    """Проверка валидации типа данных стоимости брони."""
    booking_data = BookingData.random()
    booking_data.totalprice = "one hundred"
    response = auth_client.create_booking(booking_data)
    assert response.status_code != 200
