from django.db import models
from google.appengine.ext import db
from google.appengine.api import users
import webapp2 
# Create your models here.

class User(db.Model):
    username = db.StringProperty()
    nickname = db.StringProperty(required = True)
    age = db.StringProperty()
    email = db.StringProperty(required = True)
    team = db.StringProperty()
    
meta = {
    'indexes': [
        'nickname',
        'email'
    ]
}

class Team(db.Model):
    name = db.StringProperty(required = True)
    points = db.IntegerProperty(required = True)
    goalsScored = db.IntegerProperty(required = True)
    goalsAgainst = db.IntegerProperty(required = True)
    imageUrl = db.StringProperty(required = True)
    lat = db.FloatProperty(required = True)
    lon = db.FloatProperty(required = True)

meta = {
    'indexes': [
        'name',
        'imageUrl'
    ]
}

class Player(db.Model):
    name = db.StringProperty(required = True)
    number = db.IntegerProperty (required = True)
    position = db.StringProperty (required = True)
    teamPlayer = db.StringProperty (required = True)

meta = {
    'indexes': [
        'name',
        'team'
    ]
}

class Testing(db.Model):
    data = db.BooleanProperty(required = True)