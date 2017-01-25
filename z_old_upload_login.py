import requests

"""
name: 'user_id'
pwd: 'user_pw'
login action url: "http://www.danbinews.com/member/login.php"
'danbi2990' / 'Today1234'
"""

params = {'user_id': 'danbi2990', 'user_pw': 'Today1234'}
r = requests.post("http://www.danbinews.com/member/login.html", params)

# print("Cookie is set to:")
# print(r.cookies.get_dict())
# print("-----------")

