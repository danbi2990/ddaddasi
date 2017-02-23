from dda_publisher import Publisher
from urllib.parse import quote
import requests
from bs4 import BeautifulSoup as bs

"""
문화일보
url:
http://search.munhwa.com/munhwa.jsp?searchTerm={}
http://search.munhwa.com/munhwa.jsp?q=
http://search.munhwa.com/main.jsp?q={}
http://search.munhwa.com
http://search.munhwa.com/munhwa.jsp?q=
문화일보, 세계일보, 연합뉴스,
뉴스원, 뉴시스, 한국경제, 서울경제, 매일경제, 헤럴드경제
"""


class MunHwa(Publisher):
    def __init__(self):
        super().__init__("문화일보", "http://search.munhwa.com/munhwa.jsp")

    def set_keyword(self, keyword):
        self.keyword = keyword.encode('euc-kr')

    def run(self):
        key = quote(self.keyword)
        # query = self.base_url.format(key)
        query = self.base_url
        # r = requests.post(query, {"whereAll":"","code":"","startDate":"","endDate":"","orderType":"","protoColStr":"%40where+SRV_TITLE%28HASALL%7C%27%B1%E8%C1%A4%B3%B2%27%7C100%29+or+TXT_NEWS%28HASALL%7C%27%B1%E8%C1%A4%B3%B2%27%7C100%29","allSearchTerm":key,"sel":2,"searchTerm":key})
        r = requests.post(query, param=key, data={"sel": 2, "searchTerm": key})
        bs_obj = bs(r.text, "html.parser")
        return self.navigate_article(bs_obj)


    def navigate_article(self, bs_obj):
        try:
            tags = bs_obj.find_all("td", {"style":"line-height:20px;"})
            remove_opinion = [x.a for x in tags if x.font.get_text().find("오피니언")==-1]
            for tag in remove_opinion:
                try:
                    self.articles.append({"title": tag.get_text(), "publisher": self.name, "url": tag['href']})
                except AttributeError:
                    pass
        except AttributeError:
            pass


# m = MunHwa()
# m.set_keyword("김정남")
# m.run()
# print(m.articles)
