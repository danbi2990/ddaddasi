from dda_publisher import Publisher

"""
서울경제
url:
http://www.sedaily.com/Search/?Page=1&scDetail=&scOrdBy=0&catView=AL&scText={}&scPeriod=6m&scArea=tc&scTextIn=&scTextExt=&scPeriodS=&scPeriodE=
매일경제, 헤럴드경제
"""


class SeoKyung(Publisher):
    def __init__(self):
        super().__init__("서울경제", "http://www.sedaily.com/Search/?Page=1&scDetail=&scOrdBy=0&catView=AL&scText={}&scPeriod=6m&scArea=tc&scTextIn=&scTextExt=&scPeriodS=&scPeriodE=")

    def navigate_article(self, bs_obj):
        try:
            print(bs_obj)
            tags = bs_obj.find("div", {"class":"search_result"}).find_all("dt")
            # print(tags)
            for dt_tag in tags:
                tag = dt_tag.parent
                # print(tag)
                try:
                    self.articles.append({"title": tag.get_text().strip(), "publisher": self.name, "url": tag['href']})
                except AttributeError:
                    pass
        except AttributeError:
            pass


# k = SeoKyung()
# k.set_keyword('김정남')
# k.run()
# print(k.articles)
