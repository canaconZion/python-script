#!/usr/bin/python3
#coding:utf-8
'''
request 接口
'''

import requests


def post_req():
    response = requests.post("http://localhost:6003/generate_token")
    token = response.json().get("token")
    print(response.json())
    headers = {"Authorization": f"Bearer {token}"}

    # /recode
    url = 'http://localhost:6003/info'
    data = {'file': 'mecha.mp4'}
    response = requests.post(url, headers=headers, params=data)
    if response.status_code == 200:
        print('请求成功')
        print(response.json())
    else:
        print('请求失败')
        print(response.text)
    return response.status_code


def get_req():
    headers = {"Cookie": f""}

    url = 'http://localhost:6003/get_msg'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print('请求成功')
        print(response.text)
    else:
        print('请求失败')
        print(response.text)
    return response.status_code


if __name__ == "__main__":
    get_req()
    #post_req()