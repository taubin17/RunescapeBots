import requests
from pathlib import Path
from bs4 import BeautifulSoup
import urllib.request
import json
from urllib.request import Request, urlopen
import time
from datetime import datetime
from osrsbox import items_api
import sys
import os
import re

all_db_items = items_api.load()
#all_db_items = [all_db_items[1893], all_db_items[1894]]

GE_prices = Path('C:/Users/Tyler/PycharmProjects/RunescapeBots/GE_prices')
Others = Path('C:/Users/Tyler/PycharmProjects/RunescapeBots/others')


#print(all_db_items[5589])
#fixed_string = re.sub('[\W_]+', '', all_db_items[5589].name)
#print(fixed_string)
#exit()
#print(all_db_items[5589].name.replace('/', '-'))
#exit()
now = datetime.now()

print(now.strftime('%H:%M:%S'))
if __name__ == '__main__':
    for anything in all_db_items:
        anything.name.replace('/', '-')
    for item in all_db_items:
        try:
            if item.tradeable_on_ge == True:
                Id = item.id
                item_lookup = r'https://secure.runescape.com/m=itemdb_oldschool/api/graph/' + str(Id) + '.json'
                response = requests.get(item_lookup)
                json_data = response.json()

                #Clean up item name for filename set
                fixed_string = re.sub('[\W_]+', '', all_db_items[5589].name)
                filename = fixed_string + '.txt'
                file_to_open = GE_prices / filename
                fd = open(file_to_open, 'w')
                fd.write(item.name + ', ' + str(item.highalch) + '\n')
                # fd.close()
                for time, price in json_data['daily'].items():
                    # Convert the time from miloseconds since epoch to seconds
                    time = int(time) / 1000
                    # Then convert epoch time to date time
                    date = datetime.fromtimestamp(time).strftime('%Y-%m-%d')
                    fd.write(str(date) + ', ')
                    fd.write(str(price) + '\n')
                fd.close()
                response.close()
                print('Item: ' + item.name + ' added.', item.id)
                #print (json_data)
            else:
                fixed_string = re.sub('[\W_]+', '', all_db_items[5589].name)
                filename = fixed_string + '.txt'
                file_to_open = Others / filename
                fd = open(file_to_open, 'w')
                fd.write(item.name + ', ' + str(item.highalch) + '\n')
                fd.write('Item not tradeable\n')
                print('Not tradeable item: ', item.name, item.id)
        except:
            fixed_string = re.sub('[\W_]+', '', all_db_items[5589].name)
            filename = fixed_string + '.txt'
            file_to_open = Others / filename
            fd = open(file_to_open, 'w')
            fd.write(item.name + ', ' + str(item.highalch) + '\n')
            fd.write('No grand exchange page\n')
            fd.close()
            print('Item: ', item.name,  'does not have associative GE price page', item.id)
exit()

