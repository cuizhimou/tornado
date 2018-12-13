#coding:utf-8

import os
from handlers import Passport,VerifyCode,Profile,House,Orders
from tornado.web import StaticFileHandler

handlers = [
    (r"/api/imagecode",VerifyCode.ImageCodeHandler),
    (r"/api/smscode", VerifyCode.SMSCodeHandler),
    (r"/api/register",Passport.RegisterHandler),
    (r"/api/check_login",Passport.CheckLoginHandler),
    (r"/api/login",Passport.LoginHandler),
    (r"/api/logout",Passport.LogoutHandler),
    (r"/api/check_login",Passport.CheckLoginHandler),
    (r"/api/profile/avatar",Profile.AvatarHandler),#用户上传头像
    (r"/api/profile",Profile.ProfileHandler),#个人主页信息获取个人信息
    (r"/api/profile/name",Profile.NameHandler),#个人主页修改用户名
    (r"/api/pfofile/auth",Profile.AuthHandler),#实名认证
    (r"/api/house/area", House.AreaInfoHandler), # 城区信息
    (r'^/api/house/info$', House.HouseInfoHandler), # 上传房屋的基本信息
    (r'^/api/house/image$', House.HouseImageHandler), # 上传房屋图片
    (r'^/api/house/my$', House.MyHousesHandler), # 查询用户发布的房源
    (r'^/api/house/index$', House.IndexHandler), # 首页
    (r'^/api/house/list$', House.HouseListHandler), # 房屋过滤列表数据
    (r'^/api/house/list2$', House.HouseListRedisHandler), # 房屋过滤列表数据
    (r'^/api/order$', Orders.OrderHandler), # 下单
    (r'^/api/order/my$', Orders.MyOrdersHandler), # 我的订单，作为房客和房东同时适用
    (r'^/api/order/accept$', Orders.AcceptOrderHandler), # 接单
    (r'^/api/order/reject$', Orders.RejectOrderHandler), # 拒单
    (r'^/api/order/comment$', Orders.OrderCommentHandler),
    (r"/(.*)",StaticFileHandler,dict(path=os.path.join(os.path.dirname(
        __file__),"html"),default_filename="index.html")),

]