#
# Name: Czech News Highlights
# Author: Vít Černý
# License: GPL v3
#
import requests
from bs4 import BeautifulSoup as bs
import codecs

SEZNAM_ZPRAVY_URL = "https://www.seznamzpravy.cz/" # first h3 element
IROZHLAS_URL = "https://www.irozhlas.cz/"
NOVINKY_URL = "https://www.novinky.cz/"
DENIKN_URL = "https://denikn.cz/"

def get_page(url):
    s = requests.Session()
    site = s.get(url)
    site = site.content.decode('utf-8')
    soup = bs(site, 'html.parser')
    #soup = bs(s.get(url).text, 'html.parser')
    return soup

def seznam_zpravy():
    soup = get_page(SEZNAM_ZPRAVY_URL)
    info = soup.find("h3")
    return info.string

def irozhlas():
    soup = get_page(IROZHLAS_URL)
    info = soup.find(class_="b-article__link")
    return info.string.strip()

def novinky():
    soup = get_page(NOVINKY_URL)
    info = soup.find(class_="d_r d_u f_a2")
    return info.string

def denikn():
    soup = get_page(DENIKN_URL)
    info = soup.find("h3")
    info = info.contents[0]
    return info.string

def main():
    print("Seznam Zprávy: ", seznam_zpravy())
    print("iRozhlas: ", irozhlas())
    print("Novinky: ", novinky())
    print("Deník N:", denikn())

if __name__ == "__main__":
    main()
