from tornado.web import RequestHandler


class IndexHandler(RequestHandler):

    def get(self):
        return self.render("../templates/index.html")
#        self.write("Hello, World")
