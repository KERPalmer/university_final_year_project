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
def get_num_correct_direction_difference(predictions, observations):
    correct_num = np.sum(np.sign(predictions) == np.sign(observations))

    print(f"{correct_num} correct directions out of a total: {len(predictions)}" )
    return correct_num
    
def get_num_correct_direction_actual(predictions, obs):
    correct_num = 0
    for index in range(1, obs):
        is_actual_increase = obs[index] >= obs[index - 1]
        is_predicted_increase = predictions[index] >= obs[index - 1]

        if is_actual_increase == is_predicted_increase:
            correct_num += 1

    print(f"{correct_num} correct directions out of a total: {len(predictions)}" )
    return correct_num

def get_cumulative_return_difference(predictions, obs): #assume buy when predict increase
    cum_reward = 0
    for index in range(1, obs):
        is_increase = obs[index] >= obs[index - 1]
        is_predicted_increase = predictions[index] >= obs[index - 1]

        if is_actual_increase == is_predicted_increase:
            cum_reward += obs

    print(f"{correct_num} correct directions out of a total: {len(predictions)}" )
    return correct_num 


    
# def main():
#     data = {
#         "Target":[0, 100, 50, 60, 70, 80]
#     }
    
#     actual = pd.DataFrame(data)
#     predictions = [0, 40, 50, 60, 70, 80]
    
#     print(get_num_correct_direction(predictions, actual))



# if __name__ == "__main__":
#     main()