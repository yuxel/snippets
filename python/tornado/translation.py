#!/usr/bin/env python
# Demonstrationg translation/locale usage of tornadoweb

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.locale
import os

# handles main page 
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/translation.html")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":

    #tornado.locale.set_default_locale('tr_TR')
    
    #set path for location dir
    tornado.locale.load_translations(os.path.join(os.path.dirname(__file__),                                                                                       "translations"))


    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
tornado.ioloop.IOLoop.instance().start()
