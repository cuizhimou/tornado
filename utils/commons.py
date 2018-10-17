# coding:utf-8

import functools

from utils.session import Session
from utils.response_code import RET


def required_login(fun):
    # 保证被装饰的函数对象的__name__不变
    @functools.wraps(fun)
    def wrapper(request_handler_obj, *args, **kwargs):
        # 调用get_current_user方法判断用户是否登录
        if not request_handler_obj.get_current_user():
        # session = Session(request_handler_obj)
        # if not session.data:
            request_handler_obj.write(dict(errcode=RET.SESSIONERR, errmsg="用户未登录"))
        else:
            fun(request_handler_obj, *args, **kwargs)
    return wrapper

# @dec
# def add_two(num1, num2):
#     return num1+num2
#
# add_two = dec(add_two)    .__name__ = "add_two"
#
# @dec
# def add_three(num1, num2, num3):
#     return num1+num2+num3
#
# def dec(f):
#     @functools.wraps(f)
#     def wrapper(*args, **kwargs):
#         print("hello")
#         f(*args, **kwargs)
#     return wrapper
#
#
#
# def main(fun):
#     a, b, c = 1, 2, 3
#     if fun.__name__ == "add_two":
#         fun(a, b)
#     elif fun.__name__ == "add_three":
#         fun(a, b, c)























