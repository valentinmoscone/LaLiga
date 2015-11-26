from django.shortcuts import render
from google.appengine.ext import db
from laliga.models import User
from laliga.models import Team
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    if request.method == 'POST':
        items = request.POST
        q = User.all()
        q.filter("email =", items['email'] )
        result = q.get()
        if result is None:
            u = User(username=items['username'], email=items['email'])
            u.put()
        return redirect('/home')
    else:
        return render(request,"login.html")


def home(request):
    team = Team.all();
    return render(request, "home.html",{'teams':team})

def team(request, team_name):
    if request.method == 'GET':
        team = Team.all();
        team.filter("name = ", team_name)
        result = team.get()
        return render(request, "team.html",{'teamdetail':result})
    else:
        return render(request,"team.html")
