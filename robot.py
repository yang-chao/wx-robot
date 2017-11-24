#coding:utf-8
#!/usr/bin/env python

from wxpy import *

# 扫码登陆
bot = Bot()

# 初始化图灵机器人
tuling = Tuling(api_key='535bba16d4c543889f9ba36f2174feae')

specialGroup = bot.groups().search('高精尖')[0]
specialFriend = bot.friends().search('陈洁')[0]

# 自动回复所有文字消息
# @bot.register(specialFriend, msg_types=TEXT)
# def auto_reply_all(msg):
#     tuling.do_reply(msg)

# 获取所有类型的消息（好友消息、群聊、公众号，不包括任何自己发送的消息）
# 并将获得的消息打印到控制台
@bot.register()
def print_others(msg):
    print(msg)

# 回复发送给自己的消息，可以使用这个方法来进行测试机器人而不影响到他人
# @bot.register(bot.self, except_self=False)
# def reply_self(msg):
    return 'received: {} ({})'.format(msg.text, msg.type)

# 打印出所有群聊中@自己的文本消息，并自动回复相同内容
# 这条注册消息是我们构建群聊机器人的基础
# @bot.register(Group, TEXT)
# def print_group_msg(msg):
#     if msg.is_at:
#         print(msg)
        # msg.reply(meg.text)

# 进入 Python 命令行
embed()

# 开始运行
# bot.join()
