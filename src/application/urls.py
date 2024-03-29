"""
urls.py

URL dispatch route mappings and error handlers

"""

from flask import render_template

from application import app
from application import views


## URL dispatch rules
# App Engine warm up handler
# See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests
app.add_url_rule('/_ah/warmup', 'warmup', view_func=views.warmup)

# Home page
app.add_url_rule('/', 'home', view_func=views.home)

# Say hello
app.add_url_rule('/hello/<username>', 'say_hello', view_func=views.say_hello)

# Examples list page
app.add_url_rule('/examples', 'list_examples', view_func=views.list_examples)

# Add new example via web form
app.add_url_rule('/example/new', 'new_example', view_func=views.new_example, methods=['GET', 'POST'])

# Contrived admin-only view example
app.add_url_rule('/admin_only', 'admin_only', view_func=views.admin_only)

# Posts list page
app.add_url_rule('/blog', 'list_posts', view_func=views.list_posts)

# Add new example via web form
app.add_url_rule('/blog/new', 'new_post', view_func=views.new_post, methods=['GET', 'POST'])

app.add_url_rule('/blog/post/<int:id>', 'show_post', view_func=views.show_post)
app.add_url_rule('/blog/post/edit/<int:id>', 'edit_post', view_func=views.edit_post, methods=['POST','GET'])
app.add_url_rule('/blog/post/delete/<int:id>', 'delete_post', view_func=views.delete_post, methods=['GET'])
app.add_url_rule('/blog/category/<tag>', 'show_category', view_func=views.show_category, methods=['GET', 'POST'])

app.add_url_rule('/pygments.css', 'pygments_css', view_func=views.pygments_css)
app.add_url_rule('/md', 'md', view_func=views.md)

## Error handlers
# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

