# publicschtuff: Darvas Box Crypto Analysis

A practical Python project for analyzing cryptocurrency price movements using the **Darvas Box** method. This project is designed for Arch Linux users running **Fish shell**, but it works on any platform that supports Python 3.13+.

---

## Features

- Fetch historical OHLCV (Open, High, Low, Close, Volume) data from exchanges such as **Binance** and **KuCoin** using the **CCXT** library.
- Identify **Darvas boxes** on historical price data to visualize price ranges.
- Generate **PNG plots** for easy review of box patterns.
- Lightweight, extensible, and suitable for testing older financial strategies in crypto markets.

---

## Requirements

- **Python 3.13+**
- **Fish shell** (optional, recommended for virtual environment handling)
- Python packages (installable via pip):

```bash
pip install pandas matplotlib ccxt numpy

