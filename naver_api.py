import os
import sys
import urllib.request
import json

major = {'hani.co.kr':'한겨레', 'news.chosun.com':'조선일보', 'khan.co.kr':'경향신문', 'joongang.joins.com':'중앙일보', 'donga.com':'동아일보'}

client_id = "etxyO6Nmsb8_r9_llGKN"
client_secret = "S8Dls1GTNU"
encText = urllib.parse.quote("전안법")
url = "https://openapi.naver.com/v1/search/news?query=" + encText + "&display=100" # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()


if(rescode==200):
    response_body = response.read()
    res_str = response_body.decode('utf-8')
    res_json = json.loads(res_str)
    items = res_json["items"]

    # major_items = [x.append(y,major[y]) for x in items for y in major if x['link'].find(y) != -1]
    # print(major_items)
    print(type(items))
    print(items)
    # print(type(res_json))
    # print(res_json)



    # response_body = response.read()
    # print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
