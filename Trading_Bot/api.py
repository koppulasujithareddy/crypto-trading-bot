import requests

BASE_URL = "https://api.coingecko.com/api/v3"


def get_crypto_price(coin):
    """
    Fetch current USD price of a cryptocurrency.
    """

    url = f"{BASE_URL}/simple/price"

    params = {
        "ids": coin.lower(),
        "vs_currencies": "usd"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:

            data = response.json()

            if coin.lower() in data:
                return data[coin.lower()]["usd"]

            return None

        else:
            print("API Error:", response.status_code)
            return None

    except requests.exceptions.Timeout:
        print("Request Timed Out.")
        return None

    except requests.exceptions.ConnectionError:
        print("No Internet Connection.")
        return None

    except Exception as e:
        print("Unexpected Error:", e)
        return None