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

pip install pandas matplotlib ccxt numpy


---

## Installation

1. Clone the repository:

git clone git@github.com

:rashallahsar/publicschtuff.git
cd publicschtuff


2. Create a Python virtual environment:

python -m venv venv


3. Activate the virtual environment:

source venv/bin/activate.fish


4. Install required packages:

pip install -r requirements.txt


---

## Usage

Run the main script:

python src/darvas.py --symbol BTC/USDT --exchange kucoin --since-days 180


### Command-line options

- `--symbol` Trading pair, e.g., BTC/USDT  
- `--exchange` Name of exchange, e.g., binance or kucoin  
- `--since-days` Number of past days to fetch and analyze  

---

## Output

- A PNG file named `darvas.png` will be saved in the repository folder.  
- The PNG can be opened manually using `xdg-open darvas.png` on Linux or `open darvas.png` on macOS.  

---

## Recommended Workflow

1. Enter the repository folder:

cd ~/Documents/publicschtuff


2. Activate your virtual environment:

source venv/bin/activate.fish


3. Run the script with your desired symbol and timeframe.  
4. Inspect the generated `darvas.png` for identified Darvas boxes.  
5. Deactivate the environment after work:

deactivate


---

## Notes and Troubleshooting

- Do not commit the `venv` folder; it is machine-specific. Use `.gitignore`.  
- If the API returns a 451 error, your location may be restricted by the exchange. Consider using a different exchange or VPN.  
- To recreate the environment on a new machine: create the venv, activate it, and run `pip install -r requirements.txt`.  
- If `xdg-open` or `open` fails, manually open the PNG with any image viewer.  

---

## License

**Unlicense**  

This is free and unencumbered software released into the public domain. Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.  

For more information, see unlicense.org
