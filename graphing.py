# File: graphing.py

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
import pandas as pd


def graph_normal(predictions, actual, title):
    """
    Visualize predictions vs. actual outcomes and calculate error metrics.

    Parameters:
        predictions (array-like): Predicted values.
        actual (array-like): Actual values.
        title (str): Title for the plot.
    """
    # Visualize Predictions vs. Actual Outcomes
    plt.figure(figsize=(8, 6))
    plt.scatter(actual, predictions, alpha=0.7, color='b', label='Predicted vs Actual')
    plt.plot([predictions.min(), predictions.max()], [predictions.min(), predictions.max()], 'r--', lw=2, label='Perfect Prediction')
    plt.title(f'{title}: Actual vs Predicted Values', fontsize=14)
    plt.xlabel('Actual Values', fontsize=12)
    plt.ylabel('Predicted Values', fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(True)
    plt.show()

def show_results(results):
    results_df = pd.DataFrame(results).sort_values(by='mean_test_score', ascending=False)
    for i, row in results_df.iterrows():
        print(f"Rank {row['rank_test_score']}:")
        print(f"Parameters: {row['params']}")
        print(f"Mean Test Score: {row['mean_test_score']:.4f}")
        print(f"Std Dev of Test Score: {row['std_test_score']:.4f}")
        print("-" * 30)

def graph_line(predictions, actual, title):
    x = range(len(actual))
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, actual, label='Actual', marker='o')
    plt.plot(x, predictions, label='Predicted', marker='x')
    plt.xlabel('Time Step')
    plt.ylabel('Difference')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


