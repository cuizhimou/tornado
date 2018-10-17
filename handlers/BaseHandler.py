#coding:utf-8

from tornado.web import RequestHandler
import json


class BaseHandler(RequestHandler):
    """handler基类"""
    @property
    def db(self):
        return self.application.db

    @property
    def redis(self):
        return self.application.redis

    def prepare(self):
        self.xsrf_token
        if self.request.headers.get("Content-Type","").startswith("application/json"):
            self.json_args=json.loads(self.request.body)
        else:
            self.json_args=None

    def write_error(self, status_code, **kwargs):
        pass

    def set_default_headers(self):
        pass

    def initialize(self):
        pass

    def on_finish(self):
        pass