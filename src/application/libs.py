import markdown
from flask import Markup

def md2html(text):
    try:
        import pygments
    except ImportError:
        extensions = []
    else:
        extensions = ['codehilite']
    html = Markup(markdown.markdown(text, extensions))
    return html