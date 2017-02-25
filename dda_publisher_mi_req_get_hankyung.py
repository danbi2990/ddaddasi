from dda_publisher import Publisher

"""
한국경제
url:
http://search.hankyung.com/apps.frm/search.news?query={}
서울경제, 매일경제, 헤럴드경제
"""


class HanKyung(Publisher):
    def __init__(self):
        super().__init__("한국경제", "http://search.hankyung.com/apps.frm/search.news?query={}")

    def navigate_article(self, bs_obj):
        try:
            # print(bs_obj)
            tags = bs_obj.find("div", {"class":"section hk_news"}).find_all("em",{"class":"tit"})
            # print(tags)
            for em_tag in tags:
                tag = em_tag.parent
                # print(tag)
                try:
                    self.articles.append({"title": tag.get_text().strip(), "publisher": self.name, "url": tag['href']})
                except AttributeError:
                    pass
        except AttributeError:
            pass


# k = HanKyung()
# k.set_keyword('김정남')
# k.run()
# print(k.articles)
