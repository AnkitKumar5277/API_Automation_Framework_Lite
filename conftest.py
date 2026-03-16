import pytest
from src.helpers.request_helper import post_request
from src.constants.api_constants import *

@pytest.fixture()
def auth_token():

    payload = {
        "username": "admin",
        "password": "password123"
    }

    response = post_request(AUTH_ENDPOINT, payload)

    assert response.status_code == 200
    return response.json()["token"]


@pytest.fixture()
def create_booking():

    payload = {
        "firstname": "Ankit",
        "lastname": "Kumar",
        "totalprice": 1500,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-01-10",
            "checkout": "2026-01-15"
        },
        "additionalneeds": "Breakfast"
    }

    response = post_request(BOOKING_ENDPOINT, payload)

    assert response.status_code == 200
    return response.json()["bookingid"]