from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from core.forms import LoginForm
import logging

#-*- coding: UTF-8 -*-

logger = logging.getLogger("django")

def index(request):
    
    form = LoginForm(initial = {'username': 'ruby'})
    context = {"form": form}

    return render(request,"index.html", context)

def login(request):
    logger.debug("sssssss")
    context = {"name": 'ruby'}
    return render(request,"login.html", context)

def detail(request):
    context = {"name": 'ruby'}
#     return HttpResponse("detail")
    return HttpResponseRedirect("/login", context)

def global_context(request):
    context = {'is_login':False}
    return context