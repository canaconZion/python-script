#!/usr/bin/python3
#coding:utf-8
'''
批量化修改文件名，会删除文件名中的中文空格和特殊字符，
将中文转化为拼音字母，
并在目录下生成 description.txt 文件保存原来的文件名
'''

import os
import shutil
import re
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

def rename_folder_and_files(root_path):
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

            # 创建并保存原始文件夹名称的描述文件
            description_file_path = os.path.join(new_folder_path, 'description.txt')
            with open(description_file_path, 'w') as f:
                f.write(entry.name)
            
            # 递归处理子文件夹
            rename_folder_and_files(new_folder_path)
        elif entry.is_file():
            # 处理文件
            file_name, file_ext = os.path.splitext(entry.name)
            new_file_name = remove_special_characters(file_name)
            new_file_name = convert_to_pinyin(new_file_name)
            new_file_name = new_file_name + file_ext
            new_file_path = os.path.join(root_path, new_file_name)
            os.rename(entry.path, new_file_path)

            if file_ext == '.m3u8':
                # 处理 m3u8 文件中需要播放的 .ts 文件名
                with open(new_file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # 正则表达式模式，匹配中文标点符号
                punctuation_pattern = r'[\u3000-\u303f\uff01-\uff0f\uff1a-\uff20\uff3b-\uff40\uff5b-\uff65\uffe5]'
                
                # 删除中文标点符号
                content = re.sub(punctuation_pattern, '', content)
                
                # 将中文转化为拼音
                pinyin_content = pinyin(content, style=Style.NORMAL)
                pinyin_content = ''.join([item[0] for item in pinyin_content])
                
                with open(new_file_path, 'w', encoding='utf-8') as f:
                    f.write(pinyin_content)

if __name__ == "__main__":
    root_directory = '/mnt/f/file/点播'
    rename_folder_and_files(root_directory)
