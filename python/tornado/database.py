#!/usr/bin/python
# demonstrates database usage of tornadoweb

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.database

class DBHandler(tornado.web.RequestHandler):
    def get(self):
        db = tornado.database.Connection(
            host="localhost", database="pyist",
            user="root", password="12345678")

        datas = db.query("select name_surname from pyist")

        # print datas
        for data in datas:
            self.write(data["name_surname"])
            self.write("<br/>")


application = tornado.web.Application([
    (r"/", DBHandler),
])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
