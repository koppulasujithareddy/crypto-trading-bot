from api import get_crypto_price
from orders import create_order
from logger import logger

print("=" * 50)
print("        CRYPTO TRADING BOT")
print("=" * 50)

# Coin Validation
while True:
    coin = input("Enter Coin (bitcoin/ethereum/solana): ").lower()

    if coin in ["bitcoin", "ethereum", "solana"]:
        break

    print("❌ Invalid coin! Please enter bitcoin, ethereum or solana.")

# BUY / SELL Validation
while True:
    side = input("Enter Side (BUY/SELL): ").upper()

    if side in ["BUY", "SELL"]:
        break

    print("❌ Invalid input! Enter BUY or SELL.")

# MARKET / LIMIT Validation
while True:
    order_type = input("Enter Order Type (MARKET/LIMIT): ").upper()

    if order_type in ["MARKET", "LIMIT"]:
        break

    print("❌ Invalid input! Enter MARKET or LIMIT.")

# Quantity Validation
while True:
    try:
        quantity = float(input("Enter Quantity: "))

        if quantity > 0:
            break

        print("❌ Quantity must be greater than zero.")

    except ValueError:
        print("❌ Enter a valid number.")

# Fetch Live Price
current_price = get_crypto_price(coin)

if current_price is None:
    print("❌ Unable to fetch price.")
    logger.error("Price Fetch Failed")
    exit()

# Limit Order
if order_type == "LIMIT":

    while True:

        try:
            price = float(input("Enter Limit Price: "))

            if price > 0:
                break

            print("❌ Price must be greater than zero.")

        except ValueError:
            print("❌ Enter a valid price.")

else:
    price = current_price

# Create Order
order = create_order(
    coin,
    side,
    order_type,
    quantity,
    price
)

logger.info(
    f"{side} {coin} {order_type} Qty:{quantity} Price:{price}"
)

print("\n" + "=" * 50)
print("        ORDER SUCCESSFUL")
print("=" * 50)

for key, value in order.items():
    print(f"{key:<15}: {value}")

print("=" * 50)
print("Thank You For Using Crypto Trading Bot")