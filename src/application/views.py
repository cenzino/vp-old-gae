"""
views.py

URL route handlers

Note that any handler params must match the URL route params.
For example the *say_hello* handler, handling the URL route '/hello/<username>',
  must be passed *username* as the argument.

"""


from google.appengine.api import users
from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError

from flask import render_template, flash, url_for, redirect, request


from models import ExampleModel, Post
from decorators import login_required, admin_required
from forms import ExampleForm, PostForm

from wtforms.ext.appengine.db import model_form
from flaskext.wtf import Form

def home():
    return redirect(url_for('list_posts'))

def say_hello(username):
    """Contrived example to demonstrate Flask's url routing capabilities"""
    return 'Hello %s' % username


def list_examples():
    """List all examples"""
    examples = ExampleModel.all()
    return render_template('list_examples.html', examples=examples)

def list_posts():
    posts = Post.all()
    return render_template('list_posts.html', posts=posts)

def show_post(id):
    post = Post.get_by_id(id)
    return render_template('show_post.html', post=post)
    
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title = form.title.data,
            text = form.text.data,
            text_html = "<pre>" + form.text.data + "</pre>",
            tags = form.tags.data,
        )
        #form.populate_obj(post)
        try:
            post.put()
            flash(u'Post salvato.', 'success')
            return redirect(url_for('list_posts'))
        except CapabilityDisabledError:
            flash(u'App Engine Datastore is currently in read-only mode.', 'failure')
            return redirect(url_for('list_posts'))
    return render_template('new_post.html', form=form)

def edit_post(id):
    post = Post.get_by_id(id)
    form = PostForm(request.form, post)

    if form.validate_on_submit():
        form.populate_obj(post)
        try:
            post.put()
            flash(u'Post aggiornato.', 'success')
            return redirect(url_for('list_posts'))
        except CapabilityDisabledError:
            flash(u'App Engine Datastore is currently in read-only mode.', 'failure')
            return redirect(url_for('list_posts'))
    return render_template('edit_post.html', form=form)
    
@login_required
def new_example():
    """Add a new example, detecting whether or not App Engine is in read-only mode."""
    form = ExampleForm()
    if form.validate_on_submit():
        example = ExampleModel(
                    example_id = form.example_id.data,
                    example_title = form.example_title.data,
                    added_by = users.get_current_user()
                    )
        try:
            example.put()
            flash(u'Example successfully saved.', 'success')
            return redirect(url_for('list_examples'))
        except CapabilityDisabledError:
            flash(u'App Engine Datastore is currently in read-only mode.', 'failure')
            return redirect(url_for('list_examples'))
    return render_template('new_example.html', form=form)


@admin_required
def admin_only():
    """This view requires an admin account"""
    return 'Super-seekrit admin page.'


def warmup():
    """App Engine warmup handler
    See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests

    """
    return ''

