#!/usr/bin/env python
# coding=utf-8
__auther__ = 'liazylee'
# connect='li233111@gmail.com'
# @Time    : 6/13/19 11:03 AM
# @FileName: proxy_pool.py
# @Software: PyCharm
# @project: woaidu


import requests
def get_proxy():
    proxy=requests.get('http://47.104.5.200:5010/get/').content.decode("utf-8")
    return proxy