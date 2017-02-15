from urllib.request import urlopen
from bs4 import BeautifulSoup
from google import search

class article_factory:
    def __init__(self):
        self.articles
        self.html = urlopen(url)
        self.bsObj = BeautifulSoup(self.html.read(), "html.parser")
        self.title = self.bsObj.find()

class article:
    """abstract article class"""
    def __init__(self, publisher, url, html_selector):
        self.publisher = publisher
        self.url = url
        self.html_selector = html_selector
        self.title

class chosun_article(article):
    def __init__(self, publisher, url, html_selector):
        super(chosun_article, self).__init__(publisher, url, html_selector)
