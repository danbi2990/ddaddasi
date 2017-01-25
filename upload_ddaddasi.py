import requests

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

session = requests.Session()
login_info = {'user_id': 'danbi2990', 'user_pw': 'Today1234'}
s = session.post("http://www.danbinews.com/member/login.php", login_info)
# print(s.cookies)
# print(s.text)

upload_info = {'mode':'input', 'idxno':'', 'area':'D', 'level':'B', 'view_level':'A', 'article_type':'B', 'flash_tag':'', 'recognition':'R', 'view_recognition':'N', 'onoff':'F', 'serial_number':'0', 'pub_date_year':'0', 'pub_date_month':'0', 'pub_date_day':'0', 'page':'0', 'pdf':'N', 'sectionCode':'S1N10', 'subSectionCode':'', 'serialCode':'', 'user_id':'danbi2990','user_name':'박진우 기자'.encode('euc-kr'), 'user_email':'danbi2990@gmail.com', 'title':'ddaddasi test', 'subTitle':'ddaddasi test', 'summary':'', 'FCKeditor1':'<p>ddaddasi test</p>'}
r = session.post("http://www.danbinews.com/news/userArticleWrite.php", upload_info)
# 
# 
# 
# print(r.content)
# print("Cookie is set to:")
# print(r.cookies.get_dict())
# print("-----------")




