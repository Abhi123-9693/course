from django.shortcuts import render
from django.http import HttpResponse
from . models import *


# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    title='login'
    
    return render(request,'login.html')

def about(request):
    return render(request,'about.html')

def signup(request):
    title='signup'
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        permanent_address=request.POST['permanent_address']
        residincial_address=request.POST['residincial_address']
        number=request.POST['number']
        city=request.POST['city']
        state=request.POST['state']
        checkbox=request.POST['checkbox']
        cust=Customer.objects.filter(number=number,email=email).first()
        # return HttpResponse(cust)
        if cust is None:
            Customer.objects.create(first_name=first_name,last_name=last_name,email=email,password=password,permanent_address=permanent_address,residincial_address=residincial_address,number=number,city=city,state=state,checkbox=checkbox)
        else:
            return HttpResponse("profile  is already exists")
        return HttpResponse('registered success')
    return render(request,'signup.html',{'title':title})

