from source.dda_publisher import Publisher

"""
한겨레
url: http://search.hani.co.kr/Search?command=query&keyword={}sort=d&period=all&media=news
"""


class Hani(Publisher):
    def __init__(self):
        super().__init__("한겨레", "http://search.hani.co.kr/Search?command=query&keyword={}&sort=d&period=all&media=news")

    def navigate_article(self, bs_obj):
        try:
            tags = bs_obj.find("ul", {"class":"search-result-list"}).find_all("dt")
            for tag in tags:
                try:
                    a_tag = tag.find("a")
                    self.articles.append({"title": a_tag.get_text(), "publisher": self.name, "url": a_tag['href']})
                except (AttributeError, KeyError):
                    pass
        except (AttributeError, KeyError):
            pass


