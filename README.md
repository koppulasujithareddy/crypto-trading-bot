# 🚀 Crypto Trading Bot

A Python-based Crypto Trading Bot that fetches live cryptocurrency prices using the CoinGecko API and simulates BUY/SELL orders. The project includes input validation, logging, and local order history management.

## 📌 Features

- 🔹 Fetches live cryptocurrency prices using the CoinGecko API
- 🔹 Supports BUY and SELL orders 
- 🔹 Supports MARKET and LIMIT order types
- 🔹 Input validation for user-friendly interaction
- 🔹 Error handling for invalid inputs and API failures
- 🔹 Saves order history in `orders.json`
- 🔹 Logs all activities in `logs/trading.log`
- 🔹 Simple command-line interface (CLI)

## 🛠 Technologies Used

- Python 3
- CoinGecko API
- Requests
- JSON
- Logging Module

## 📂 Project Structure

```
Trading_Bot/
│── api.py
│── logger.py
│── main.py
│── orders.py
│── orders.json
│── requirements.txt
└── logs/
    └── trading.log
```

## ⚙️ Installation

1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/crypto-trading-bot.git
```

2. Navigate to the project

```bash
cd crypto-trading-bot
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the project

```bash
python main.py
```

## 📷 Sample Output

```
==================================================
        CRYPTO TRADING BOT
==================================================

Enter Coin: bitcoin
Enter Side: BUY
Enter Order Type: MARKET
Enter Quantity: 2

==================================================
ORDER SUCCESSFUL
==================================================

order_id : 123456
symbol : BITCOIN
side : BUY
order_type : MARKET
quantity : 2
price : 62050
status : SUCCESS
```

## 📌 Future Improvements

- Binance Testnet Integration
- Portfolio Management
- Real-time Price Monitoring
- Graphical User Interface (GUI)
- Database Storage
- Multiple Cryptocurrency Support

## 👩‍💻 Author

**Koppula Sujitha Reddy**

B.Tech – Computer Science Engineering (AI & ML)

