from selenium import webdriver
from dda_publisher import Publisher
import time

"""
한국일보
url:
http://hankookilbo.com/fd.aspx?q={}
"""


class HanKook(Publisher):
    def __init__(self):
        super().__init__("한국일보", "http://hankookilbo.com/fd.aspx?q={}", is_selenium=True)

    def navigate_article(self, bs_obj):
        try:
            tags = bs_obj.find_all("a", {"class": "gs-title"})
            for idx, tag in enumerate(tags):
                if idx % 2 == 1:
                    try:
                        # print(tag)
                        self.articles.append({"title": tag.get_text().replace("한국일보 : ", ""), "publisher": self.name, "url": tag['href']})
                    except (AttributeError, KeyError):
                        pass
            # print(self.name)
        except (AttributeError, KeyError):
            pass


# web_driver = webdriver.PhantomJS('./phantomjs/bin/phantomjs')
# h = HanKook()
# h.set_web_driver(web_driver)
# h.set_keyword("김정남")
# h.run()
# print(h.articles)
# web_driver.quit()
