from django.db import models
from google.appengine.ext import db
from google.appengine.api import users
import webapp2 
# Create your models here.

class User(db.Model):
    username = db.StringProperty(required = True)
    email = db.StringProperty(required = True)
    
meta = {
    'indexes': [
        'username',
        'email'
    ]
}

class Team(db.Model):
    name = db.StringProperty(required = True)
    points = db.IntegerProperty(required = True)
    goalsScored = db.IntegerProperty(required = True)
    goalsAgainst = db.IntegerProperty(required = True)
    imageUrl = db.StringProperty(required = True)

meta = {
    'indexes': [
        'name',
        'imageUrl'
    ]
}