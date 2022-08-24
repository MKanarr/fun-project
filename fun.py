from concurrent.futures import process
from math import prod
import requests
from bs4 import BeautifulSoup

LEGO_STAR_WARS_URL = "https://www.lego.com/en-us/themes/star-wars?page="
HTML_PRODUCT_CLASS = "ProductGridstyles__Item-lc2zkx-1"
HTML_SETNAME_CLASS = "Markup__StyledMarkup-ar1l9g-0"
HTML_IMAGE_CLASS = "Imagestyles__Img-m2o9tb-0"

i = 1


while True:
    req = requests.get(LEGO_STAR_WARS_URL + str(i))
    soup = BeautifulSoup(req.content, 'html.parser')

    products = soup.find_all('li', class_=HTML_PRODUCT_CLASS)

    if len(products) == 0:
        break

    for prod in products:
        print(prod.find('span', class_=HTML_SETNAME_CLASS).text)
        print(prod.find('img', class_=HTML_IMAGE_CLASS))


    i += 1