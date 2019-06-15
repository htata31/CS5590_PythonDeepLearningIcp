import requests
from bs4 import BeautifulSoup


def get_href():
    # Set the URL you want to webscrape from
    url = "https://en.wikipedia.org/wiki/Deep_learning"
    # Connect to the URL
    response = requests.get(url)
    # Parse HTML and save to BeautifulSoup object¶
    soup = BeautifulSoup(response.text, 'html.parser')
    # Iterate through all the tags and get the links
    links = [a.get('href') for a in soup.find_all('a', href=True)]
    write(links)
    # print(len(links))


def write(links):
    # Writing into a text file
    with open('links.txt', 'w') as f:
        for item in links:
            f.write("%s\n" % item)


if __name__ == '__main__':
    get_href()

