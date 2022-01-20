import requests
from bs4 import BeautifulSoup


class Parser:
    def __init__(self, site):
        self.site = site

    def get_url(self):
        r = requests.get(self.site)
        html = r.text
        parse = "html.parser"
        soup = BeautifulSoup(html, parse)
        for tag in soup.find_all("a"):
            url = tag.get("href")
            if url and "html" in url:
                print("\n" + url)


news = "https://www.zakon.kz/"
Parser(news).get_url()
