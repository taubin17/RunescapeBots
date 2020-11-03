import requests
from pathlib import Path
from osrsbox import items_api
from bs4 import BeautifulSoup
import time
import os
import re
from datetime import datetime


GE_prices = Path('C:/Users/Tyler/PycharmProjects/RunescapeBots/GE_prices')
bad_items = []

def open_page(url):
    # Send request to wike specified in URL
    response = requests.get(url)

    # Create soup object for parsing response, and find our desired table data
    soup = BeautifulSoup(response.content, 'html.parser')
    tables = (soup.find('table', attrs={'class': 'plainlinks rsw-infobox infobox no-parenthesis-style infobox-item', }))

    # Close our response, no more to be done
    response.close()
        #print(tables)
    try:
        divs = soup.find('div', {'class':'GEdataprices'})
        # print(divs)
        data = get_price(divs)

        # Set our file destination to a GE_price directory
        dest = get_item(divs) + '.txt'

        # Simply combine predetermined path with item name to create CSV data file
        handle = GE_prices / dest

        # Open our newly assigned file, and give a heading
        fd = open(handle, 'w')
        fd.write('Date/Time,GE_Price,VolumeSold,HighAlc,Limit\n')

        # Create the body of item CSV
        for x in range(len(data)):
            fd.write(data[x][0] + ',' + data[x][1] + ',' + data[x][2] + ',' + str(get_highalc_value(divs)) + ',' + get_limit(divs) + '\n')

    except:
        print(f'{url} failed to load')

def get_price(divs):
    # Pull price data from soup, and parse
    price_history = (divs.get('data-data')).split('|')

    # Now that we parsed our | as newlines, parse colons as commas
    for x in range(len(price_history)):
        price_history[x] = price_history[x].split(':')

    #An empty list to later hold our newly formatted data
    price_data = []

    # For each line in our content, reformat the data to be convenient for use
    for each in price_history:
        # Convert the time from miloseconds since epoch to seconds
        time = int(each[0])
        # Then convert epoch time to date time
        date = datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')


        price = str(each[1])

        try:
            volume = str(each[2])
        except:
            volume = ''

        price_data.append([date, price, volume])
    return price_data



def get_item(divs):
    return divs.get('data-item')


def get_limit(divs):
    return divs.get('data-limit')


def get_highalc_value(divs):
    value = divs.get('data-value')
    high_alc = int(value) * 0.6
    return high_alc


def main():
    x = 0

    url_file = 'urls.txt'

    num_lines = sum(1 for line in open(url_file))
    for file in open(url_file).readlines():
        t = time.perf_counter()
        file = re.sub('[\\n\t ]', '', file)
        # print(file, ' a')
        open_page(file)
        t = time.perf_counter() - t
        # print(f'{file} took approximately {t} seconds to add to Database, {x}/{num_lines} items complete')
        x += 1
        print(str(x) + '/' + str(num_lines))


if __name__ == '__main__':
    t = time.perf_counter()
    main()
    t = time.perf_counter() - t
    print(f'One wiki scrape took {int(t / 60)} minutes and {t % 60} seconds')