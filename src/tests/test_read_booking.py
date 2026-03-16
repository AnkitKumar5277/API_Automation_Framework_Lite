from src.helpers.request_helper import get_request
from src.constants.api_constants import *

def test_read_booking(create_booking):

    response = get_request(f"{BOOKING_ENDPOINT}/{create_booking}")

    assert response.status_code == 200