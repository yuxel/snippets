#!/usr/bin/env python
# Demonstrationg template usage of tornadoweb

import tornado.httpserver
import tornado.ioloop
import tornado.web
import time

# handles main page 
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        cookieName = "pyist";
        cookieValue = self.get_cookie(cookieName)
        currentTimestamp = str(time.time())
        if not cookieValue:
            self.set_cookie(cookieName, currentTimestamp)
            self.write("I've just set your cookie, refresh!")
        else:
            self.write("Cookie value : " + cookieValue)

# demonstrates secure cookie example
class SecureCookieHandler(tornado.web.RequestHandler):
    def get(self):
        cookieName = "pyist_secure";
        cookieValue = self.get_secure_cookie(cookieName)
        currentTimestamp = str(time.time())
        if not cookieValue:
            self.set_secure_cookie(cookieName, currentTimestamp)
            self.write("I've just set your cookie, refresh!")
        else:
            self.write("Cookie value : " + cookieValue)

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/secure/", SecureCookieHandler),
], cookie_secret="pyistSecureKeyIsNotSecureAnymore")

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
