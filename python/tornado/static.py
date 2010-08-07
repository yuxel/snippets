#!/usr/bin/env python
# Demonstrationg static file serving on tornado

import tornado.httpserver
import tornado.ioloop
import tornado.web
import os

# demonstrates cookie usage
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Static files are located on static/')

application = tornado.web.Application([
    (r"/", MainHandler),
], static_path = os.path.join(os.path.dirname(__file__), "static"))

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
