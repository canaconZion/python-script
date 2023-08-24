#!/usr/bin/python3
#coding:utf-8
'''
将txt中的内容，按行写入excel表格
'''

import openpyxl

# 替换为你的输入文件和输出文件路径
input_file = 'msg.txt'
output_file = 'msg.xlsx'

# 创建一个新的Excel工作簿
workbook = openpyxl.Workbook()
sheet = workbook.active

# 打开.txt文件并逐行读取内容，将每行内容写入Excel表格中
with open(input_file, 'r') as file:
    for line in file:
        # 使用strip()方法去除每行开头和结尾的空格和换行符
        line = line.strip()
        # 将内容写入Excel表格的下一行
        sheet.append([line])

# 保存Excel工作簿到输出文件
workbook.save(output_file)
