#coding:utf-8

from handlers import Passport

handlers = [
    (r"/",Passport.IndexHandler),
]