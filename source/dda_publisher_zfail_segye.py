from source.dda_publisher import Publisher

# from selenium import webdriver

"""
세계일보
url:
http://search3.segye.com/index.jsp
"""


class SeGye(Publisher):
    def __init__(self, web_driver):
        super().__init__("세계일보", "http://search3.segye.com/index.jsp", method="post", is_selenium=True, web_driver=web_driver)

    def set_post_data(self):
        self.post_data = {
            "search_ContType": "article",
            "searchWord": self.keyword,
            "period": "all"
            # "cust_media": "SGN",
            # "sfield": "title_body",
            # "searchWord2": self.keyword
        }

    # def run(self):
    #     key = quote(self.keyword)
    #     # query = self.base_url.format(key)
    #     query = self.base_url
    #     r = requests.post(query, data={"search_ContType": "article", "searchWord": key})
    #     bs_obj = bs(r.text, "html.parser")
    #     return self.navigate_article(bs_obj)

    def navigate_article(self, bs_obj):
        try:
            print(bs_obj)
            tags = bs_obj.find("div", {"class":"articleArea"}).find_all("dt")

            for dt_tag in tags:
                tag = dt_tag.a
                try:
                    self.articles.append({"title": tag.get_text(), "publisher": self.name, "url": tag['href']})
                except (AttributeError, KeyError):
                    pass
        except (AttributeError, KeyError):
            pass


# web_driver = PhantomJS('./phantomjs/bin/phantomjs')
# m = SeGye(web_driver)
# m.set_keyword("김정남")
# m.run()
# print(m.articles)
# web_driver.quit()
