import requests
from random import choice

username = '你的账号'
password = '你的密码'
login_url = 'http://58.193.0.104/?q=custom_user_login'
course_url= 'http://58.193.0.104/?q=items/student/study/75827'
comment_url= 'http://58.193.0.104/?q=item/comments/save'
vedio_url= 'http://58.193.0.104/?q=items/study/current/save'
doc_url= 'http://58.193.0.104/?q=items/student/study/75827/'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
headers = {'User-Agnet': user_agent, 'Connection': 'keep-alive'}
unit_id_max = 2889

#用户登陆
requests_session = requests.session()
login = {'username': username, 'password': password}
login_response = requests_session.post(url=login_url,data=login,headers=headers)
print('正在登陆')
course_response = requests_session.get(url=course_url)
if(course_response.status_code == 200):
    print('登陆成功')

#课程视频
vedio_unit_id = 2886
while vedio_unit_id <= unit_id_max:
    vedio_item_id = 33260
    vedio_item_id_max = 33429
    while vedio_item_id <= vedio_item_id_max:
        fid = vedio_item_id + 11889
        vedio_from='http://58.193.0.104/?q=items/student/study/75827/'+str(vedio_unit_id)+'/'+str(vedio_item_id)
        vedio_data = {'fid':fid, 'from': vedio_from,'item_id':vedio_item_id,'resource': '0','time':'666','totaltime':'666'}
        vedio_response  = requests_session.post(url=vedio_url,data=vedio_data,headers=headers)
        vedio_item_id = vedio_item_id + 1
        print(vedio_unit_id,'的',vedio_item_id,'视频播放完成')
    vedio_unit_id = vedio_unit_id + 1

#课程文档
doc_unit_id = 2886
while doc_unit_id <= unit_id_max:
    doc_item_id = 33260
    doc_item_id_max = 33429
    while doc_item_id <= doc_item_id_max:
        doc_get_url = doc_url + str(doc_unit_id)+'/'+str(doc_item_id)
        doc_response  = requests_session.get(url=doc_get_url,headers=headers)
        doc_item_id = doc_item_id + 1
        print(doc_unit_id,'的',doc_item_id,'文档浏览完成')
    doc_unit_id = doc_unit_id + 1


#课程评论
comment_item_id = 33260
item_id_max = 34935
comment_content=['老师讲的很好','老师真的很棒','谢谢老师的耐心讲解','送老师一个666','为老师打call','重要的知识点讲得很棒','课程内容很详细','对学习很有帮助','课程很棒，值得学习','很棒，给老师一杯卡布奇诺','给老师一个么么哒']
while comment_item_id <= item_id_max:
    comment_data = {'content':choice(comment_content)  , 'star_num': '5','item_id':comment_item_id,'course_id': '75827'}
    comment_response = requests_session.post(url=comment_url,data=comment_data,headers=headers)
    print('正在评论',comment_item_id)
    comment_item_id = comment_item_id + 1
