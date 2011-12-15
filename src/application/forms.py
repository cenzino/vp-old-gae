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
#PostForm = model_form(Post, wtf.Form)

class TagListField(wtf.TextField):
    widget = wtf.TextInput()

    def _value(self):
        if self.data:
            return u', '.join(self.data)
        else:
            return u''

    def process_formdata(self, valuelist):
        self.data = []
        if valuelist:
            """
            self.data = [x.strip() for x in valuelist[0].split(',')]
            """
            for x in valuelist[0].split(','):
                x = x.strip()
                if not x == '':
                    self.data.append(x)

class BetterTagListField(TagListField):
    def __init__(self, label='', validators=None, remove_duplicates=True, **kwargs):
        super(BetterTagListField, self).__init__(label, validators, **kwargs)
        self.remove_duplicates = remove_duplicates

    def process_formdata(self, valuelist):
        super(BetterTagListField, self).process_formdata(valuelist)
        if self.remove_duplicates:
            self.data = list(self._remove_duplicates(self.data))

    @classmethod
    def _remove_duplicates(cls, seq):
        """Remove duplicates in a case insensitive, but case preserving manner"""
        d = {}
        for item in seq:
            if item.lower() not in d:
                d[item.lower()] = True
                yield item


class PostForm(wtf.Form):
    title = wtf.TextField('Title', validators=[validators.Required()])
    text = wtf.TextAreaField('Text', validators=[validators.Required()])
    tags = BetterTagListField()