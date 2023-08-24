#!/usr/bin/python3
#coding:utf-8
'''
调用linux命令行
'''

import subprocess
import os


def run_os_command():
    comm = "df -h"
    res = os.system(comm)
    if res == 0:
        print("os successful")
    else:
        print("error")


def run_sub_command():
    ''' 通过subprocess调用，可以捕获命令行输出的错误信息 '''
    comm = "df -h"
    p = subprocess.Popen(comm,
                         shell=True,
                         preexec_fn=os.setsid,
                         executable='bash',
                         stderr=subprocess.PIPE)
    p.wait()
    rcode = p.returncode
    if rcode != 0 and rcode != 255:
        output, err = p.communicate()
        err_str = err.decode('utf-8')
        print("ERROR: " + err_str)
    elif rcode == 255:
        print("recode process was killed !!!")
    elif rcode == 0:
        print("subprocess successful")


if __name__ == "__main__":
    run_os_command()