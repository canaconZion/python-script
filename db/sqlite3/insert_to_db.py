#!/bin/python3

"""
sqlite数据库操作
"""

import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()
table = "video"
data = "mecha.mp4"
cur.execute(f"CREATE TABLE IF NOT EXISTS \"{table}\"(id INTEGER PRIMARY KEY,name TEXT)")
cur.execute(f"INSERT INTO \"{table}\"(name) VALUES (\"{data}\")")  
con.commit()
cur.close()
con.close()