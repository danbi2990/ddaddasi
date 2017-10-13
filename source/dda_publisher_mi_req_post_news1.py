from source.dda_publisher import Publisher

"""
뉴스1
url:
http://news1.kr/search_front/search.php
"""


class NewsOne(Publisher):
    def __init__(self):
        super().__init__("뉴스1", "http://news1.kr/search_front/search.php", method="post")

    def set_post_data(self):
        # print(self.keyword)
        self.post_data = {
            "mode": "basic",
            "sort": "DATE",
            "query": self.keyword
        }

    def navigate_article(self, bs_obj):
        try:
            # print(bs_obj)
            tags = bs_obj.find("div", {"class":"listType1"}).find_all("dt")

            for dt_tag in tags:
                tag = dt_tag.a
                try:
                    self.articles.append({"title": tag.get_text(), "publisher": self.name, "url": tag['href']})
                except (AttributeError, KeyError):
                    pass
        except (AttributeError, KeyError):
            pass


# m = NewsOne()
# m.set_keyword("김정남")
# m.run()
# print(m.articles)
