from dda_publisher import Publisher

"""
경향신문
url: http://search.khan.co.kr/search.html?stb=khan&q=%EC%A0%84%EC%95%88%EB%B2%95
"""


class Khan(Publisher):
    def __init__(self):
        super().__init__("경향신문", "http://search.khan.co.kr/search.html?stb=khan&q={}")

    def navigate_article(self, bs_obj):
        try:
            tags = bs_obj.find("div", {"class":"news section"}).find_all("a")
            for tag in tags:
                try:
                    self.articles.append({"title": tag.get_text(), "publisher": self.name, "url": tag['href']})
                except AttributeError:
                    pass
        except AttributeError:
            pass


# k = Khan()
# k.set_keyword('김정남')
# k.run()
# print(k.articles)
