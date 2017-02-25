from dda_publisher import Publisher

"""
조선
url:
http://search.chosun.com/search/news.search?query={}&pageno=0&orderby=&naviarraystr=&kind=&cont1=&cont2=&cont5=&categoryname=&categoryd2=&c_scope=news&sdate=&edate=&premium=
"""


class ChoSun(Publisher):
    def __init__(self):
        super().__init__("조선일보", "http://search.chosun.com/search/news.search?query={}&pageno=0&orderby=&naviarraystr=&kind=&cont1=&cont2=&cont5=&categoryname=&categoryd2=&c_scope=news&sdate=&edate=&premium=")

    def navigate_article(self, bs_obj):
        try:
            tags = bs_obj.find("div", {"class":"result_box"}).find_all("dt")

            for tag in tags:
                try:
                    a_tag = tag.find("a")
                    self.articles.append({"title": a_tag.get_text(), "publisher": self.name, "url": a_tag['href']})
                except AttributeError:
                    pass
        except AttributeError:
            pass


# k = ChoSun()
# k.set_keyword('김정남')
# k.run()
# print(k.articles)
