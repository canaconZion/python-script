#!/bin/python3
"""
统计数据库中的总数据数
"""

import sqlite3

con = sqlite3.connect('video.db')
cursor = con.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
total_rows = 0
for table in tables:
    table_name = table[0]
    cursor.execute(f"SELECT COUNT(*) FROM \"{table_name}\";")
    row_count = cursor.fetchone()[0]
    print(f"Table {table_name}: {row_count} rows")
    total_rows += row_count

print(f"Total rows in all tables: {total_rows}")
con.close()
