#!/usr/bin/python3
#coding:utf-8
'''
request 网站
'''

import requests

if __name__ == "__main__":
    headers = {
        "Cookie":
        f""
    }

    # /recode
    url = 'http://text.com/index#'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print('请求成功')
        print(response.text)
    else:
        print('请求失败')
        print(response.text)