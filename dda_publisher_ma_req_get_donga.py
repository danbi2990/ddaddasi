from dda_publisher import Publisher

"""
동아
url:
http://news.donga.com/search?query={}&check_news=1%7C2%7C3%7C4%7C5
"""


class DongA(Publisher):
    def __init__(self):
        super().__init__("동아일보", "http://news.donga.com/search?query={}&check_news=1%7C2%7C3%7C4%7C5")

    def navigate_article(self, bs_obj):
        try:
            h2 = bs_obj.find_all("h2")
            h2 = [x for x in h2 if x.get_text().find("웹동아일보")!=-1][0]
            tags = h2.parent.find_all("p", {"class":"tit"})

            for tag in tags:
                try:
                    a_tag = tag.find("a")
                    self.articles.append({"title": a_tag.get_text(), "publisher": self.name, "url": a_tag['href']})
                except (AttributeError, KeyError):
                    pass
        except (AttributeError, IndexError):
            pass


# k = DongA()
# k.set_keyword('김정남')
# k.run()
# print(k.articles)
