import yfinance as yf
import pandas as pd
import os
from datetime import datetime

def fetch_stock_data(ticker="AAPL", start="2020-01-01", end=None, save_dir="data/raw"):
    """
    Downloads historical OHLCV data for a stock and saves it as CSV.
    """
    end = end or datetime.today().strftime("%Y-%m-%d")
    df = yf.download(ticker, start=start, end=end, progress=False)

    if df.empty:
        print(f"⚠️ No data found for {ticker}")
        return

    df.reset_index(inplace=True)
    df["Ticker"] = ticker

    os.makedirs(save_dir, exist_ok=True)
    file_path = os.path.join(save_dir, f"{ticker}_ohlcv.csv")
    df.to_csv(file_path, index=False)
    print(f"✅ Saved {ticker} data to {file_path}")


def fetch_multiple_tickers(tickers, start="2020-01-01", end=None):
    """
    Fetch multiple tickers and save to individual CSVs.
    """
    for ticker in tickers:
        fetch_stock_data(ticker, start, end)


# If you want to test manually
if __name__ == "__main__":
    tickers = ["AAPL", "MSFT", "GOOGL", "TSLA"]
    fetch_multiple_tickers(tickers)
