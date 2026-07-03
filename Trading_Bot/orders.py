import random
import json
import os
from datetime import datetime

FILE_NAME = "orders.json"


def create_order(symbol, side, order_type, quantity, price):

    order = {
        "order_id": random.randint(100000, 999999),
        "symbol": symbol.upper(),
        "side": side.upper(),
        "order_type": order_type.upper(),
        "quantity": quantity,
        "price": price,
        "status": "SUCCESS",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    save_order(order)

    return order


def save_order(order):

    if os.path.exists(FILE_NAME):

        try:
            with open(FILE_NAME, "r") as file:
                orders = json.load(file)

        except json.JSONDecodeError:
            orders = []

    else:
        orders = []

    orders.append(order)

    with open(FILE_NAME, "w") as file:
        json.dump(orders, file, indent=4)