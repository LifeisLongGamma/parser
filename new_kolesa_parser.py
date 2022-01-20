import requests
from bs4 import BeautifulSoup

URL = "https://kolesa.kz/cars/toyota/camry/almaty/"
HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0", "accept": "*/*"}
parser = "html.parser"

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, parser)
    items = soup.find_all("a", class_="a-info-side col-right-list")

    cars = []

    for item in items:
        cars.append({
            "info": item.find("div", class_="a-info-mid").get_text()
        })
    print(cars)

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print("Error")


parse()
