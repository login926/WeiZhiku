import requests

login_url = 'http://58.193.0.104/?q=custom_user_login'
course_url= 'http://58.193.0.104/?q=user/27407/course'
comment_url= 'http://58.193.0.104/?q=item/comments/save'
item_id = 33260
item_id_max = 34936
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
headers = {'User-Agnet': user_agent, 'Connection': 'keep-alive'}


requests_session = requests.session()
login = {'username': '13012345678', 'password': 'testpass'}
#1301234567和testpass更改为自己的账号和密码
login_response = requests_session.post(url=login_url,data=login,headers=headers)
print('正在登陆')

course_response = requests_session.get(url=course_url)
if(course_response.status_code == 200):
    print('登陆成功')


while item_id < item_id_max:
    comment = {'content': '老师讲的很好', 'star_num': '5','item_id':item_id,'course_id': '75827'}
    comment_response = requests_session.post(url=comment_url,data=comment,headers=headers,timeout=1)
    print('正在评论',item_id)
    item_id = item_id + 1
