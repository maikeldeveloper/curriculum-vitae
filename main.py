import webapp2
import os
import jinja2
from src.urls import pages
jinja_enviroment = jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

class AppPage(webapp2.RequestHandler):

    def get(self):
        request_path = self.request.path if self.request.path.endswith('/') else self.request.path + '/'
        if request_path in pages:
            template = jinja_enviroment.get_template(pages[request_path]['template'])
            self.response.write(template.render(pages[request_path]['data']))



app = webapp2.WSGIApplication([
    ('/.*', AppPage)

], debug=True)
