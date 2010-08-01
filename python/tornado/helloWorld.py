#!/usr/bin/python

import tornado.httpserver
import tornado.ioloop
import tornado.web

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World")

application = tornado.web.Application([
    (r"/", HelloHandler),
])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
