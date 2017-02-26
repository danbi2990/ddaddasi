from dda_publisher import Publisher

"""
중앙
url:
http://search.joins.com/news?keyword={}&cloc=joongang|section|subsection
"""


class Joins(Publisher):
    def __init__(self):
        super().__init__("중앙일보", "http://search.joins.com/news?keyword={}&cloc=joongang|section|subsection")

    def navigate_article(self, bs_obj):
        try:
            tags = bs_obj.find("div", {"class":"section_joongang"}).find_all("strong", {"class":"headline"})
            for tag in tags:
                try:
                    a_tag = tag.find("a")
                    self.articles.append({"title": a_tag.get_text(), "publisher": self.name, "url": a_tag['href']})
                except (AttributeError, KeyError):
                    pass
        except (AttributeError, KeyError):
            pass


