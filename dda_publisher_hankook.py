from selenium import webdriver
from dda_publisher import Publisher
from urllib.parse import quote
from bs4 import BeautifulSoup as bs
import time


"""
동아
url:
http://hankookilbo.com/fd.aspx?q={}
서울신문, 국민일보, 문화일보, 세계일보, 연합뉴스,
뉴스원, 뉴시스, 한국경제, 서울경제, 매일경제, 헤럴드경제
"""


class HanKook(Publisher):
    def __init__(self, driver):
        super().__init__("한국일보", "http://hankookilbo.com/fd.aspx?q={}")
        self.driver = driver

    def run(self):
        stime = time.time()
        # driver = webdriver.PhantomJS('./phantomjs/bin/phantomjs')
        base = "http://hankookilbo.com/fd.aspx?q={}"
        # keyword = "김정남"
        query = base.format(quote(self.keyword))

        self.driver.get(query)

        html = self.driver.page_source
        bs_obj = bs(html, 'html.parser')
        etime = time.time()
        print(etime - stime)

        return self.navigate_article(bs_obj)

    def navigate_article(self, bs_obj):
        try:
            tags = bs_obj.find_all("a", {"class": "gs-title"})
            for idx, tag in enumerate(tags):
                if idx % 2 == 1:
                    try:
                        # print(tag)
                        self.articles.append({"title": tag.get_text().replace("한국일보 : ", ""), "publisher": self.name,
                                              "url": tag['href']})
                    except (AttributeError, KeyError):
                        pass
        except AttributeError:
            pass


# h = HanKook()
# re = h.search_article("김정남")
# print(re)
