#!/usr/bin/env python
# Demonstrationg template usage of tornadoweb

import tornado.httpserver
import tornado.ioloop
import tornado.web

# handles main page 
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #we demonstrate this using a ?userLogged=userName parameter
        switchLoggedFromGet = self.get_argument("userLogged", False)
        self.render("templates/main.html", title="Pyist.net", userLogged=switchLoggedFromGet)

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
