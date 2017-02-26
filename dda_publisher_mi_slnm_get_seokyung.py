from selenium import webdriver
from dda_publisher import Publisher

"""
서울경제
url:
http://www.sedaily.com/Search/?Page=1&scDetail=&scOrdBy=0&catView=AL&scText={}&scPeriod=6m&scArea=tc&scTextIn=&scTextExt=&scPeriodS=&scPeriodE=
"""


class SeoKyung(Publisher):
    def __init__(self, web_driver):
        super().__init__("서울경제", "http://www.sedaily.com/Search/?Page=1&scDetail=&scOrdBy=0&catView=AL&scText={}&scPeriod=6m&scArea=tc&scTextIn=&scTextExt=&scPeriodS=&scPeriodE=", is_selenium=True, web_driver=web_driver)

    def navigate_article(self, bs_obj):
        try:
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
        except (AttributeError, KeyError):
            pass

# web_driver = webdriver.PhantomJS('./phantomjs/bin/phantomjs')
# k = SeoKyung(web_driver)
# k.set_keyword('김정남')
# k.run()
# print(k.articles)
# web_driver.quit()
