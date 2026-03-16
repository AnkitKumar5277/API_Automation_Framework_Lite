import pytest
from src.helpers.csv_reader import read_csv
from src.helpers.request_helper import post_request
from src.constants.api_constants import *

data = read_csv("src/data/booking_data.csv")

@pytest.mark.parametrize("booking", data)
def test_create_booking(booking):

    payload = {
        "firstname": booking["firstname"],
        "lastname": booking["lastname"],
        "totalprice": int(booking["totalprice"]),
        "depositpaid": booking["depositpaid"] == "True",
        "bookingdates": {
            "checkin": booking["checkin"],
            "checkout": booking["checkout"]
        },
        "additionalneeds": booking["additionalneeds"]
    }

    response = post_request(BOOKING_ENDPOINT, payload)

    assert response.status_code == 200