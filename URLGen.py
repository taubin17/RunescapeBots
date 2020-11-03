from osrsbox import items_api
import os
from pathlib import Path
import re


database = items_api.load()


fd = open('urls.txt', 'w')


bad_items = ['Myre snelm', 'Priest gown', "Blood'n'tar snelm"]

snelm_toggle = False
bad_item = False


if __name__ == '__main__':
    for item in database:
        if item.tradeable_on_ge == True:
            url = item.wiki_url
            fd.write(url + '\n')

    fd.close()
    exit()
