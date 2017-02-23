from selenium import webdriver
from dda_publisher import Publisher
from bs4 import BeautifulSoup as bs
from urllib.parse import quote
import time

"""
국민일보
url:
http://www.kmib.co.kr/search/result.asp?q={}
서울신문, 문화일보, 세계일보, 연합뉴스,
뉴스원, 뉴시스, 한국경제, 서울경제, 매일경제, 헤럴드경제
"""


class KookMin(Publisher):
    def __init__(self, driver):
        super().__init__("국민일보", "http://www.kmib.co.kr/search/result.asp?q={}")
        self.driver = driver

    def run(self):
        # driver = webdriver.PhantomJS('./phantomjs/bin/phantomjs')
        base = "http://www.kmib.co.kr/search/result.asp?q={}"
        # keyword = "김정남"
        query = base.format(quote(self.keyword.encode('euc-kr')))
        self.driver.get(query)

        time.sleep(1)

        html = self.driver.page_source
        bs_obj = bs(html, 'html.parser')

        return self.navigate_article(bs_obj)

    def navigate_article(self, bs_obj):
        try:
            tags = bs_obj.find_all("a", {"class":"gs-title"})

            for idx, tag in enumerate(tags):
                if idx % 2 == 1:
                    try:
                        # print(tag)
                        self.articles.append({"title": tag.get_text(), "publisher": self.name, "url": tag['href']})
                    except (AttributeError, KeyError):
                        pass
        except (AttributeError, IndexError):
            pass



# k = KookMin()
# k.set_keyword("황교안")
# k.run()
# print(k.articles)
