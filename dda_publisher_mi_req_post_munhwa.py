
from dda_publisher import Publisher

"""
문화일보
url:
http://search.munhwa.com/main.jsp?searchTerm={0}&q={0}
"""


class MunHwa(Publisher):
    def __init__(self):
        super().__init__("문화일보", "http://search.munhwa.com/main.jsp?searchTerm={0}&q={0}", encoding="euc-kr", method="post", is_url_variable=True)

    def set_post_data(self):
        self.post_data = {"searchTerm": self.keyword}
        self.cookies = {
            "history_backurl": "http%3A//search.munhwa.com/main.jsp%3FsearchTerm%3D%25B1%25E8%25C1%25A4%25B3%25B2%26q%3D%25B1%25E8%25C1%25A4%25B3%2"
        }

    def navigate_article(self, bs_obj):
        try:
            tags = bs_obj.find_all("td", {"style":"line-height:20px;"})

            remove_opinion = [x.a for x in tags if x.get_text().find("오피니언")==-1]
            for tag in remove_opinion:
                try:
                    self.articles.append({"title": tag.get_text(), "publisher": self.name, "url": tag['href']})
                except (AttributeError, KeyError):
                    pass
        except (AttributeError, KeyError):
            pass


# m = MunHwa()
# m.set_keyword("김정남")
# m.run()
# print(m.articles)


# url = "http://search.munhwa.com/munhwa.jsp?q=%B1%E8%C1%A4%B3%B2"
# print(url)
#
# data = {
#     # "protocolStr": "%40where+SRV_TITLE%28HASALL%7C%27%B1%E8%C1%A4%B3%B2%27%7C100%29+or+TXT_NEWS%28HASALL%7C%27%B1%E8%C1%A4%B3%B2%27%7C100%29",
#     # "sel":2,
#     # "allSearchTerm": "김정남",
#     "searchTerm": "김정남".encode("euc-kr")
# }
#
# cookies = {
# # "__utma":"263674640.2036381237.1429926560.1429926560.1429926560.1", "RB_PCID":"1487760030339883851", "RB_GUID":"7bd4034c-3f6e-4723-a2ba-d128e2b0a6a0", "JSESSIONID":"D028819132422B42F5AC07E389474410",
#     "history_backurl": "http%3A//search.munhwa.com/main.jsp%3FsearchTerm%3D%25B1%25E8%25C1%25A4%25B3%25B2%26q%3D%25B1%25E8%25C1%25A4%25B3%2"
# }
#
# r = requests.post(url, data=data, cookies=cookies)
# print(r.text)
