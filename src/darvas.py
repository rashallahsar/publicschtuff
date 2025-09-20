import ccxt
import pandas as pd
import numpy as np
import argparse
import datetime
import matplotlib.pyplot as plt
import os
import subprocess
import sys

# Fetch OHLCV data
def fetch_ohlcv(exchange_id='kucoin', symbol='BTC/USDT', timeframe='1d', since=None, limit=500):
    ex_cls = getattr(ccxt, exchange_id)
    ex = ex_cls({'enableRateLimit': True})
    data = ex.fetch_ohlcv(symbol, timeframe=timeframe, since=since, limit=limit)
    df = pd.DataFrame(data, columns=['ts','open','high','low','close','vol'])
    df['ts'] = pd.to_datetime(df['ts'], unit='ms')
    df.set_index('ts', inplace=True)
    return df

# Simple naive Darvas box calculation
def darvas_boxes(df, lookback=10):
    highs = df['high']
    local_high = highs[(highs == highs.rolling(window=2*lookback+1, center=True).max())]
    local_highs = local_high.dropna()
    boxes = []
    for i in range(len(local_highs)-1):
        t1, h1 = local_highs.index[i], local_highs.iloc[i]
        t2, h2 = local_highs.index[i+1], local_highs.iloc[i+1]
        box_top = min(h1, h2)
        box_bottom = df.loc[t1:t2]['low'].min()
        boxes.append({'t1': t1, 't2': t2, 'top': box_top, 'bottom': box_bottom})
    return boxes

# Plot the Darvas boxes and save/open PNG
def plot_boxes(df, boxes, out='darvas.png'):
    fig, ax = plt.subplots(figsize=(12,6))
    ax.plot(df.index, df['close'], label='close')
    
    for b in boxes:
        ax.hlines(b['top'], b['t1'], b['t2'], linestyle='dashed')
        ax.hlines(b['bottom'], b['t1'], b['t2'], linestyle='dotted')
        ax.axvspan(b['t1'], b['t2'], alpha=0.08)
    
    ax.set_title('Darvas boxes (naive)')
    ax.legend()
    plt.savefig(out)
    print(f"Saved plot to {out}")

    # Auto-open image on Linux
    try:
        if sys.platform.startswith('linux'):
            subprocess.run(['xdg-open', out])
    except Exception as e:
        print(f"Could not open image automatically: {e}")

# Main function
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--exchange', default='kucoin')
    parser.add_argument('--symbol', default='BTC/USDT')
    parser.add_argument('--timeframe', default='1d')
    parser.add_argument('--since-days', type=int, default=365)
    args = parser.parse_args()

    since = int((pd.Timestamp.utcnow() - pd.Timedelta(days=args.since_days)).timestamp() * 1000)
    df = fetch_ohlcv(args.exchange, args.symbol, args.timeframe, since=since, limit=1000)
    
    boxes = darvas_boxes(df, lookback=5)
    
    os.makedirs('data', exist_ok=True)
    csv_path = f"data/{args.symbol.replace('/','_')}.csv"
    df.to_csv(csv_path)
    print(f"Saved CSV to {csv_path}")
    
    png_path = f"data/{args.symbol.replace('/','_')}_darvas.png"
    plot_boxes(df, boxes, out=png_path)

if __name__ == '__main__':
    main()
