#!/usr/bin/env python
# Demonstrationg request handling of tornado web

import tornado.httpserver
import tornado.ioloop
import tornado.web

# handles main page 
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hi this is web page")

# handles pages matches URI /another/someUriParam
class AnotherHandler(tornado.web.RequestHandler):
    def get(self,uriParam):
        self.write("This is another page with URI parameter = " + uriParam)


# handles pages matches /postTest/ and demonstrate getting request parameter
class PostSomethingHandler(tornado.web.RequestHandler):
    def get(self):
        form = """<form method="post">
        <input type="text" name="something"/>
        <input type="submit"/>
        </form>"""
        self.write(form)

    def post(self):
        postedValue = self.get_argument("something") # get request argument
        self.write("You've postted 'something' as : " + postedValue)


# demonstrates an HTTP response error
class ResponseErrorHandler(tornado.web.RequestHandler):
    def get(self):
        # send a 403 forbidden error
        raise tornado.web.HTTPError(403)


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/another/([^/]+)", AnotherHandler),
    (r"/postTest/", PostSomethingHandler),
    (r"/someError/", ResponseErrorHandler),
])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
