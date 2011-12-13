import markdown
from flask import Markup

from jinja2 import Environment, PackageLoader

env = Environment()

def md2html(text):
    try:
        import pygments
    except ImportError:
        extensions = []
    else:
        extensions = ['codehilite']
    html = Markup(markdown.markdown(text, extensions))
    return html
    
def format_datetime(value, format='%H:%M / %d-%m-%Y'):
    return value.strftime(format)
    
env.filters['datetime'] = format_datetime
