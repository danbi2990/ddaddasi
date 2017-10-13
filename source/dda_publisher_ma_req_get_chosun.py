from source.dda_publisher import Publisher

"""
조선
url:
http://search.chosun.com/search/news.search?query={}&pageno=0&orderby=&naviarraystr=&kind=&cont1=&cont2=&cont5=&categoryname=&categoryd2=&c_scope=news&sdate=&edate=&premium=
http://search.chosun.com/search/news.search?query={}&pageno=0&orderby=&naviarraystr=&kind=&cont1=&cont2=&cont5=&categoryname=&categoryd2=&c_scope=news&sdate=&edate=&premium=
http://search.chosun.com/search/news.search?query={}&pageno=0&orderby=news&naviarraystr=&kind=&cont1=&cont2=&cont5=&categoryname=%EC%A1%B0%EC%84%A0%EC%9D%BC%EB%B3%B4&categoryd2=&c_scope=navi&sdate=&edate=&premium=#;
"""


class ChoSun(Publisher):
    def __init__(self):
        super().__init__("조선일보", "http://search.chosun.com/search/news.search?query={}&pageno=0&orderby=news&naviarraystr=&kind=&cont1=&cont2=&cont5=&categoryname=%EC%A1%B0%EC%84%A0%EC%9D%BC%EB%B3%B4&categoryd2=&c_scope=navi&sdate=&edate=&premium=#;")

    def navigate_article(self, bs_obj):
        try:
            tags = bs_obj.find("div", {"class":"search_news_box"}).find_all("dt")

            for tag in tags:
                try:
                    a_tag = tag.find("a")
                    self.articles.append({"title": a_tag.get_text(), "publisher": self.name, "url": a_tag['href']})
                except (AttributeError, KeyError):
                    pass
        except (AttributeError, KeyError):
            pass


if __name__ == "__main__":
    k = ChoSun()
    k.set_keyword('이재용')
    k.run()
    print(k.articles)
