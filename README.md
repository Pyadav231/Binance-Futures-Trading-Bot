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