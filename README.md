# Risk and Return Analysis of TSLA, BND, and SPY

This repository contains the analysis and results of a comparative study on the risk and return characteristics of three financial assets: Tesla Inc. (TSLA), Vanguard Total Bond Market ETF (BND), and SPDR S&P 500 ETF (SPY). The analysis focuses on calculating and interpreting Value at Risk (VaR) and Sharpe Ratio, along with time series decomposition and volatility assessment.

## Project Overview

The project aims to provide a comprehensive understanding of the risk-return profiles of TSLA, BND, and SPY. By calculating VaR and Sharpe Ratio, we quantify the potential losses and risk-adjusted returns for each asset. Additionally, time series decomposition and volatility analysis offer insights into the underlying patterns and fluctuations of their price movements.

## Files

* **`analysis.ipynb`**: Jupyter Notebook containing the Python code for data analysis, calculations, and visualizations.
* **`data/tsla_data.csv`**: CSV file containing historical price data for TSLA.
* **`data/bnd_data.csv`**: CSV file containing historical price data for BND.
* **`data/spy_data.csv`**: CSV file containing historical price data for SPY.
* **`README.md`**: This file, providing an overview of the project.

## Methodology

1.  **Data Acquisition:** Historical price data for TSLA, BND, and SPY was downloaded and stored in CSV files.
2.  **Data Preparation:** The data was cleaned and formatted for analysis.
3.  **Daily Returns Calculation:** Daily percentage changes (daily returns) were calculated to assess volatility.
4.  **Volatility Analysis:** Daily returns were plotted to visualize volatility. Rolling mean and standard deviation were calculated to further analyze volatility trends.
5.  **Time Series Decomposition:** The time series data was decomposed into trend, seasonal, and residual components to understand underlying patterns.
6.  **VaR Calculation:** Value at Risk (VaR) at a 95% confidence level was calculated to estimate potential losses.
7.  **Sharpe Ratio Calculation:** Sharpe Ratio was calculated (assuming a risk-free rate of 0) to assess risk-adjusted returns.
8.  **Results Interpretation:** The calculated VaR and Sharpe Ratio, along with the time series decomposition and volatility analysis, were interpreted to draw conclusions about the risk-return profiles of the assets.

## Results

* **TSLA:** High volatility, high potential losses (VaR: -0.051387), and moderate risk-adjusted returns (Sharpe Ratio: 0.054218).
* **BND:** Low volatility, low potential losses (VaR: -0.004801), and low risk-adjusted returns (Sharpe Ratio: 0.018204).
* **SPY:** Moderate volatility, moderate potential losses (VaR: -0.016719), and moderate risk-adjusted returns (Sharpe Ratio: 0.050239).

## Conclusion

The analysis highlights the distinct risk-return profiles of TSLA, BND, and SPY. TSLA is suited for high-risk, high-reward seekers, BND for risk-averse investors, and SPY for those seeking a balanced approach. The VaR and Sharpe Ratio calculations, along with the time series decomposition and volatility analysis, provide valuable insights for making informed investment decisions.

## Dependencies

* Python 3.x
* Pandas
* NumPy
* Matplotlib
* Statsmodels
