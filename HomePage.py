import webapp2
import jinja2
import os
import logging 

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
    
class SearchResult(webapp2.RequestHandler):
    def post(self):
        #results_template = the_jinja_env.get_template('/results.html')
        user_input = self.request.get('search')
        
        
search = ["Drug alcohol", "health care", "child care"]

for i in search:
    if i == user_input:
        self.response.write(results_template)


    

    

    
    
    
    
app = webapp2.WSGIApplication([
    ('/search', EnterInfoHandler),
], debug=True)