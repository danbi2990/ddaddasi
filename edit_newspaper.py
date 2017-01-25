

from urllib.request import urlopen
from bs4 import BeautifulSoup
from google import search
import requests

"""
variable: search keyword, stop number, article list(checkbox)
title tag:
hani: <h4>
chosun: <h1>
dongA: <h1>
joongang: <h1>
khan: <h1>
"""

major = {'hani.co.kr':'한겨레', 'news.chosun.com':'조선일보', 'khan.co.kr':'경향신문', 'joongang.joins.com':'중앙일보', 'donga.com':'동아일보'}


def get_title(site, url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html.read(), "html.parser")
    # print(url)
    if site == 'donga.com':
        return bsObj.find("div", {"class":"article_title02"}).h1.get_text()
    elif site == 'hani.co.kr':
        return bsObj.find("div", {"class":"article-head"}).find("span", {"class":"title"}).get_text()
    elif site == 'news.chosun.com':
        return bsObj.find("h1", {"id":"news_title_text_id"}).get_text()
    elif site == 'khan.co.kr':
        return bsObj.find("h1", {"id":"article_title"}).get_text()
    elif site == 'joongang.joins.com':
        return bsObj.find("h1", {"id": "article_title"}).get_text()
    return ""


# 전안법, 재러드 쿠슈너
# for url in search('Mariposa botnet', tld='es', lang='es', stop=20):
def get_articles(keyword, stop=50):
    articles = []
    # print(keyword)
    for url in search(keyword, stop=stop):
        for site in major:
            # print(site)
            if str(url).find(site) != -1:
                try:
                    title = get_title(site, url)
                except AttributeError as e:
                    print(e)
                    continue
                articles.append((url, title, major[site]))
                # print(url + ": " + title + ", " + major[site])
    return articles

# get_articles('전안법')
