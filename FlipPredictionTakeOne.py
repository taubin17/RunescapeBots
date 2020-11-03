from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import os
from pathlib import Path
import pandas as pd
import numpy as np
import csv
import re
import keras
from keras.models import Sequential
from keras.layers import Dense, LSTM
from matplotlib import pyplot as plt
from tensorflow import set_random_seed


GE_prices = Path('C:/Users/Tyler/PycharmProjects/RunescapeBots/GE_prices')
file = r'Rune scimitar.txt'


def read_file(file):
    data = pd.read_csv(file)
    return data


def main():
    data = read_file(GE_prices / file)

    data_list = data.to_string()

    date_time = []
    price = []


    for index, row in data.iterrows():
        date_time.append(row['Date/Time'])
        price.append(row['GE_Price'])
        #print(row['Date/Time'], row['GE_Price'])

    date_time_reshaped = np.array(date_time).reshape(-1, 1)


    date_train, date_test, price_train, price_test = train_test_split(date_time_reshaped, price, test_size=0.2, random_state=0, shuffle=False)







    game_train, game_test, answer_train, answer_test = train_test_split(game_reshape, answers, test_size=0.2, random_state=0, shuffle=False)

    # Create our model, and find the best move using said model
    linear_model, linear_accuracy = linear_regression(game_train, answer_train, game_test, answer_test)
    tree_model, tree_accuracy, tree_model_results = decision_tree_method(game_train, answer_train, game_test, answer_test, 'gini')

    print(f'Accuracy of Linear Model: {linear_accuracy}%. Accuracy of Tree Model: {tree_accuracy}%')

    if linear_accuracy > tree_accuracy:
        print('Model selected: Linear Model')
        best_move = get_best_move(linear_model, len(answers), 1)
    else:
        print('Model Selected: Tree Model')
        best_move = get_best_move(tree_model, len(answers), 1)
        profit = model_reward(tree_model_results, 'Tree (Gini)')

    # End timer now that program has ended
    t = time.perf_counter() - t

    print(f'\nThe winning move is playing {best_move}, and was theorized in {int(round((t / 60), 3))} minutes and {round(t % 60, 4)} seconds')





if __name__ == '__main__':
    main()