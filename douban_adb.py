import random
import os
import time
import datetime
import xml.etree.cElementTree as ET

"""
python套shell, 增加随机话术
"""

def log(msg):
    print('{}: {}'.format(datetime.datetime.now(), msg))

def rand(min, max):
  return random.randint(min, max)


def call_shell(cmd):
  log(cmd)
  os.system(cmd)

def random_text():
  return random.choice(['看房', '来', '嗯', '来了', '啊啊啊', '啊啊', '啊', '啦啦', '😋', '在', '不', '(づ￣3￣)づ╭❤～', '看看',
                        'ok', '哈哈', '租', '来喽', '♪(^∇^*)', '哈', '木北', '支持', '赞', '👍', '作一首诗', '三元桥', '来一首诗',
                        '好累', '没法上班了', '凡人', '呀', '考虑考虑', '进近景近', '健健康康', '走起', '看',
                        '支持', '支持', '支持', '支持', '支持', '支持',
                        '周六日随时看房', '周末随时看房', '周六日随时看房', '周末随时看房', '周六日随时看房', '周末随时看房', '周六日随时看房',
                        '周末随时看房', '周六日随时看房', '周末随时看房', '周六日随时看房', '周末随时看房''周六日随时看房', '周末随时看房',
                        '周末随时看房', '周六日随时看房', '周末随时看房', '周六日随时看房', '周末随时看房''周六日随时看房', '周末随时看房',
                        '周末随时看房', '周六日随时看房', '周末随时看房', '周六日随时看房', '周末随时看房''周六日随时看房', '周末随时看房',
                        ])

def reply():
  log('>>> start reply')
  call_shell('adb shell input tap 300 2300')
  time.sleep(1)
  text = random_text()
  call_shell('adb shell am broadcast -a ADB_INPUT_TEXT --es msg "{}"'.format(text))

  time.sleep(1)
  call_shell('adb shell input tap 1000 2250')


def dump():
    call_shell('adb shell uiautomator dump /sdcard/uidump.xml')
    call_shell('adb pull /sdcard/uidump.xml')



while True:
    reply()
    sleep = rand(60 * 5, 60 * 15)
    log('sleep {}min'.format(sleep // 60))
    time.sleep(sleep)
