from model.booking_model import BookingData


def test_create_booking(auth_client):
    booking_data = BookingData.random()
    response = auth_client.create_booking(booking_data)
    assert response == response
