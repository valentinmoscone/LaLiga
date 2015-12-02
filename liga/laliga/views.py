#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
from django.shortcuts import render
from django.http import HttpResponseNotFound
from google.appengine.ext import db
from laliga.models import User
from laliga.models import Team
from laliga.models import Player
from laliga.models import Testing
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from google.appengine.api import users
from google.appengine.api import mail



@csrf_exempt
def login(request):
    if request.method == 'GET':
        user = users.get_current_user()
        if user:
            username = user.nickname()
            allusers = User.all()
            allusers.filter("email = ", user.email())
            result = allusers.get()
            if result is None:
                u = User(nickname = user.nickname(), email = user.email(), username = "", team = "")
                u.put()
            team = Team.all()
            return render(request,"home.html",{'teams': team, 'user': result})
        else:
            return redirect(users.create_login_url("/"))
    else:
        return redirect("https://www.google.com")


def user_logout(request):
    return redirect(users.create_logout_url("/"))


def home(request):
    if request.method == 'GET':
        user = users.get_current_user()
        if user:
            allusers = User.all()
            allusers.filter("email = ", user.email())
            result = allusers.get()
            if result is None:
                return redirect(users.create_login_url("/"))
            else:
                team = Team.all()
                return render(request,"home.html",{'teams': team, 'user': result})
        else:
            return redirect(users.create_login_url("/"))
    else:
        return redirect("https://www.google.com")

def team(request, team_name):
    if request.method == 'GET':
        user = users.get_current_user()
        if user:
            allusers = User.all()
            allusers.filter("email =", user.email())
            result = allusers.get()
            if result is None:
                return redirect(users.create_login_url("/"))
            else:
                team = Team.all()
                team.filter("name = ", team_name)
                resultteam = team.get()
                if resultteam is None:
                    return HttpResponseNotFound('<h1>404 Page not found</h1>')
                players = Player.all()
                players.filter("teamPlayer = ", team_name)
                return render(request, "team.html",{'teamdetail':resultteam,'playerdetail':players, 'user': result})
        else:
            return redirect(users.create_login_url("/"))
    else:
        return redirect("https://www.google.com")

@csrf_exempt
def contact(request):
    if request.method == 'GET':
        user = users.get_current_user()
        if user:
            allusers = User.all()
            allusers.filter("email =", user.email())
            result = allusers.get()
            if result is None:
                return redirect(users.create_login_url("/"))
            else:
                return render(request,"contact.html", {'user': result})
        else:
            return redirect(users.create_login_url("/"))
    if request.method == 'POST':
        user = users.get_current_user()
        if user:
            allusers = User.all()
            allusers.filter("email =", user.email())
            result = allusers.get()
            if result is None:
                return redirect(users.create_login_url("/"))
            else:
                message = mail.EmailMessage(sender=user.email(),
                            subject="Comentario")

                message.to = "<jota.blanco91@gmail.com>;<valentin.moscone@gmail.com>"
                message.body = request.POST.get("mailbody","")
                message.send()
                return render(request,"contact.html", {'user': result})
        else:
            return redirect(users.create_login_url("/"))
        
@csrf_exempt 
def profile(request):
    if request.method == 'GET':
        user = users.get_current_user()
        if user:
            allusers = User.all()
            allusers.filter("email =", user.email())
            result = allusers.get()
            if result is None:
                return redirect(users.create_login_url("/"))
            else:
                teams = Team.all()
                return render(request,"profile.html",{'userprofile': result, 'teams': teams})
        else:
            return redirect(users.create_login_url("/"))
    if request.method == 'POST':
        user = users.get_current_user()
        if user:
            allusers = User.all()
            allusers.filter("email =", user.email())
            result = allusers.get()
            if result is None:
                return redirect(users.create_login_url("/"))
            else:
                result.username = request.POST['username']
                result.age = request.POST['age']
                result.team = request.POST['team']
                result.put()
                return render(request, "profile.html",{'userprofile': result})
    return redirect(users.create_login_url("/"))

@csrf_exempt 
def setting(request):
    if request.method == 'GET':
        user = users.get_current_user()
        if user:
            allusers = User.all()
            allusers.filter("email =", user.email())
            result = allusers.get()
            if result is None:
                return redirect(users.create_login_url("/"))
            else:
                return render(request,"setting.html",{'user': result})
        else:
            return redirect(users.create_login_url("/"))
    if request.method == 'POST':
        user = users.get_current_user()
        if user:
            allusers = User.all()
            allusers.filter("email =", user.email())
            result = allusers.get()
            if result is None:
                return redirect(users.create_login_url("/"))
            else:
                result.delete()
                return redirect(users.create_logout_url("/"))
    return redirect(users.create_login_url("/"))
    
def testdata(request):
    if request.method == 'GET':
        test = Testing.all()
        result = test.get()
        if result is None:
            t = Testing(data = True)
            t.put()
            t1 = Team(name=u'Nacional', points=24, goalsScored=25, goalsAgainst=4, imageUrl= "https://upload.wikimedia.org/wikipedia/commons/1/1e/Club_Nacional_de_Football's_logo.png", lat = -34.8943868, lon = -56.1528241)
            t1.put()
            t2 = Team(name=u'Peñarol', points=27, goalsScored=32, goalsAgainst=10, imageUrl= "https://upload.wikimedia.org/wikipedia/commons/2/26/Escudo-club-atletico-penarol.png", lat = -34.8943868, lon = -56.1528241)
            t2.put()
            t3 = Team(name="Cerro", points=22, goalsScored=20, goalsAgainst=10, imageUrl= u'https://upload.wikimedia.org/wikipedia/commons/6/60/Escudo_Club_Atlético_Cerro.png', lat = -34.8943868, lon = -56.1528241)
            t3.put()
            t4 = Team(name="Defensor", points=20, goalsScored=10, goalsAgainst=14, imageUrl= "https://upload.wikimedia.org/wikipedia/commons/c/c4/Escudo_Defensor_Sporting_Club.png", lat = -34.8943868, lon = -56.1528241)
            t4.put()
            t5 = Team(name="Danubio", points=17, goalsScored=17, goalsAgainst=6, imageUrl= u'https://upload.wikimedia.org/wikipedia/commons/5/5e/Escudo_Danubio_Fútbol_Club.png', lat = -34.8943868, lon = -56.1528241)
            t5.put()
            t6 = Team(name="Wanderes", points=17, goalsScored=13, goalsAgainst=10, imageUrl= "https://upload.wikimedia.org/wikipedia/commons/e/e8/Escudo_Montevideo_Wanderers_FC.png", lat = -34.8943868, lon = -56.1528241)
            t6.put()
            t7 = Team(name="Fenix", points=16, goalsScored=5, goalsAgainst=10, imageUrl= u'https://upload.wikimedia.org/wikipedia/en/d/de/CA_Fenix.png', lat = -34.8943868, lon = -56.1528241)
            t7.put()
            t8 = Team(name="Rentistas", points=13, goalsScored=6, goalsAgainst=17, imageUrl= u'https://upload.wikimedia.org/wikipedia/commons/6/62/Escudo_Club_Atlético_Rentistas.gif', lat = -34.8943868, lon = -56.1528241)
            t8.put()
            t9 = Team(name="River", points=13, goalsScored=5, goalsAgainst=20, imageUrl= u'https://upload.wikimedia.org/wikipedia/commons/8/8a/Escudo_Club_Atlético_River_Plate.png', lat = -34.8943868, lon = -56.1528241)
            t9.put()
            p1 = Player(name="Juan", number=1, position="Golero", teamPlayer="Nacional")
            p1.put()
            p2 = Player(name="Pedro", number=2, position="Defensa", teamPlayer="Nacional")
            p2.put()
            p3 = Player(name="Federico", number=5, position="Defensa", teamPlayer="Nacional")
            p3.put()
            p4 = Player(name="Alberto", number=3, position="Defensa", teamPlayer="Nacional")
            p4.put()
            p5 = Player(name="Nacho", number=13, position="Medio", teamPlayer="Nacional")
            p5.put()
            p6 = Player(name="Matias", number=15, position="Medio", teamPlayer="Nacional")
            p6.put()
            p7 = Player(name="Valentin", number=10, position="Medio", teamPlayer="Nacional")
            p7.put()
            p8 = Player(name="Alfredo", number=9, position="Delantero", teamPlayer="Nacional")
            p8.put()
    return render(request,"testdata.html")

