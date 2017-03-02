from urllib.parse import quote
import requests
import time
from bs4 import BeautifulSoup
# from selenium import webdriver
import threading


class Publisher(threading.Thread):
    def __init__(self, name, base_url, encoding="utf-8", method="", is_selenium=False, is_url_variable=False, web_driver=None, sleep=0):
        super().__init__()
        self.name = name
        self.base_url = base_url
        self.keyword = None
        self.articles = []

        self.encoding = encoding    # utf-8 or euc-kr

        self.method = method    # get or post
        self.post_data = None   # if method is post
        self.cookies = None     # if cookie is needed
        self.is_url_variable = is_url_variable      # MoonHwa's url is variable although it's post

        self.is_selenium = is_selenium  # phantomJS used?
        self.web_driver = web_driver    # phantom obj
        self.sleep = sleep

    def run(self):
        bs_obj = self.get_bs_obj()
        return self.navigate_article(bs_obj)

    def set_post_data(self):
        pass

    def navigate_article(self, bs_obj):
        pass

    def set_web_driver(self, driver):
        self.web_driver = driver

    def set_keyword(self, keyword):
        if self.encoding != "utf-8":   # euc-kr
            self.keyword = keyword.encode(self.encoding)
        else:   # utf-8
            self.keyword = keyword

    def get_bs_obj(self):
        query = self.base_url.format(quote(self.keyword))

        if not self.is_selenium:    # basic

            if self.method == "post":
                # print(query)
                self.set_post_data()
                r = requests.post(query if self.is_url_variable else self.base_url, data=self.post_data, cookies=self.cookies)
                # r = requests.post(query, data=self.post_data)

            else:   # basic
                # print(query)
                r = requests.get(query)
            # if self.encoding == "euc-kr":
            r.encoding = self.encoding
            html = r.text   # r.content?

        else:   # phantomJS used

            if self.method == "post":
                self.set_post_data()
                r = self.web_driver.request("POST",self.base_url, data=self.post_data)

            else:   # method: get
                # print(query)
                self.web_driver.get(query)
                time.sleep(self.sleep)
            html = self.web_driver.page_source

        bs_obj = BeautifulSoup(html, "html.parser")
        # print(bs_obj)
        return bs_obj
