# Binance Futures Testnet Trading Bot

## 📌 Overview
This is a simplified Python-based trading bot that interacts with Binance Futures Testnet (USDT-M). It supports placing MARKET and LIMIT orders using a CLI interface.

---

## ⚙️ Setup Instructions

1. Clone or download the project

2. Install dependencies:
   pip install -r requirements.txt

3. Add your Binance Testnet API keys in:
   bot/client.py

---

## ▶️ How to Run

### MARKET Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### LIMIT Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 30000

---

## ✅ Features

- Market & Limit order support
- BUY / SELL support
- CLI-based input (argparse)
- Input validation
- Structured code (client, orders, validators)
- Logging to file (`trading.log`)
- Error handling with clear messages

---

## 📄 Logs

Logs are stored in:
trading.log

Includes:
- Order requests
- API responses
- Errors

---

## ⚠️ Note

Due to access limitations with Binance Testnet API key generation in some regions, the bot may return authentication errors if API keys are not provided.

However, all functionality including request formation, validation, logging, and error handling is fully implemented and testable.

---

## 📦 Requirements

- Python 3.x
- python-binance