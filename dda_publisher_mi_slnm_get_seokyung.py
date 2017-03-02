from selenium import webdriver
from dda_publisher import Publisher

"""
서울경제
url:
http://www.sedaily.com/Search/?Page=1&scDetail=&scOrdBy=0&catView=AL&scText={}&scPeriod=6m&scArea=tc&scTextIn=&scTextExt=&scPeriodS=&scPeriodE=
"""


class SeoKyung(Publisher):
    def __init__(self):
        super().__init__("서울경제", "http://www.sedaily.com/Search/?Page=1&scDetail=&scOrdBy=0&catView=AL&scText={}&scPeriod=6m&scArea=tc&scTextIn=&scTextExt=&scPeriodS=&scPeriodE=", is_selenium=True, sleep=1)

    def navigate_article(self, bs_obj):
        try:
            # print(self.name)
            # print(bs_obj)
            tags = bs_obj.find("ul", {"class":"news_list"}).find_all("dt")
            # print(tags)
            for dt_tag in tags:
                tag = dt_tag.a
                # print(tag)
                try:
                    self.articles.append({"title": tag.get_text().strip(), "publisher": self.name, "url": "http://www.sedaily.com" + tag['href']})
                except (AttributeError, KeyError):
                    pass
            # print(self.name)
        except (AttributeError, KeyError):
            # print(self.name)
            pass

# web_driver = webdriver.PhantomJS('./phantomjs/bin/phantomjs')
# k = SeoKyung()
# k.set_web_driver(web_driver)
# k.set_keyword('김정남')
# k.run()
# print(k.articles)
# web_driver.quit()
