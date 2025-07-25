import requests

def get_countries_by_currency(currency_code):
    url = f"https://restcountries.com/v3.1/currency/{currency_code}"
    return requests.get(url)
