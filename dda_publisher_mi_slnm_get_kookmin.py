from selenium import webdriver
from dda_publisher import Publisher
# from seleniumrequests import PhantomJS
import time

"""
국민일보
url:
http://www.kmib.co.kr/search/result.asp?q={}
서울신문, 문화일보, 세계일보, 연합뉴스,
뉴스원, 뉴시스, 한국경제, 서울경제, 매일경제, 헤럴드경제
"""


class KookMin(Publisher):
    def __init__(self, web_driver):
        super().__init__("국민일보", "http://www.kmib.co.kr/search/result.asp?q={}", encoding="euc-kr", is_selenium=True, web_driver=web_driver)

    def navigate_article(self, bs_obj):
        try:
            # print(bs_obj)
            tags = bs_obj.find_all("a", {"class":"gs-title"})
            for idx, tag in enumerate(tags):
                if idx % 2 == 1:
                    try:
                        # print(tag)
                        self.articles.append({"title": tag.get_text().replace("-국민일보", ""), "publisher": self.name, "url": tag['href']})
                    except (AttributeError, KeyError):
                        pass
        except (AttributeError, IndexError):
            pass


# web_driver = webdriver.PhantomJS('./phantomjs/bin/phantomjs')
# h = KookMin(web_driver)
# h.set_keyword("김정남")
# h.run()
# print(h.articles)
# web_driver.quit()
