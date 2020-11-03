import json
import os
from pathlib import Path
import codecs
from bs4 import BeautifulSoup


path = Path('C:/Users/Tyler/PycharmProjects/RunescapeBots/GE_Prices_Wiki')
ge_price_location = 'div class="GEdataprices"'


def open_file(file_name):
    fd = open(file_name)
    read = fd.read()
    #decoded = read.decode('utf-8')

    #soup = BeautifulSoup(fd, 'html.parser')
    #content = soup.find(ge_price_location)
    print(fd)
    #print(content)
    #print(fd.readlines())


def main():
    for file in os.listdir(path):
        try:
            open_file(path / file)
        except:
            print(f'Could not open {file} file')


if __name__ == '__main__':
    main()