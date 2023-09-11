#!/bin/python3

"""
通过关键字搜索数据库中的元素
"""

import sqlite3
import sys

conn = sqlite3.connect('video.db')
cursor = conn.cursor()


def search_db(video):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print(video)
    matched_list = []
    print("\n========================")
    for table in tables:
        t_n = []
        table_name = table[0]
        cursor.execute(
            f"SELECT * FROM \"{table_name}\" WHERE name LIKE '%{video}%';")
        results = cursor.fetchall()

        # 打印匹配的结果
        if results:
            print(f"Table: {table_name}")
            for row in results:
                t_n.append(table_name)
                t_n.append(row)
                print(t_n)
                matched_list.append(t_n)
            print("\n========================")
            # break

    for a in matched_list:
        print(a)
    # print(matched_list)
    conn.close()


if __name__ == "__main__":
    search_db(sys.argv[1])
