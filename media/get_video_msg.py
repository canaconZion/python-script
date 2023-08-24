#!/usr/bin/python3
#coding:utf-8
'''
获取媒体文件的信息
'''

from pymediainfo import MediaInfo
import os

def get_video_msg(file_path: str):
    video_msg = {}
    file_extension = os.path.splitext(file_path)[1]
    media_info = MediaInfo.parse(file_path)
    data = media_info.to_data()
    print(data)

if __name__ == '__main__':
    get_video_msg("/home/zion/workdir/zk-vod/video/a/a.mp4")