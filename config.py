#coding:utf-8

import os

#application配置参数
settings = {
    "static_path":os.path.join(os.path.dirname(__file__), "static"),
    "template_path":os.path.join(os.path.dirname(__file__),"template"),
    "cookie_secret":"ScDhzx04SNm3e5InXphoV/HiKongLUM+jeyRSkem+3Y=",
    "xsrf_cookies":True,
    "debug":True,
}

#mysql
mysql_options=dict(
    host="192.168.1.170",
    database="ihome",
    user="root",
    password="mysql"
)

#redis
redis_options = dict(
    host="192.168.1.170",
    port=6379
)

#log
log_file = os.path.join(os.path.dirname(__file__),"logs/log")
log_level = "debug"