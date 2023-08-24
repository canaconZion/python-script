#!/usr/bin/python3
#coding:utf-8
'''
寻找文件名中包含指定字段的文件，将其绝对路径写入msg.txt中
'''

import os
import fnmatch

def find_m3u8_files(root_dir, output_file):
    with open(output_file, 'w') as f:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            for filename in fnmatch.filter(filenames, '*.m3u8'):
                file_path = os.path.abspath(os.path.join(dirpath, filename))
                print(file_path + '\n')
                f.write(file_path + '\n')

if __name__ == "__main__":
    root_directory = '/home/data/docker/video/vod'
    output_file = 'msg.txt'
    find_m3u8_files(root_directory, output_file)

