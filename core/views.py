from django.shortcuts import render

#-*- coding: UTF-8 -*-

def index(request):
    

    return render(request,"index.html")

def login(request):
    
    return render(request,"login.html")

def global_context(request):
    context = {'is_login':False}
    return context