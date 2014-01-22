from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from core.forms import LoginForm
import logging
from core.models import Member

#-*- coding: UTF-8 -*-

logger = logging.getLogger("django")

def index(request):
    
    form = LoginForm(initial = {'username': 'ruby'})
    context = {"form": form}
    return render(request,"index.html", context)

def login(request):
    
    form = LoginForm(initial = {'username':'ruby'})
    context = {"name": 'ruby', 'form': form}
    return render(request,"login.html", context)

def blogs(request):
    
    context = {}
    return render(request,"blogs.html",context)
def detail(request):
    context = {"name": 'ruby'}
#     return HttpResponse("detail")
    return HttpResponseRedirect("/demo", context)

def demo(request):
    logger.debug("msg")
    
    return HttpResponseRedirect("/")

def logout(request):
    if request.session.has_key("user_id"):
	 del request.session["user_id"]
	
    return HttpResponseRedirect("/")

def global_context(request):
    context = {'is_login':False}
    return context
