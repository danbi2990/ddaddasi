from iface_publisher import publisher
from imple_self_article import article
from urllib.parse import quote
from func_get_bs_obj import get_bs_obj

"""
경향신문
url: http://search.khan.co.kr/search.html?stb=khan&q=%EC%A0%84%EC%95%88%EB%B2%95
method: get




"""

class khan(publisher):
    def __init__(self):
        super(khan, self).__init__("경향신문", "http://search.khan.co.kr/search.html?stb=khan&q=")

    def search_keyword(self, keyword):
        query = self.create_query(keyword)
        bs_obj = get_bs_obj(query)
        return self.find_article(bs_obj)

    def create_query(self, keyword):
        return self.base_url + quote(keyword)

    def find_article(self, bs_obj):
        res = []
        tags = bs_obj.find("div", {"class":"news section"}).find_all("a")
        for tag in tags:
            res.append(article(tag.get_text(), self.name, tag['href']))

        return res
