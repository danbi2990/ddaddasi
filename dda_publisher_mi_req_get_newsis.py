from dda_publisher import Publisher

"""
뉴시스
url:
http://www.newsis.com/search/schlist?val={}&sort=acc&jo=all_jogun&bun=all_bun&sdate=&term=allday&edate=&s_yn=Y&catg=1&t=1&page=1&
한국경제, 서울경제, 매일경제, 헤럴드경제
"""


class NewSis(Publisher):
    def __init__(self):
        super().__init__("뉴시스", "http://www.newsis.com/search/schlist?val={}&sort=acc&jo=all_jogun&bun=all_bun&sdate=&term=allday&edate=&s_yn=Y&catg=1&t=1&page=1&")

    def navigate_article(self, bs_obj):
        try:
            # print(bs_obj)
            tags = bs_obj.find("div", {"class":"lst_p12 mgt30"}).find_all("strong",{"class":"title"})
            # print(tags)
            for strong_tag in tags:
                tag = strong_tag.a
                try:
                    self.articles.append({"title": tag.get_text(), "publisher": self.name, "url": "http://www.newsis.com"+tag['href']})

                except (AttributeError, KeyError):
                    pass
        except (AttributeError, KeyError):
            pass


# k = NewSis()
# k.set_keyword('김정남')
# k.run()
# print(k.articles)
