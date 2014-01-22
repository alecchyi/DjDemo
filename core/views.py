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
#     teacher = {'user_name': "teacher_01", 'passwd': '123456'}
#     m = Member()
#     m.username= 'asdf'
#     m.password = 'qwer'
#     m.save()
    return render(request,"index.html", context)

def login(request):
    logger.debug("sssssss")
    context = {"name": 'ruby'}
    return render(request,"login.html", context)

def detail(request):
    context = {"name": 'ruby'}
#     return HttpResponse("detail")
    return HttpResponseRedirect("/demo", context)

def demo(request):
    logger.debug("msg")
    
    return HttpResponseRedirect("/")
def global_context(request):
    context = {'is_login':False}
    return context