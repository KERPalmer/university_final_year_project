# File: results.py

import pandas as pd
import numpy as np

"""
given a list of predictions and the true value return how much the model would have made
"""
def get_predictived_earnings(prediction, actual):
    pass


"""
given a list of predictions and the true value return how many times the model predicted the correct direction
"""
def get_num_correct_direction(predictions, real):
    actual = pd.DataFrame()
    actual["Target"] = real

    actual["diff"] = actual['Target'].diff()
    actual["prediction"] = predictions
    actual["predicted_diff"] = actual["prediction"] - actual["Target"].shift(1)
    actual.dropna(inplace=True)

    correct_num = sum(np.sign(actual["predicted_diff"]) == np.sign(actual["diff"]))
    print(f"{correct_num} correct directions out of a total: {len(actual)}" )
    

# def main():
#     data = {
#         "Target":[0, 100, 50, 60, 70, 80]
#     }
    
#     actual = pd.DataFrame(data)
#     predictions = [0, 40, 50, 60, 70, 80]
    
#     print(get_num_correct_direction(predictions, actual))



# if __name__ == "__main__":
#     main()