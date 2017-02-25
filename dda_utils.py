from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote


def get_bs_obj(url, method):
    html = urlopen(url)
    bs_obj = BeautifulSoup(html.read(), "html.parser")
    return bs_obj


def search_definition(keyword):
    res = []
    quoted_keyword = quote(keyword)
    url_naver = "http://terms.naver.com/search.nhn?query={}&searchType=&dicType=&subject=".format(quoted_keyword)
    url_wiki = "https://ko.wikipedia.org/wiki/{}".format(quoted_keyword)
    res.append({"publisher":"네이버 백과사전", "title":"", "url":url_naver})
    res.append({"publisher":"위키백과", "title": "", "url":url_wiki})
    return res


def search_minor(keyword):
    res = []

    res.append({"title": "", "publisher": "한국일보", "url": "http://hankookilbo.com/fd.aspx?q={}".format(quote(keyword))})
    res.append({"title": "", "publisher": "국민일보", "url": "http://www.kmib.co.kr/search/result.asp?q={}".format(quote(keyword.encode('euc-kr')))})
    return res
