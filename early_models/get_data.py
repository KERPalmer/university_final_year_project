# File: get_data.py

import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler

#average true value - simple moving average of the true range
def addATR(data, period=14):
    """
    Compute the Average True Range (ATR) manually.
    """
    # Calculate True Range (TR)
    data['TR'] = np.maximum(data['High'] - data['Low'], 
                            np.maximum(abs(data['High'] - data['Close'].shift(1)), 
                                       abs(data['Low'] - data['Close'].shift(1))))
    
    data['ATR'] = data['TR'].rolling(window=period).mean()
    
    return data

def addRSI(data):
    #RSI = 100 - 100/(1 + RS)
    #RS = avg gain/ avg loss
    delta = data['Close'].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / avg_loss
    data['RSI'] = 100 - (100 / (1 + rs))

    return data

def get_apple_stock_split(days_lag = 5):
    # Download Apple stock data
    data = yf.download("AAPL", start="2015-01-01", end="2024-01-01")

    # Calculate moving averages and relative price change
    data['SMA_10'] = data['Close'].rolling(window=10).mean()
    data['SMA_50'] = data['Close'].rolling(window=50).mean()

    # Set target as next difference in price
    data['Target'] = data['Close'].diff(1)

    # Create lag columns
    lags = {f'lag_{i}': data['Close'].diff(-i) for i in range(1, days_lag + 1)}
    data = data.assign(**lags)

    # add RSI
    data = addRSI(data)

    #add atr
    data = addATR(data)

    # Add day of the week as an integer (Monday=0, ..., Friday=4)
    data['Day_of_Week'] = data.index.dayofweek
    
    # Drop rows with missing values
    data.dropna(inplace=True)

    # Features
    X = data[['SMA_10', 'SMA_50', 'High', 'Close', 'Open', 'Low', 'RSI', 'ATR', 'Day_of_Week'] + [f'lag_{i}' for i in range(1, days_lag + 1)]]
    # Target
    Y = data[['Target']]
    
    # Split data into training and testing sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    
    return X_train, X_test, Y_train, Y_test
    