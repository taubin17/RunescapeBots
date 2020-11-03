import aiohttp
import asyncio
import time
import json
from pathlib import Path
from bs4 import BeautifulSoup


GE_prices = Path('C:/Users/Tyler/PycharmProjects/RunescapeBots/GE_Prices_Wiki')

async def download_file(url):
    print(f'Started Downloading File {url}')
    async with aiohttp.ClientSession() as session:
        #asyncio.sleep(1)
        #print(session.)
        async with session.get(url) as resp:
            print(resp.status)
            content = await resp.read()
            #soup = BeautifulSoup(content, 'html.parser')
            #tables = (soup.find('table', {'class': 'plainlinks rsw-infobox infobox no-parenthesis-style infobox-item', },{'class=GEdataprices'}))
            #divs = tables.find('div', {'class': 'GEdataprices'})
            #price_data = divs.get('data-data')
            #print(price_data)
            #content = json.dumps(content)
            #print(content)
            print(f'Finished Downloading File {url}')
            return content
async def write_file(n, content):

    #json2 = content.decode('utf-8')
    #json2 = json.dumps(json2)
    #print(content)
    filename = f'async_{n}.html'
    item_price_file = GE_prices / filename
    with open(item_price_file, 'wb') as fd:
        print(f'Started Writing {filename}')
        fd.write(content)
        print(f'Finished Writing {filename}')

async def scrape_task(n, url):
    content = await download_file(url)
    await write_file(n, content)


async def main():
    tasks = []
    for n, url in enumerate(open('urls.txt').readlines()):
        tasks.append(scrape_task(n, url))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    t = time.perf_counter()
    asyncio.run(main())
    t2 = time.perf_counter() - t
    print(f'Total time taken {t2:0.2f} seconds')