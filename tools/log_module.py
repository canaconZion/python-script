#!/usr/bin/python3
#coding:utf-8
'''
生成日志
'''

import logging
from logging.handlers import RotatingFileHandler


def logging_fun():
    # TODO 可以通过配置文件设置日志等级
    logging.basicConfig(level=logging.DEBUG)
    log_handle = RotatingFileHandler(
        "log/vod.log", maxBytes=10 * 1024 * 1024,
        backupCount=10)  # 单个日志文件最大为10MB, 最多保留10个日志文件
    formatter = logging.Formatter(
        '%(asctime)s [%(name)s][%(funcName)s][%(levelname)s] %(message)s')
    log_handle.setFormatter(formatter)
    return log_handle


def log_test(log_handle):
    logging.getLogger().addHandler(log_handle)
    logging.debug("debug")
    logging.info("info")
    logging.warning("warning")
    logging.error("error")
    logging.critical("critical")


if __name__ == '__main__':
    a = logging_fun()
    log_test(a)