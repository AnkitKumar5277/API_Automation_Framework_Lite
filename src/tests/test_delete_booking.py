from src.helpers.request_helper import delete_request
from src.constants.api_constants import *

def test_delete_booking(create_booking, auth_token):

    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={auth_token}"
    }

    response = delete_request(f"{BOOKING_ENDPOINT}/{create_booking}", headers)

    assert response.status_code == 201