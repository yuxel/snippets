#!/usr/bin/env python
# Demonstrationg translation/locale usage of tornadoweb

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.locale
import os

# Turkish page
class TRHandler(tornado.web.RequestHandler):
    def get(self):
        tornado.locale.set_default_locale('tr_TR')
        self.render("templates/translation.html")

# English page
class ENHandler(tornado.web.RequestHandler):
    def get(self):
        tornado.locale.set_default_locale('en_US')
        self.render("templates/translation.html")


application = tornado.web.Application([
    (r"/tr/", TRHandler),
    (r"/en/", ENHandler),
])

if __name__ == "__main__":
    #set path for location dir
 
    translationsPath = os.path.join(os.path.dirname(__file__), "translations")  
    tornado.locale.load_translations(translationsPath)

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)

    tornado.ioloop.IOLoop.instance().start()
