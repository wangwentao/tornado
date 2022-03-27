import tornado.ioloop
import tornado.web

from handler.HelloHandler import MainHandler


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler)
    ],
        debug=True
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8880)
    tornado.ioloop.IOLoop.current().start()
