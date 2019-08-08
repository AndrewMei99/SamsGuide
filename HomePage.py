import webapp2
import jinja2
import os
import logging
import time
from google.appengine.ext import ndb

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
class CoordsRequest(ndb.Model):
    lat = ndb.StringProperty(required = True)
    lon = ndb.StringProperty(required = True)
    timestamp = ndb.DateTimeProperty(auto_now_add = True)

class AddressRequest(ndb.Model):
    address = ndb.StringProperty(required = True)
    timestamp = ndb.DateTimeProperty(auto_now_add = True)
    
    
class MainHandler(webapp2.RequestHandler):
    def get(self):
        home_template = the_jinja_env.get_template('HomePage.html')
        self.response.write(home_template.render())
class AlcoholDrugCounceling(webapp2.RequestHandler):
    def get(self):
        alcohol_template = the_jinja_env.get_template("alcohol.html")
        self.response.write(alcohol_template.render())
    
    
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/AlcoholDrugCounceling', AlcoholDrugCounceling),
], debug=True)