import yfinance as yf
import pandas as pd
import numpy as np
import os

# Define tickers and date range
tickers = ['TSLA', 'BND', 'SPY']
start_date = '2015-07-01'
end_date = '2025-07-31'

# Create output directory if it doesn't exist
os.makedirs('../data', exist_ok=True)

# Fetch real data using yfinance with auto_adjust=False
try:
    data = yf.download(tickers, start=start_date, end=end_date, group_by='ticker', auto_adjust=False)
    if data.empty:
        raise ValueError("No data retrieved from yfinance. Check ticker symbols or date range.")
except Exception as e:
    print(f"Error fetching data: {e}")
    exit(1)

# Initialize an empty DataFrame with business day index
rng = pd.date_range(start=start_date, end=end_date, freq='B')
flat_data = pd.DataFrame(index=rng)

# Flatten the multi-indexed yfinance data
for ticker in tickers:
    if ticker in data:
        try:
            flat_data[f'{ticker}_Open'] = data[ticker]['Open']
            flat_data[f'{ticker}_High'] = data[ticker]['High']
            flat_data[f'{ticker}_Low'] = data[ticker]['Low']
            flat_data[f'{ticker}_Close'] = data[ticker]['Close']
            flat_data[f'{ticker}_Adj Close'] = data[ticker]['Adj Close']
            flat_data[f'{ticker}_Volume'] = data[ticker]['Volume']
        except KeyError as e:
            print(f"Column missing for {ticker}: {e}")
            exit(1)
    else:
        print(f"No data for {ticker}")
        exit(1)

# Data cleaning
flat_data.index = pd.to_datetime(flat_data.index)  # Ensure datetime index
flat_data = flat_data.asfreq('B')  # Set business day frequency
flat_data.fillna(method='ffill', inplace=True)  # Forward fill missing values
flat_data.fillna(method='bfill', inplace=True)  # Backward fill any remaining

# Verify data integrity
print("Data Info:")
print(flat_data.info())
print("\nMissing Values:")
print(flat_data.isna().sum())

# Save to CSV
output_path = '../data/financial_data_clean.csv'
flat_data.to_csv(output_path, index=True)
print(f"\nData saved to {output_path}")
print("\nFirst 5 rows of data:")
print(flat_data.head())
