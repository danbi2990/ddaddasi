from dda_publisher_khan import Khan
from dda_publisher_hani import Hani
from dda_publisher_chosun import ChoSun
from dda_publisher_joins import Joins
from dda_publisher_donga import DongA
from dda_publisher_seoul import Seoul

from dda_publisher_hankook import HanKook
from dda_publisher_kookmin import KookMin

from dda_utils import search_definition, search_minor
from urllib.parse import quote
import time


def get_articles(keyword):
    res = []
    res += search_definition(keyword)

    start_time = time.time()

    # HanKook(), KookMin() excluded
    publishers = [Khan(), Hani(), ChoSun(), Joins(), DongA(), Seoul()]
    for p in publishers:
        p.set_keyword(keyword)
        p.start()

    for p in publishers:
        p.join()

    for p in publishers:
        res += p.articles[:2]

    # res += search_minor(keyword)

    end_time = time.time()
    print("Duration: ", end_time - start_time)

    return res

# 특검
# articles = get_articles("특검")
# for a in articles:
#     print(a["publisher"], a["title"], a["url"], sep=', ')


