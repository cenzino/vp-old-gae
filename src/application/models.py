"""
models.py

App Engine datastore models

"""


from google.appengine.ext import db

#from libs import md2html
import markdown

class ExampleModel(db.Model):
    """Example Model"""
    example_id = db.StringProperty(required=True)
    example_title = db.StringProperty(required=True)
    added_by = db.UserProperty()
    timestamp = db.DateTimeProperty(auto_now_add=True)

class Post(db.Model):
    title = db.StringProperty(required=True)

    text = db.TextProperty()
    text_html = db.TextProperty()

    tags = db.StringListProperty(db.Category)

    published = db.DateTimeProperty(auto_now_add=True)
    updated = db.DateTimeProperty(auto_now=True)

    @property
    def id(self):
        return self.key().id()

    def save(self):
        self.text_html = markdown.markdown(self.text, ['codehilite'])
        #self.put()
        super(Post, self).put()