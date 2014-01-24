from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from core.forms import LoginForm, BlogForm
import logging
from core.models import Blog
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib import messages

#-*- coding: UTF-8 -*-

logger = logging.getLogger("django")

def index(request):

    form = {}
    context = {"form": form}
    return render(request,"index.html", context)

def login(request):
    if request.session.has_key("user_id") and request.session["user_id"] is not "":
        return HttpResponseRedirect("/")
    
    form = LoginForm(initial = {'username':''})
    context = { 'name': 'ruby',  'form': form}
    flag = -1
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            flag = form.login(request)
        else:
            flag = 3
            messages.info(request, "Form is invalid")
    if flag == 1:
        messages.info(request, "username or password is wrong")
    if flag == 2 or flag == 0:
        return HttpResponseRedirect("/")
    else:
        return render(request,"login.html", context)

def blogs(request):
    items = Blog.objects.filter(status=1)
    paginator = Paginator(items, 2)
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1
    try:
        blogs = paginator.page(page)
    except (EmptyPage, InvalidPage):
        blogs = paginator.page(paginator.num_pages)
    
    context = {'blogs':blogs}
    return render(request,"blogs.html",context)

def new_blog(request):
    if not (request.session.has_key("user_id") and request.session["user_id"] is not ""):
        return HttpResponseRedirect("/")
    
    context = {'form': BlogForm(initial = {'title':'input the title'})}
    flag = -1 
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            flag = form.save(request)
        else:
            flag = 0
    if flag == 1:
        return HttpResponseRedirect("/blogs")
    return render(request,"new_blog.html", context)

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
    
    is_login = False
    if request.session.has_key('user_id'):
        if request.session['user_id'] is not "" :
            is_login = True
        else:
            is_login = False
    context = {'is_login':is_login}
    return context
