from dda_publisher_ma_req_get_khan import Khan
from dda_publisher_ma_req_get_hani import Hani
from dda_publisher_ma_req_get_chosun import ChoSun
from dda_publisher_ma_req_get_joins import Joins
from dda_publisher_ma_req_get_donga import DongA
from dda_publisher_mi_req_get_seoul import Seoul
from dda_publisher_mi_req_get_newsis import NewSis
from dda_publisher_mi_req_get_hankyung import HanKyung
from dda_publisher_mi_req_get_maekyung import MaeKyung
from dda_publisher_mi_req_get_herald import Herald
from dda_publisher_mi_req_post_news1 import NewsOne
from dda_publisher_mi_req_post_munhwa import MunHwa

from dda_publisher_mi_slnm_get_hankook import HanKook
from dda_publisher_mi_slnm_get_kookmin import KookMin

from dda_utils import search_definition, search_minor
import time

from multiprocessing import Process, Queue, Pipe
from selenium import webdriver
from urllib.parse import quote



# def slow_article():
#     driver = [webdriver.PhantomJS('./phantomjs/bin/phantomjs')]
#     while True:
#         p = (yield)


def get_articles(keyword):
    res = []
    res += search_definition(keyword)

    start_time = time.time()

    # HanKook(), KookMin() excluded
    publishers = [Khan(), Hani(), ChoSun(), Joins(), DongA(), Seoul(), NewSis(), HanKyung(), MaeKyung(), Herald(), NewsOne(), MunHwa()]
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


