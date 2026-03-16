import requests
from src.constants.api_constants import BASE_URL

def post_request(endpoint, payload, headers=None):
    return requests.post(BASE_URL + endpoint, json=payload, headers=headers)

def get_request(endpoint, headers=None):
    return requests.get(BASE_URL + endpoint, headers=headers)

def put_request(endpoint, payload, headers=None):
    return requests.put(BASE_URL + endpoint, json=payload, headers=headers)

def delete_request(endpoint, headers=None):
    return requests.delete(BASE_URL + endpoint, headers=headers)