import webapp2
import logging
#Step 1: Import jinja and os
import jinja2
import os

# Step 2: Set up Jinja Environment
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
)

class MainPage (webapp2.RequestHandler):
        def get(self):
            template = jinja_env.get_template('madlibs.html')
            self.response.write(template.render())

        def post(self):
            template_vars = {
                "name": self.request.get("classmate"),
                "pronoun": self.request.get("preferred singular pronoun"),
                "object": self.request.get("noun"),
                "activity": self.request.get("activity"),
            }
            template = jinja_env.get_template('story.html')
            self.response.write(template.render(template_vars))

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
