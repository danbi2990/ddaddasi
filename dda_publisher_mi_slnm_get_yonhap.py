from dda_publisher import Publisher
from selenium import webdriver

"""
연합뉴스
url:
http://www.yonhapnews.co.kr/home09/7091000000.html?query={}
"""


class YonHap(Publisher):
    def __init__(self):
        super().__init__("연합뉴스", "http://www.yonhapnews.co.kr/home09/7091000000.html?query={}", is_selenium=True)

    def navigate_article(self, bs_obj):
        try:
            # print(bs_obj)
            tags = bs_obj.find("div", {"class":"cts_atclst"}).find_all("a")
            for tag in tags:
                try:
                    self.articles.append({"title": tag.find("span",{"class":"tt2"}).get_text(), "publisher": self.name, "url": tag['href']})
                except (AttributeError, KeyError):
                    pass
            # print(self.name)
        except (AttributeError, KeyError):
            pass


# web_driver = webdriver.PhantomJS('./phantomjs/bin/phantomjs')
# y = YonHap(web_driver)
# y.set_keyword("김정남")
# y.run()
# print(y.articles)
# web_driver.quit()
