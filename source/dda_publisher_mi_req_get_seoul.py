from source.dda_publisher import Publisher

"""
서울신문
url:
http://search.seoul.co.kr/index.php?keyword={}
문화일보, 세계일보, 연합뉴스,
뉴스원, 뉴시스, 한국경제, 서울경제, 매일경제, 헤럴드경제
"""


class Seoul(Publisher):
    def __init__(self):
        super().__init__("서울신문", "http://search.seoul.co.kr/index.php?keyword={}")

    def navigate_article(self, bs_obj):
        try:
            tags = bs_obj.find("div", {"id":"list_area"}).find_all("dt")
            for dt_tag in tags:
                tag = dt_tag.find("a")
                try:
                    self.articles.append({"title": tag.get_text(), "publisher": self.name, "url": tag['href']})
                except (AttributeError, KeyError):
                    pass
        except (AttributeError, KeyError):
            pass


# s = Seoul()
# s.set_keyword("김정남")
# s.run()
# print(s.articles)
