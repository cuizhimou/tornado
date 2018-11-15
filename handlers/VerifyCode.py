#coding:utf-8

import logging
import constants
import random
import re

from .BaseHandler import BaseHandler
from utils.captcha.captcha import captcha
from utils.response_code import RET


class ImageCodeHandler(BaseHandler):
    """"""
    def get(self):
        code_id = self.get_argument("codeid")
        pre_code_id = self.get_argument("pcodeid")
        if pre_code_id:
            try:
                self.redis.delete("image_code_%s" % pre_code_id)
            except Exception as e:
                logging.error(e)
        """
        name ，text ，image

        """
        name,text,image = captcha.generate_captcha()
        try:
            self.redis.setex("image_code_%s" % code_id,constants.IMAGE_CODE_EXPIRES_SECONDS,text)
        except Exception as e:
            logging.error(e)
            self.write("")
        self.set_header("Content-Type","image/jpg")
        self.write(image)


class  SMSCodeHandler(BaseHandler):
    """"""
    def post(self):
        #获取参数
        mobile = self.json_args.get("mobile")
        image_code_id = self.json_args.get("image_code_id")
        image_code_text = self.json_args.get("image_code_text")
        if not all((mobile,image_code_id,image_code_text)):
            return self.write(dict(error=RET.PARAMERR,errmsg="参数错误"))
        if not re.match(r"1\d{10}",mobile):
            return self.write(dict(errno=RET.PARAMERR,errmsg="手机号错误"))
        #判断图片验证码
        try:
            real_image_code_text=self.redis.get('image_code_%s' % image_code_id)
        except  Exception as e:
            logging.error(e)
            return self.write(dict(errno=RET.DBERR,errmsg="查询出错"))
        if not real_image_code_text:
            return self.write(dict(errno=RET.NODATA,errmsg="验证码过期"))

        if real_image_code_text.lower() != image_code_text.lower():
            return self.write(dict(errno=RET.DATAERR,errmsg="验证码错误"))

        #若成功
        #生成随机验证码
        sms_code = "%4d" % random.randint(0,999)
        try:
            self.redis.setex("sms_code_%s" % mobile,constants.SMS_CODE_EXPIPES_SECODES,sms_code)
            logging.info(sms_code)
        except Exception as e:
            logging.error(e)
            return self.write(dict(errno=RET.DBERR,errmsg="生成短信验证码错误"))

        #发送短信
        try:
            pass#短信服务未开通，省略
        except Exception as e:
            pass#发送失败的情况
        self.write(dict(errno=RET.OK,errmsg="ok"))
        #不成功
        #返回错误信息