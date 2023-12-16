import pymysql
import requests
import time
import threading
from datetime import datetime
import os

start = time.time()

db = pymysql.connect(
    host="192.168.2.123",
    user="root",
    password="1207",
    port=3306,  # 端口  
    database="",
    charset='utf8')
# try:
with db.cursor() as cursor:
    sql = f"SELECT vod_id,vod_play_from,vod_play_url FROM `mac_vod_1000`"
    cursor.execute(sql)
    values = cursor.fetchall()
    for results in values:
        # results = cursor.fetchone()
        # if results is None:
        #     break
        print(results[0])
        url_list = results[2].split("$$$")
        from_list = results[1].split("$$$")
        if url_list != [""]:
            for u, f in zip(url_list, from_list):
                e_url_list = u.split("#")
                for e_u in e_url_list:
                    # print(f"{results[0]}url:{str(e_u)}")
                    n_u = e_u.split("$")
                    if len(n_u) != 2:
                        print("error")
                        with open("error.txt", "a") as f:
                            f.write(f"{results[0]}\n")
                    else:
                        # print(str(n_u[1]),"\n")
                        try:
                            sql = f"INSERT INTO vod_url_msg(vod_id,vod_play_from,vod_play_url) VALUES ({results[0]},'{f}','{n_u[1]}')"
                            cursor.execute(sql)
                            print(results[0])
                        except Exception as e:
                            with open("error.txt", "a") as f:
                                f.write(f"{results[0]}\n")
            db.commit()
db.close()
end = time.time()
print(end - start)