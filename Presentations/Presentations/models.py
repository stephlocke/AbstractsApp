import datetime
from flask import Markup
from mongoengine import Document
from mongoengine import DateTimeField, StringField, ReferenceField, ListField, FileField, ImageField
#from flask_appbuilder.security.mongoengine.models import User

class Abstract(Document):
    created_at = DateTimeField(default=datetime.datetime.now, required=True)
    title = StringField(max_length=75, required=True, unique=True)
    shortabstract = StringField(max_length=255,required=True)
    mediumabstract = StringField(max_length=500,required=True)
    longabstract = StringField()
    tags = ListField(ReferenceField('Tag'))
    tracks = ListField(ReferenceField('Track'))

    def __repr__(self):
        return self.title


class Tag(Document):
    created_at = DateTimeField(default=datetime.datetime.now, required=True)
    tag = StringField(verbose_name="Tag", required=True, unique=True)

    def __repr__(self):
        return self.title


class Track(Document):
    created_at = DateTimeField(default=datetime.datetime.now, required=True)
    track = StringField(verbose_name="Track", required=True, unique=True)

    def __repr__(self):
        return self.title
