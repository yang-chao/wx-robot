import itchat
import time
import requests
import hashlib


# 图灵机器人
def get_response(msg, FromUserName):
    api_url = 'http://www.tuling123.com/openapi/api'
    apikey = '**************************'
    # data中有userd才能实现上下文一致的聊天效果。
    hash = hashlib.md5()
    userid = hash.update(FromUserName.encode('utf-8'))
    data = {'key': apikey,
            'info': msg,
            'userid': userid
            }
    try:
        req = requests.post(api_url, data=data).json()
        return req.get('text')
    except:
        return



itchat.auto_login()


#适合 个人间聊天
@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing'])
def Tuling_robot(msg):
    respones = get_response(msg['Content'], msg['FromUserName'])
    itchat.send(respones, msg['FromUserName'])

#返回图片，录音，视频
@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
def download_files(msg):
    fileDir = '%s%s'%(msg['Type'], int(time.time()))
    msg['Text'](fileDir)
    itchat.send('%s received'%msg['Type'], msg['FromUserName'])
    itchat.send('@%s@%s'%('img' if msg['Type'] == 'Picture' else 'fil', fileDir), msg['FromUserName'])

#自动同意陌生人好友申请
@itchat.msg_register('Friends')
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])


Message = '整点新闻：如何留住制造业人才 董明珠霸气送房'
GroupsContainer = set()
"""
#整点发新闻
检测时间，到时间节点就触发程序执行群发消息的任务。本例子中是八点整触发程序执行群内新闻播报
通过监控群聊，收集微信群的UserName并保存起来，方便后续群发。
"""
@itchat.msg_register('Text', isGroupChat = False) #isGroupChat为True,机器人可以回复群内消息，为False不能回复群内消息
def broadcast(msg):
    response = get_response(msg['Content'], msg['FromUserName'])
    itchat.send(response, msg['FromUserName'])
    groups_json_list = itchat.get_chatrooms()
    groupsName = [nm.get('UserName') for nm in groups_json_list]
    groupsName = set(groupsName)
    for grpn in groupsName:
        GroupsContainer.add(grpn)
    while True:
        current_time = time.localtime(time.time())
        if ((current_time.tm_hour == 8) and (current_time.tm_min == 0) and (current_time.tm_sec == 0)):
            for grn in GroupsContainer:
                itchat.send(Message, grn)


itchat.run()