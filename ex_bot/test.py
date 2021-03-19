import requests
import json


URL = 'https://api.exchangeratesapi.io/latest?base=USD'


def load_exchange():
    return json.loads(requests.get(URL).text)


def get_exchange(ccy_key):
    for exc in load_exchange():
        if ccy_key == exc['rates']:
            return exc
    return False

