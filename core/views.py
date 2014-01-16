from django.shortcuts import render


def index(request):
    

    return render(request,"index.html")

def global_context(request):
    context = {'is_login':False}
    return context