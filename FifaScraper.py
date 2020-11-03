import requests
from bs4 import BeautifulSoup

def main():

    url = r'https://www.futbin.com/20/player/44119/cristiano-ronaldo'

    response = requests.get(url)
    #data = response.json()
    #print(data)

    fd = open('Ronaldo.txt', 'w')

    #print(response.content)

    soup = BeautifulSoup(response.content, 'html.parser')

    divs = soup.find_all('div')
    print(divs)

    #print(soup)
    for tag in soup.find_all('p'):
        if tag.get('id'):
            print(tag)
    string = str(soup.decode('utf-8'))

    #fd.write(string)
    #print(response.text)


if __name__ == '__main__':
    main()