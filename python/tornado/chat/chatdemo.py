#!/usr/bin/env python

import tornado.auth
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.web
import os.path
import time
import uuid


# uri handlers
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/new", MessageNewHandler),
            (r"/updates", MessageUpdatesHandler),
        ]
        settings = {
            "template_path": os.path.join(os.path.dirname(__file__), "templates"),
            "static_path" :os.path.join(os.path.dirname(__file__), "static"),
        }

        tornado.web.Application.__init__(self, handlers, **settings)

# render main template
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # assign current cache to template
        self.render("index.html", messages=MessageMixin.cache)

class MessageMixin(object):
    waiters = []  
    cache = [] # message cache
    cache_size = 2

    def wait_for_messages(self, callback, cursor=None):
        #print "waiting for message"
        cls = MessageMixin
        if cursor:
            index = 0

            # move to current cursor
            for i in xrange(len(cls.cache)):
                index = len(cls.cache) - i - 1
                if cls.cache[index]["id"] == cursor: break

            recent = cls.cache[index + 1:] #new current cursor

            if recent:
                callback(recent)
                return

        cls.waiters.append(callback)

    def new_messages(self, messages):
        cls = MessageMixin
        print "Sending new message to ", len(cls.waiters), " listeners"

        for callback in cls.waiters:
            try:
                #print "sending this message to waiters"
                #print messages
                callback(messages)
            except:
                print "Error in waiter callback"

        cls.waiters = [] #reset waiters

        cls.cache.extend(messages)

        # control for max cache size
        if len(cls.cache) > self.cache_size:
            cls.cache = cls.cache[-self.cache_size:]

class MessageNewHandler(tornado.web.RequestHandler, MessageMixin):
    def post(self):
        message = {
            "id": str(uuid.uuid4()),
            "from": self.get_argument("from","Pyist"),
            "body": self.get_argument("body"),
        }

        message["html"] = self.render_string("message.html", message=message)

        if self.get_argument("next", None):
            self.redirect(self.get_argument("next"))
        else:
            self.write(message)

        self.new_messages([message])

class MessageUpdatesHandler(tornado.web.RequestHandler, MessageMixin):
    @tornado.web.asynchronous
    def get(self):
        cursor = self.get_argument("cursor", None)
        self.wait_for_messages(self.async_callback(self.on_messages_updated),
                               cursor=cursor)

    def on_messages_updated(self, messages):
        if self.request.connection.stream.closed():
            return
        #self.finish(dict(messages=messages))
        self.finish({"messages":messages})


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
