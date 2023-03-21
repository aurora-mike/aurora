import os
import pyautogui as pg

import json
import time
import requests
import socket
from weworkbot import Bot as bot

WEBHOOK = '3ae09d54-afb7-4a87-afe0-a29c263ecc99'
URL = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=' + WEBHOOK
UPLOAD_URL = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key=' + WEBHOOK + '&type=file'

def upload_file(file_path):

    files = {'file': open(file_path, 'rb')}
    media_id = requests.post(url=UPLOAD_URL, files=files).json()['media_id']

    headers = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    data ={
        "msgtype": "file",
        "file": {
            "media_id": media_id
        }
    }

    data = json.dumps(data)
    requests.post(url=URL, data=data, headers=headers)



if __name__ == "__main__":

    # bot(URL).set_text("Hi, I am Robot 朝晖小助手 - Dev\nAdded to the group by 张睿 on 03/20", 'text').send()
    # bot(URL).set_image_path()
    # ai.chatgpt.chat(api_key='', prompt='你好我是朝晖小助手')
    file_path = '/Users/mike/Library/Mobile Documents/com~apple~CloudDocs/Work/系统/宏观/朝晖 商品 2023.03.21.pdf'
    upload_file(file_path)

