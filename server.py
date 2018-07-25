# coding=utf-8
import tornado.ioloop
import tornado.httpserver
import tornado.options
from tornado.options import options, define
from urls import handlers
import config
import redis

define('port', default=8000, type=int, help='run server on the given port')

class Application(tornado.web.Application):
    """"""
    def __init__(self, *args,**kwargs):
        super(Application,self).__init__(*args,**kwargs)
        # self.db=tornado.Connection(
        #     host=config.mysql_options['host'],
        #     database=config.mysql_options['database'],
        #     user=config.mysql_options['user'],
        #     password=config.mysql_options['password']
        # )
        self.db = tornado.Connection(**config.mysql_options)
        # self.redis = redis.StrictRedis(
        #     host=config.redis_options['host'],
        #     port=config.redis_options['port']
        # )
        self.redis = redis.StrictRedis(**config.redis_options)

def main():
    options.logging = config.log_level
    options.log_file_prefix = config.log_file
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers, **config.settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    #http_server.bind(8000)
    #http_server.start(0)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()