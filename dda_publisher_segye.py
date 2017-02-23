from dda_publisher import Publisher
from urllib.parse import quote
import requests
from bs4 import BeautifulSoup as bs

"""
세계일보
url:
http://search3.segye.com/index.jsp
연합뉴스,
뉴스원, 뉴시스, 한국경제, 서울경제, 매일경제, 헤럴드경제
"""


class SeGye(Publisher):
    def __init__(self):
        super().__init__("세계일보", "http://search3.segye.com/index.jsp")

    def set_keyword(self, keyword):
        self.keyword = keyword

    def run(self):
        key = quote(self.keyword)
        # query = self.base_url.format(key)
        query = self.base_url
        r = requests.post(query, data={"search_ContType": "article", "searchWord": key})
        bs_obj = bs(r.text, "html.parser")
        return self.navigate_article(bs_obj)

    def navigate_article(self, bs_obj):
        try:
            print(bs_obj)
            tags = bs_obj.find("div", {"class":"articleArea"}).find_all("dt")

            for dt_tag in tags:
                tag = dt_tag.a
                try:
                    self.articles.append({"title": tag.get_text(), "publisher": self.name, "url": tag['href']})
                except AttributeError:
                    pass
        except AttributeError:
            pass

#
# m = SeGye()
# m.set_keyword("김정남")
# m.run()
# print(m.articles)
