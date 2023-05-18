from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request, 'register.html')

def open(request):
    return render(request, 'open.html')

def edit(request):
    return render(request, 'edit.html')