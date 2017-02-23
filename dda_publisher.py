from urllib.parse import quote
from dda_utils import get_bs_obj
import threading


class Publisher(threading.Thread):
    def __init__(self, name, base_url):
        super().__init__()
        self.name = name
        self.base_url = base_url
        self.keyword = None
        self.articles = []

    def set_keyword(self, keyword):
        self.keyword = keyword

    def run(self):
        query = self.base_url.format(quote(self.keyword))
        bs_obj = get_bs_obj(query)
        return self.navigate_article(bs_obj)

    def navigate_article(self, bs_obj):
        pass
