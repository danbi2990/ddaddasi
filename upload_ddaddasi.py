import requests


def format_articles(description, articles):
    res = '<p style="text-align: justify;">{0}</p>'.format(description.replace('\u000A','<br>'))
    res += """
<table id="Gray_style" cellspacing="0" cellpadding="0" border="0">
    <tbody>
        <tr>
            <td>
            <p style="text-align: justify"><img alt="" src="http://www.danbinews.com/news/editor/images/smiley/msn/lightbulb.gif" />&nbsp;{0}</p>
""".format("관련기사로 알아보기")
    for art in articles:
        res +="""            <p style="text-align: justify">-{0}</p>
            <p style="text-align: justify"><a target="_blank" href="{2}">{1}</a></p>
""".format(art[0], art[1], art[2])
    res += """            </td>
        </tr>
    </tbody>
</table>"""
    return res.replace('\u2027','&middot;').encode('euc-kr')


def upload_ddaddasi(uid, upw, uname, email, title, subtitle, description, articles):
    session = requests.Session()

    login_info = {'user_id': uid, 'user_pw': upw}
    s = session.post("http://www.danbinews.com/member/login.php", login_info)
    # print(s.cookies)
    # print(s.text)

    upload_info = {'mode': 'input', 'idxno': '', 'area': 'D', 'level': 'B', 'view_level': 'A', 'article_type': 'B',
                   'flash_tag': '', 'recognition': 'R', 'view_recognition': 'N', 'onoff': 'F', 'serial_number': '0',
                   'pub_date_year': '0', 'pub_date_month': '0', 'pub_date_day': '0', 'page': '0', 'pdf': 'N',
                   'sectionCode': 'S1N10', 'subSectionCode': '', 'serialCode': '', 
                   'user_id': uid,
                   'user_name': uname.encode('euc-kr'), 
                   'user_email': email,
                   'title': title.encode('euc-kr'), 
                   'subTitle': subtitle.encode('euc-kr'), 
                   'summary': '',
                   'FCKeditor1': format_articles(description, articles)}
    r = session.post("http://www.danbinews.com/news/userArticleWrite.php", upload_info)
    # print('called')

# articles = (('조선','기사제목1','http://chosun.com'),
#                     ('중앙','기사제목2','http://joongang.joins.com'),
#                     ('중앙', '기사제목3', 'http://joongang.joins.com'),
#                     ('중앙', '기사제목4', 'http://joongang.joins.com'))
# print(format_articles("""설명
# 
# """
#                       , articles))
# 
# upload_ddaddasi('danbi2990','Today1234',
#                 '박진우 기자',
#                 'danbi2990@gmail.com','제목',
#                 '한줄요약',
#                 '''~아마존‧알리바바
# 
# 등 해외 사이트''',articles)

# 
# 
# 
# print(r.content)
# print("Cookie is set to:")
# print(r.cookies.get_dict())
# print("-----------")


"""
login action url: "http://www.danbinews.com/news/userArticleWrite.php"

'mode':'input'
'idxno':''
'area':'D'
'level':'B'
'view_level':'A'
'article_type':'B'
'flash_tag':''
'recognition':'R'
'view_recognition':'N'
'onoff':'F'
'serial_number':'0'
'pub_date_year':'0'
'pub_date_month':'0'
'pub_date_day':'0'
'page':'0'
'pdf':'N'
'sectionCode':'S1N10'
'subSectionCode':''
'serialCode':''
'user_id':'danbi2990'
# 'user_name':'(unable to decode value)'
# 'user_email':'danbi2990@gmail.com'
'title':' 'ddaddasi test''
'subTitle':' 'ddaddasi test''
'summary':''
'FCKeditor1':'<p>ddaddasi test</p>'

<table id="Gray_style" cellspacing="0" cellpadding="0" border="0">
    <tbody>
        <tr>
            <td>
            <p style="text-align: justify"><img alt="" src="http://www.danbinews.com/news/editor/images/smiley/msn/lightbulb.gif" />&nbsp;related article</p>
            <p style="text-align: justify">-chosun</p>
            <p style="text-align: justify"><a target="_blank" href="http://news.chosun.com/site/data/html_dir/2017/01/24/2017012401485.html">article 1</a></p>
            <p style="text-align: justify">-hani</p>
            <p style="text-align: justify"><a target="_blank" href=http://www.hani.co.kr/arti/economy/economy_general/780023.html>article 2</a></p>
            </td>
        </tr>
    </tbody>
</table>

"""


# print("called")

# login_info = {'user_id': 'danbi2990', 'user_pw': 'Today1234'}
# s = session.post("http://www.danbinews.com/member/login.php", login_info)
# # print(s.cookies)
# # print(s.text)
# 
# upload_info = {'mode':'input', 'idxno':'', 'area':'D', 'level':'B', 'view_level':'A', 'article_type':'B', 'flash_tag':'', 'recognition':'R', 'view_recognition':'N', 'onoff':'F', 'serial_number':'0', 'pub_date_year':'0', 'pub_date_month':'0', 'pub_date_day':'0', 'page':'0', 'pdf':'N', 'sectionCode':'S1N10', 'subSectionCode':'', 'serialCode':'', 'user_id':'danbi2990','user_name':'박진우 기자'.encode('euc-kr'), 'user_email':'danbi2990@gmail.com', 'title':'ddaddasi test', 'subTitle':'ddaddasi test', 'summary':'', 'FCKeditor1':'<p>ddaddasi test</p>'}
# r = session.post("http://www.danbinews.com/news/userArticleWrite.php", upload_info)

