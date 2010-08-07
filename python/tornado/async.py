#!/usr/bin/python
# demonstrate async http client on tornadoweb
# this will request to eksigator api and return async result

import tornado.httpserver
import tornado.httpclient
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        url = "http://api.eksigator.com/demo/demo/getList"
        http.fetch(url, callback=self.async_callback(self.on_response))

    def on_response(self, response):
        items = tornado.escape.json_decode(response.body)
        for item in items:
            self.write( item["title"] + "<br/>" )

        # this will end async requst
        self.finish()
        

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
