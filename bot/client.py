from binance.client import Client

API_KEY = ""
API_SECRET = ""

def get_client():
    client = Client(API_KEY, API_SECRET, testnet=True)
    return client