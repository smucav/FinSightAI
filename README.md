# 🚀 FinSightAI: Time Series Forecasting for Portfolio Management Optimization

> **AI-Powered Market Insights** – Harness time series forecasting and portfolio optimization to transform raw financial data into actionable investment strategies.
---

## 📌 Project Overview

**FinSightAI** is the official repository for the GMF Investments challenge on **time series forecasting** and **portfolio optimization**.
The project covers the **end-to-end process**:

1. **Data Preprocessing & EDA** – Clean and analyze historical financial data.
2. **Forecasting Models** – Develop and compare ARIMA and LSTM models for TSLA price forecasting.
3. **Market Trend Prediction** – 6–12 month forecasts with uncertainty intervals.
4. **Portfolio Optimization** – Modern Portfolio Theory (MPT) to balance risk and return.
5. **Backtesting** – Compare against benchmarks to validate strategy performance.

---

## 🎯 Business Objective

**Guide Me in Finance (GMF) Investments** aims to optimize client portfolios using **data-driven insights**. This project uses historical data for:

* **TSLA** – High-growth, high-volatility stock.
* **BND** – Stable U.S. bond ETF.
* **SPY** – Broad U.S. market exposure ETF.

📅 **Date Range**: **July 1, 2015 → July 31, 2025**
📊 **Data Source**: [Yahoo Finance via `yfinance`](https://pypi.org/project/yfinance/)

---

## 📂 Repository Structure

```
FinSightAI/
│
├── scripts/                 # Python scripts for automation
│   ├── fetch_data.py       # Download and save historical data
│   ├── task2_forecasting.py # ARIMA and LSTM model implementation
│   └── task3_forecasting.py # 6- and 12-month TSLA forecasts
│
├── notebooks/               # Jupyter Notebooks for analysis
│   └── preprocess_eda.ipynb # Data cleaning, EDA, stationarity, risk metrics
│
├── data/                    # Datasets
│   ├── financial_data_clean.csv
│   ├── forecast_metrics.csv # Forecasting model performance metrics
│   ├── forecast_6m.csv      # 6-month TSLA forecast
│   └── forecast_12m.csv     # 12-month TSLA forecast
│
├── figures/                 # Generated plots
│   ├── adj_close_trends.png
│   ├── volatility.png
│   ├── forecast_comparison.png # ARIMA vs LSTM forecast plot
│   └── forecast_6_12_months.png # 6- and 12-month forecast plot
│
├── reports/                 # Reports & submissions
│   └── interim_task1_report.pdf
│
├── requirements.txt         # Python dependencies
└── .gitignore               # Ignored files & folders
```

---

## 🛠 Setup Instructions

1️⃣ **Clone the repository**

```bash
git clone https://github.com/yourusername/FinSightAI.git
cd FinSightAI
```

2️⃣ **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

3️⃣ **Install dependencies**

```bash
pip install -r requirements.txt
```

4️⃣ **Run data fetching script**

```bash
python scripts/fetch_data.py
```

5️⃣ **Run forecasting scripts**

```bash
python scripts/task2_forecasting.py
python scripts/task3_forecasting.py
```

---

## 📊 Key Features

* **Data Preprocessing & EDA**:
  - Fetched and cleaned historical data for TSLA, BND, and SPY using `yfinance`.
  - Performed Exploratory Data Analysis (EDA) to identify trends, volatility, and stationarity.
  - Calculated risk metrics like Value at Risk (VaR) and Sharpe Ratio.
* **Time Series Forecasting**:
  - Implemented **ARIMA(2,1,2)** and **LSTM** models to forecast TSLA adjusted close prices.
  - Chronologically split data: 2015–2023 (training), 2024–2025 (testing).
  - ARIMA used `pmdarima.auto_arima` for optimal parameter selection (AIC: 14042.565).
  - LSTM used a 2-layer architecture with 60-day lookback and 20 epochs.
  - Evaluated models using MAE, RMSE, and MAPE:
    - **ARIMA**: MAE: 63.76, RMSE: 78.89, MAPE: 24.22%
    - **LSTM**: MAE: 67.88, RMSE: 77.58, MAPE: 28.67%
  - ARIMA outperformed LSTM in MAE and MAPE, indicating better average accuracy for TSLA’s volatile prices.
  - Generated forecast comparison plot (`figures/forecast_comparison.png`) and metrics (`data/forecast_metrics.csv`).
* **Market Trend Prediction**:
  - Used ARIMA(2,1,2) to forecast TSLA prices for 6 months (August 2025 – February 2026) and 12 months (August 2025 – July 2026).
  - **6-Month Forecast**: Mean ~$319.28, CI: $216.42–$422.14, CI Width: ~$205.72, Trend: Downward (minimal, ~0.5% decline).
  - **12-Month Forecast**: Mean ~$319.28, CI: $174.21–$464.35, CI Width: ~$290.14, Trend: Downward (minimal).
  - **Analysis**:
    - Flat forecasts suggest stability but limited growth potential.
    - CI width grows 1.41x from 6 to 12 months, indicating increasing uncertainty.
    - Opportunities: Potential upside to $422–$464 if bullish catalysts occur.
    - Risks: Wide CIs suggest significant downside risk (e.g., $174 by July 2026).
  - Generated forecast plot (`figures/forecast_6_12_months.png`) and CSVs (`data/forecast_6m.csv`, `data/forecast_12m.csv`).
* **ARIMA / SARIMA** – Classical time series models for forecasting.
* **LSTM** – Deep learning for sequential data prediction.
* **Volatility Analysis** – Rolling statistics & Value at Risk (VaR).
* **Efficient Frontier** – Portfolio optimization with `PyPortfolioOpt` (upcoming).
* **Backtesting** – Strategy validation against benchmarks (upcoming).

---

## 📚 References

**Time Series**

* [ARIMA in Python – DataCamp](https://www.datacamp.com/tutorial/arima)
* [Machine Learning Mastery: ARIMA](https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/)

**Portfolio Optimization**

* [PyPortfolioOpt GitHub](https://github.com/robertmartin8/PyPortfolioOpt)
* [Portfolio Optimization in Python – AV](https://www.analyticsvidhya.com/blog/2021/04/portfolio-optimization-using-mpt-in-python/)

**Finance Theory**

* [Efficient Market Hypothesis – Investopedia](https://www.investopedia.com/terms/e/efficientmarkethypothesis.asp)

---

## 📄 License

This project is licensed under the **MIT License** – feel free to use, modify, and distribute with attribution.

---

💡 *"Turning data into decisions, and forecasts into financial edge."*
