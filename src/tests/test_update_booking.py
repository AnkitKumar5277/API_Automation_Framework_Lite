from src.helpers.request_helper import put_request
from src.constants.api_constants import *

def test_update_booking(create_booking, auth_token):

    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={auth_token}"
    }

    payload = {
        "firstname": "Updated",
        "lastname": "User",
        "totalprice": 2000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-05-01",
            "checkout": "2026-05-10"
        },
        "additionalneeds": "Dinner"
    }

    response = put_request(f"{BOOKING_ENDPOINT}/{create_booking}", payload, headers)

    assert response.status_code == 200