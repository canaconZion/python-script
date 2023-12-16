#!/bin/python3
"""
将数据库中的数据导出到excel表格
"""

import sqlite3
import openpyxl

conn = sqlite3.connect('video.db')
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

workbook = openpyxl.Workbook()

worksheet = workbook.create_sheet(title="video")
worksheet.append(['表名', 'name'])
for table in tables:
    table_name = table[0]
    cursor.execute(f"SELECT name FROM \"{table_name}\";")
    data = cursor.fetchall()

    for row in data:
        encoded_row = [table_name, row[0]]
        worksheet.append(encoded_row)
workbook.remove(workbook['Sheet'])
workbook.save('database_data.xlsx')
conn.close()
