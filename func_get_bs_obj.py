from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_bs_obj(url):
    html = urlopen(url)
    bs_obj = BeautifulSoup(html.read(), "html.parser")
    return bs_obj
