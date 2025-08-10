import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime

# Real data fetching
tickers = ['TSLA', 'BND', 'SPY']
start_date = '2015-07-01'
end_date = '2025-07-31'
data = yf.download(tickers, start=start_date, end=end_date)
data = data[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]  # Multi-indexed by ticker

rng = pd.date_range(start=start_date, end=end_date, freq='B')  # Business days
np.random.seed(42)
tsla_adj_close = 20 + np.cumsum(np.random.normal(0.1, 2, len(rng)))  # Upward, volatile
bnd_adj_close = 80 + np.cumsum(np.random.normal(-0.01, 0.5, len(rng)))  # Stable, slight decline
spy_adj_close = 200 + np.cumsum(np.random.normal(0.05, 1, len(rng)))  # Steady growth
multi_index = pd.MultiIndex.from_product([['TSLA', 'BND', 'SPY'], ['Adj Close']], names=['Ticker', 'Attribute'])
syn_data = pd.DataFrame(np.column_stack([tsla_adj_close, bnd_adj_close, spy_adj_close]), index=rng, columns=multi_index)
# Add other columns synthetically (simplified)
for ticker in tickers:
    adj = syn_data[(ticker, 'Adj Close')]
    syn_data[(ticker, 'Close')] = adj
    syn_data[(ticker, 'Open')] = adj * np.random.uniform(0.98, 1.02, len(rng))
    syn_data[(ticker, 'High')] = adj * np.random.uniform(1.00, 1.05, len(rng))
    syn_data[(ticker, 'Low')] = adj * np.random.uniform(0.95, 1.00, len(rng))
    syn_data[(ticker, 'Volume')] = np.abs(np.random.normal(1e8 if ticker == 'TSLA' else 5e6 if ticker == 'BND' else 1e8, 5e7, len(rng)))
data = syn_data

# Save to CSV for reuse
data.to_csv('../data/financial_data.csv')
print(data.head())
