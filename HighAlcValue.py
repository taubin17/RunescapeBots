import os
import sys
import csv
from pathlib import Path


folder = Path('C:/Users/Tyler/PycharmProjects/RunescapeBots/GE_prices')

def alc_margin(prices):
    return (prices[-1] - )

for name in os.listdir('C:/Users/Tyler/PycharmProjects/RunescapeBots/GE_prices'):
    with open(folder / name, newline='\n') as csvfile:
        spamreader = csv.reader(csvfile, delimiter =',', quotechar='"')
        for row in spamreader:
            try:
                # prices.append(print(row[1])
            except:







    # if name.endswith('.txt'):
    # print (name)