import time

from dda_publisher_ma_req_get_chosun import ChoSun
from dda_publisher_ma_req_get_donga import DongA
from dda_publisher_ma_req_get_hani import Hani
from dda_publisher_ma_req_get_joins import Joins
from dda_publisher_ma_req_get_khan import Khan
from dda_publisher_mi_req_get_hankyung import HanKyung
from dda_publisher_mi_req_get_herald import Herald
from dda_publisher_mi_req_get_maekyung import MaeKyung
from dda_publisher_mi_req_get_newsis import NewSis
from dda_publisher_mi_req_get_seoul import Seoul
from dda_publisher_mi_req_post_munhwa import MunHwa
from dda_publisher_mi_req_post_news1 import NewsOne
from dda_publisher_mi_slnm_get_hankook import HanKook
from dda_publisher_mi_slnm_get_seokyung import SeoKyung
from dda_publisher_mi_slnm_get_yonhap import YonHap
from dda_utils import search_definition

from source.dda_publisher_mi_slnm_get_kookmin import KookMin


# publishers = [Khan(), Hani(), ChoSun(), Joins(), DongA(), Seoul(), NewSis(), HanKyung(), MaeKyung(), Herald(), NewsOne(), MunHwa()]

# slnm_pubs = [HanKook(), KookMin(), YonHap(), SeoKyung()]

def get_articles_child(drivers, keyword):
    res = []
    slnm_pubs = [HanKook(), KookMin(), YonHap(), SeoKyung()]
    # pubs = [SeoKyung()]

    start_time = time.time()

    for i in range(len(slnm_pubs)):
        slnm_pubs[i].set_keyword(keyword)
        slnm_pubs[i].set_web_driver(drivers[i].web_driver)
        slnm_pubs[i].start()
        # print(i)

    for p in slnm_pubs:
        p.join()

    for p in slnm_pubs:
        res += p.articles[:2]

    end_time = time.time()
    print("Child Duration: ", end_time - start_time)

    return res


def get_articles(keyword, result_q=None):
    res = []
    res += search_definition(keyword)

    start_time = time.time()
    publishers = [Khan(), Hani(), ChoSun(), Joins(), DongA(), Seoul(), NewSis(), HanKyung(), MaeKyung(), Herald(), NewsOne(), MunHwa()]

    for p in publishers:
        p.set_keyword(keyword)
        p.start()

    for p in publishers:
        p.join()

    for p in publishers:
        res += p.articles[:2]

    # res += search_minor(keyword)

    # timeout = time.time() + 10
    # while True:
    #     if not result_q.empty():
    #         res += result_q.get()
    #         break
    #     if time.time() > timeout:
    #         break
    #
    end_time = time.time()
    print("Parent Duration: ", end_time - start_time)

    return res

# 특검
# articles = get_articles("특검")
# for a in articles:
#     print(a["publisher"], a["title"], a["url"], sep=', ')


