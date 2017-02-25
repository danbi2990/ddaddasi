from dda_publisher import Publisher

"""
헤럴드경제
url:
http://biz.heraldcorp.com/search/?q={}&dt=1&nt=1&np=1&hq=
"""


class Herald(Publisher):
    def __init__(self):
        super().__init__("헤럴드경제", "http://biz.heraldcorp.com/search/?q={}&dt=1&nt=1&np=1&hq=")

    def navigate_article(self, bs_obj):
        try:
            # print(bs_obj)
            tags = bs_obj.find_all("p",{"class":"ntitle"})
            # print(tags)
            for p_tag in tags:
                tag = p_tag.a
                # print(tag)
                try:
                    self.articles.append({"title": tag.get_text().strip(), "publisher": self.name, "url": tag['href']})
                except AttributeError:
                    pass
        except AttributeError:
            pass


# k = Herald()
# k.set_keyword('김정남')
# k.run()
# print(k.articles)
