#!/usr/bin/env python
# Demonstrationg XSRF protection of tornado

import tornado.httpserver
import tornado.ioloop
import tornado.web

# handles main page 
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/xsrf.html")

    # if _xsrf value doesnt match xsrf cookie value, this will return 403
    def post(self):
        postedValue = self.get_argument("something") # get request argument
        self.write("You've postted 'something' as : " + postedValue)

application = tornado.web.Application([
    (r"/", MainHandler),
], cookie_secret="SomeSecret",xsrf_cookies=True)

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
