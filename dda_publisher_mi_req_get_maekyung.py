from dda_publisher import Publisher

"""
매일경제
url:
http://find.mk.co.kr/new/search.php?pageNum=1&cat=&cat1=&media_eco=&pageSize=20&sub=news&dispFlag=OFF&page=news&s_kwd={0}&s_page=total&go_page=page&ord=1&ord1=1&ord2=0&s_keyword={0}&y1=1991&m1=01&d1=01&y2=2017&m2=02&d2=24&area=ttbd

헤럴드경제
"""


class MaeKyung(Publisher):
    def __init__(self):
        super().__init__("매일경제", "http://find.mk.co.kr/new/search.php?pageNum=1&cat=&cat1=&media_eco=&pageSize=20&sub=news&dispFlag=OFF&page=news&s_kwd={0}&s_page=total&go_page=page&ord=1&ord1=1&ord2=0&s_keyword={0}&y1=1991&m1=01&d1=01&y2=2017&m2=02&d2=24&area=ttbd", encoding="euc-kr")

    def navigate_article(self, bs_obj):
        try:
            # print(bs_obj)
            tags = bs_obj.find_all("span",{"class":"art_tit"})
            # print(tags)
            for span_tag in tags:
                tag = span_tag.a
                # print(tag)
                try:
                    self.articles.append({"title": tag.get_text().strip(), "publisher": self.name, "url": tag['href']})
                except AttributeError:
                    pass
        except AttributeError:
            pass


# k = MaeKyung()
# k.set_keyword('김정남')
# k.run()
# print(k.articles)
