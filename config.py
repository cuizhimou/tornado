#coding:utf-8

import os

#application配置参数
settings = {
    "static_path":os.path.join(os.path.dirname(__file__), "static"),
    "template_path":os.path.join(os.path.dirname(__file__),"template"),
    "cookie_secret":"ScDhzx04SNm3e5InXphoV/HiKongLUM+jeyRSkem+3Y=",
    "xsrf_cookies":False,
    "debug":True,
}

#mysql
mysql_options=dict(
    host="192.168.2.4",
    database="ihome",
    user="root",
    password="study"
)

#redis
redis_options = dict(
    host="192.168.2.4",
    port=6379,
)

#log
log_file = os.path.join(os.path.dirname(__file__),"logs/log")
log_level = "debug"

#密码加密秘钥
passwd_hash_key = "nlgCjaTXQX2jpupQFQLoQo5N4OkEmkeHsHD9+BBx2WQ="