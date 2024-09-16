from django.shortcuts import render
from django.http import HttpResponse
from . models import *

# Create your views here.
def dashboard(request):
    return render(request,'superadmin/index.html')

def widgets(request):
    return render(request,'superadmin/widgets.html')

def header(request):
    return render(request,'superadmin/header.html')
