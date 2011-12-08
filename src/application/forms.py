"""
forms.py

Web forms based on Flask-WTForms

See: http://flask.pocoo.org/docs/patterns/wtforms/
     http://wtforms.simplecodes.com/

"""

from flaskext import wtf
from flaskext.wtf import validators
from wtforms.ext.appengine.db import model_form

class ExampleForm(wtf.Form):
    example_id = wtf.TextField('Example ID', validators=[validators.Required()])
    example_title = wtf.TextField('Example Title', validators=[validators.Required()])

from models import Post
PostForm = model_form(Post, wtf.Form)
    