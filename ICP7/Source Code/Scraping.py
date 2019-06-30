import requests
from bs4 import BeautifulSoup


def get_href():
    # Set the URL you want to webscrape from
    url = "https://en.wikipedia.org/wiki/Google"
    # Connect to the URL
    response = requests.get(url)
    # Parse HTML and save to BeautifulSoup object¶
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.find('div', {'class': 'mw-parser-output'})

    # Iterate through all the tags and get the links
    write(str(data.text))
    # print(type(data))


def write(data):
    # Writing into a text file
    with open('input.txt', 'w', encoding='utf-8') as f:
            f.write(data)


if __name__ == '__main__':
    get_href()
