from django.shortcuts import render

def home(request):
    return render(request, 'base/home.html')

def wait(request):
    return render(request, 'base/wait.html')

def login(request):
    return render(request, 'base/login.html')

def privacy(request):
    return render(request, 'base/privacy.html')