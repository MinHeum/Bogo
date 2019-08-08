from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'bogo/home.html')

def login(request):
    return render(request, 'bogo/login.html')

@login_required
def addGoods(request):
    return render(request,'bogo/add.html')