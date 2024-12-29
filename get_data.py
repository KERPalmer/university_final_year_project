# File: get_data.py

import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler


def get_apple_stock_split(scaler_X, scaler_Y):
    # Download Apple stock data
    data = yf.download("AAPL", start="2015-01-01", end="2023-01-01")

    # Calculate moving averages and relative price change
    data['SMA_10'] = data['Close'].rolling(window=10).mean()
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    data['Price_Change'] = data['Close'].pct_change()

    # set target as next days close
    data['Target'] = data['Close'].shift(-1)

    # Drop rows with missing values
    data.dropna(inplace=True)

    #inputs
    X = data[['SMA_10', 'SMA_50','Price_Change', 'High', 'Close', 'Open', 'Low']]
    X_scaled = scaler_X.fit_transform(X)

    #target
    y = data['Target']
    Y_scaled = scaler_Y.fit_transform(y.to_frame()).ravel()
    
    # Split data into training and testing sets
    X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y_scaled, test_size=0.2, random_state=42)
    return X_train, X_test, Y_train, Y_test


