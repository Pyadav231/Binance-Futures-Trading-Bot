<<<<<<< HEAD
# Binance Futures Testnet Trading Bot

## Setup

1. Clone repo
2. Create .env file with API credentials
3. Install dependencies:

pip install -r requirements.txt

## Run Examples

Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

Limit Order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 60000

## Logs
All API requests, responses and errors are logged in bot.log
=======
# Binance-Futures-Trading-Bot
An automated Binance Futures trading bot built in Python using Binance API. Supports market and limit orders with real-time price tracking and risk management.
>>>>>>> a9d5bdee39e20695ad1f75530a59b10761bf78fa
