

# from urllib.parse import quote
from imple_publisher_khan import khan

def get_articles(keyword):
    res = []
    publishers = [khan()]
    for p in publishers:
        res += p.search_keyword(keyword)
    return res

# 특검
articles = get_articles("특검")
for a in articles:
    print(a.title, a.published_by, a.url, sep=', ')

