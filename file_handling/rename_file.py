#!/usr/bin/python3
#coding:utf-8
'''
批量化修改文件名，会删除文件名中的中文空格和特殊字符，
将中文转化为拼音字母，
并在目录下生成 description.txt 文件保存原来的文件名
'''

import os
import sys
import shutil
import re
import json
from pypinyin import pinyin, Style


def remove_special_characters(string):
    """
    删除字符串中的空格和特殊字符
    """
    return re.sub(r'\s+|[^\w\s.]', '', string)


def convert_to_pinyin(string):
    """
    将字符串中的中文转化为拼音
    """
    pinyin_list = pinyin(string, style=Style.NORMAL)
    return ''.join([item[0] for item in pinyin_list])


def rename_folder_and_files(root_path, json_file):
    """
    递归地重命名文件夹及文件
    """
    for entry in os.scandir(root_path):
        if entry.is_dir():
            # 处理文件夹
            new_folder_name = remove_special_characters(entry.name)
            new_folder_name = convert_to_pinyin(new_folder_name)
            new_folder_path = os.path.join(root_path, new_folder_name)
            os.rename(entry.path, new_folder_path)
            w_str = f"\"{new_folder_name}\":\"{entry.path}\""
            write_in_json(json_file, w_str)
            rename_folder_and_files(new_folder_path, json_file)
        elif entry.is_file():
            # 处理文件
            file_name, file_ext = os.path.splitext(entry.name)
            new_file_name = remove_special_characters(file_name)
            new_file_name = convert_to_pinyin(new_file_name)
            new_file_no_ext=os.path.join(root_path, new_file_name)
            new_file_name = new_file_name + file_ext
            new_file_path = os.path.join(root_path, new_file_name)
            w_str = f"\"{new_file_no_ext}\":\"{file_name}\""
            write_in_json(json_file, w_str)
            os.rename(entry.path, new_file_path)


def write_in_json(json_file, value):
    with open(json_file, 'a', encoding='utf-8') as f:
        f.write(value + ",\n")


def read_json():
    with open('./data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


# def rename_folder_and_files(root_path):
#     # 获取文件夹中所有文件
#     file_list = os.listdir(root_path)

if __name__ == "__main__":
    root_path = ''
    json_file = "json/rename0826.json"
    if len(sys.argv) > 1:
        root_path = sys.argv[1]
        with open(json_file, 'a', encoding='utf-8') as f:
            f.write("{\n")
        rename_folder_and_files(root_path, json_file)
        with open(json_file, 'a', encoding='utf-8') as f:
            f.write("\"None\":\"None\"\n}")
    else:
        root_path = ""
        print("Please input root dir")
    # root_directory = '/mnt/f/file/点播'
    # json_file = "json/rename.json"
    # write_in_json(json_file)
