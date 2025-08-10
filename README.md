# 🚀 FinSightAI: Time Series Forecasting for Portfolio Management Optimization

> **AI-Powered Market Insights** – Harness time series forecasting and portfolio optimization to transform raw financial data into actionable investment strategies.
---

## 📌 Project Overview

**FinSightAI** is the official repository for the GMF Investments challenge on **time series forecasting** and **portfolio optimization**.
The project covers the **end-to-end process**:

1. **Data Preprocessing & EDA** – Clean and analyze historical financial data.
2. **Forecasting Models** – ARIMA, SARIMA, and LSTM.
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
│   └── fetch_data.py        # Download and save historical data
│
├── notebooks/               # Jupyter Notebooks for analysis
│   └── preprocess_eda.ipynb # Data cleaning, EDA, stationarity, risk metrics
│
├── data/                    # Datasets
│   └── financial_data_clean.csv
│
├── figures/                 # Generated plots
│   ├── adj_close_trends.png
│   └── volatility.png
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

---

## 📊 Key Features

* **ARIMA / SARIMA** – Classical time series models for forecasting.
* **LSTM** – Deep learning for sequential data prediction.
* **Volatility Analysis** – Rolling statistics & Value at Risk (VaR).
* **Efficient Frontier** – Portfolio optimization with `PyPortfolioOpt`.
* **Backtesting** – Strategy validation against benchmarks.

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
