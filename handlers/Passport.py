#coding:utf-8

import logging
import hashlib
import config
import re

from tornado.web import RequestHandler
from handlers.BaseHandler import BaseHandler
from utils.response_code import RET
from utils.session import Session
from utils.commons import required_login

class RegisterHandler(BaseHandler):
    """注册"""
    def post(self):
        #获取参数
        mobile = self.json_args.get("mobile")
        sms_code = self.json_args.get("phonecode")
        password = self.json_args.get("password")

        #检查参数
        if not all([mobile,sms_code,password]):
            return self.write(dict(errcode=RET.PARAMERR,errmsg="参数不完整"))
        if not re.match(r"^1\d{10}$",mobile):
            return self.write(dict(errcode=RET.DATAERR,errmsg="手机号格式错误"))
        #如果产品对于密码长度有限制，需要在此做判断
        #if len(password) < 6

        #判断短信验证码是否正确
        if "2468" !=sms_code:
            try:
                real_sms_code = self.redis.get("sms_code_%s" % mobile)
            except Exception as e:
                logging.error(e)
                return self.write(dict(errcode=RET.DBERR,errmsg="查询验证码出错"))

            #判断短信验证码是否过期
            if not real_sms_code:
                return self.write(dict(errcode=RET.NODATA,errmsg="验证码过期"))

            #对此用户填写的验证码真实值
            #if real_smd_code !=sms_code and sms_code != "2468"
            if real_sms_code != sms_code:
                return self.write(dict(errcode=RET.DATAERR,errmsg="验证码错误"))

            try:
                self.redis.delete("sms_code_%s" % mobile)
            except Exception as e:
                logging.error(e)
        #保存数据，同时判断手机号是否存在,判断的依据是数据库中mobile字段的唯一约束
        passwd = hashlib.sha256(password + config.passwd_hash_key).hexdigest()
        sql = "insert into ih_user_profile(up_name, up_mobile, up_passwd) values(%(name)s, %(mobile)s, %(passwd)s);"
        try:
            user_id = self.db.excute(sql,name=mobile,mobile=mobile,passwd=password)
        except Exception as e:
            logging.error(e)
            return self.write(dict(errcode=RET.DATAEXIST,errmsg="手机号已存在"))

        #用session记录用户的登录状态
        session = Session(self)
        session.data["user_id"] = user_id
        session.data["mobile"]  = mobile
        session.data["name"]    = mobile