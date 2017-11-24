#coding:utf-8
#!/usr/bin/env python

from wxpy import *

# 扫码登陆
bot = Bot()

# 初始化图灵机器人
tuling = Tuling(api_key='535bba16d4c543889f9ba36f2174feae')

specialGroup = bot.groups().search('高精尖')[0]
# 自动回复所有文字消息
@bot.register(specialGroup, msg_types=TEXT)
def auto_reply_all(msg):
    tuling.do_reply(msg)

# 开始运行
bot.join()
