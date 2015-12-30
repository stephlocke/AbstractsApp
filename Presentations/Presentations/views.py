"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Presentations import app, appbuilder

from flask_appbuilder.models.mongoengine.interface import MongoEngineInterface
from flask_appbuilder import ModelView


from .models import Abstract, Tag, Track

class AbstractModelView(ModelView):
    datamodel=MongoEngineInterface(Abstract)
    base_permissions = ['can_show','can_list']

class TagModelView(ModelView):
    datamodel=MongoEngineInterface(Tag)
    related_views = [AbstractModelView]
    base_permissions = ['can_show','can_list']

class TrackModelView(ModelView):
    datamodel=MongoEngineInterface(Track)
    related_views = [AbstractModelView]
    base_permissions = ['can_show','can_list']

appbuilder.add_view(AbstractModelView, "Abstracts", icon="fa-folder-open-o", category="Sessions", category_icon='fa-envelope')
appbuilder.add_view(TagModelView, "Tags", icon="fa-folder-open-o", category="Sessions", category_icon='fa-envelope')
appbuilder.add_view(TrackModelView, "Tracks", icon="fa-folder-open-o", category="Sessions", category_icon='fa-envelope')

appbuilder.security_cleanup()

#@app.route('/')
#@app.route('/home')
#def home():
#    """Renders the home page."""
#    return render_template(
#        'index.html',
#        title='Home Page',
#        year=datetime.now().year,
#    )

#@app.route('/contact')
#def contact():
#    """Renders the contact page."""
#    return render_template(
#        'contact.html',
#        title='Contact',
#        year=datetime.now().year,
#        message='Your contact page.'
#    )

#@app.route('/about')
#def about():
#    """Renders the about page."""
#    return render_template(
#        'about.html',
#        title='About',
#        year=datetime.now().year,
#        message='Your application description page.'
#    )
