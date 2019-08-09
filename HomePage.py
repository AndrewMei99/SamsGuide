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
        myDict = {
            'address_from_python_dict':'1015 Cass Street, Suite #4; Monterey, CA 93940 9 West Gabilan Street #11; Salinas, Ca 93901 130 W. Gabilan Street; Salinas, CA 93901 411 Central Avenue; Salinas, CA 93901 128 East Alisal Street; Salinas, CA 93905 855 E. Laural Drive, Bldg H; Salinas, CA 93906 1760 Fremon Blvd., Suite E1; Seaside, CA 93955 133 Fourth Street Suite C; Gonzalez, CA 93926'
        }
        alcohol_template = the_jinja_env.get_template("alcohol.html")
        self.response.write(alcohol_template.render(myDict))
class DomesticViolence(webapp2.RequestHandler):
    def get(self):
        DomDict = {
            'DomesticAdresses':'142 W. Alisal Street; Salinas, CA 93901 1441 Constitution Blvd.; Salinas, CA 93906 20 East Alisal, Salinas, CA 93905 236 Monterey Street; Salinas, CA 93901 433 Salinas Street; Salinas, CA 93901 1178 Broadway; Seaside, CA 93955 3785 Via Nona Marie, Carmel, CA 93923'
        }
        domestic_template = the_jinja_env.get_template('domestic.html')
        self.response.write(domestic_template.render(DomDict))
class ChildProtectives(webapp2.RequestHandler):
    def get(self):
        child_template = the_jinja_env.get_template('child.html')
        self.response.write(child_template.render())
class HealthCareServices(webapp2.RequestHandler):
    def get(self):
        health_template = the_jinja_env.get_template('healthcare.html')
        self.response.write(health_template.render())
class FoodDistribution(webapp2.RequestHandler):
    def get(self):
        food_template = the_jinja_env.get_template('food.html')
        self.response.write(food_template.render())
        
        
    
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/AlcoholDrugCounceling', AlcoholDrugCounceling),
    ('/DomesticViolence', DomesticViolence),
    ('/ChildProtectives', ChildProtectives), 
    ('/HealthCareServices', HealthCareServices),
    ('/FoodDistribution', FoodDistribution),
], debug=True)