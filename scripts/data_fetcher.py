import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

# Data Extraction
def fetch_data(ticker, start_date, end_date):
    """Fetches financial data from Yahoo Finance."""
    data = yf.download(ticker, start=start_date, end=end_date)
    return data
start_date = "2015-01-01"
end_date = "2025-01-31"