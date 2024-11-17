from django.shortcuts import render,redirect
from django.http import HttpResponse
from backend.models import *
from app.models import *
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
import random


# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def course(request):
    return render(request,'course.html')

def table(request):
    title='table'
    custdata=Customer.objects.all()
    return render(request,'table.html',{'title':title,'custdata':custdata})


def login(request):
    title='login'
    if request.method=="POST":
        email_address=request.POST['email_address']
        password=request.POST['password']
        if Customer.objects.filter(email=email_address,password=password).exists():
            subject ='login'
            message ='you are successfully login'
            from_user =settings.EMAIL_HOST_USER
            send_mail(subject,message,from_user,[email_address])
            return HttpResponse("login successful")
        else:
            return HttpResponse("wrong credentials")
    return render(request,'login.html',{'title':title}) 


def logout(request):
    del request.session['cust_id']
    del request.session['cust_name']
    messages.add_messages(request,messages.SUCCESS,'logout success')
            
        


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
        image=request.FILES['image']
        checkbox=request.POST['checkbox']
        cust=Customer.objects.filter(email=email).first()
        # return HttpResponse(cust)
        if cust is None:
            Customer.objects.create(first_name=first_name,last_name=last_name,email=email,password=password,permanent_address=permanent_address,residincial_address=residincial_address,number=number,city=city,state=state,image=image,checkbox=checkbox)
            subject ='register'
            message ='register otp' + str(random.randint(0000,9999))
            from_user =settings.EMAIL_HOST_USER
            send_mail(subject,message,from_user,[email])
            return HttpResponse('registered success')
        else:
            return HttpResponse("profile  is already exists")
        # return HttpResponse('registered success')
    return render(request,'signup.html',{'title':title})


def edit(request,id):
    title='edit in registration'
    cust=Customer.objects.get(id=id)
    if request.method == "POST":
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
        cust.first_name=first_name
        cust.last_name=last_name
        cust.email=email
        cust.password=password
        cust.permanent_address=permanent_address
        cust.residincial_address=residincial_address
        cust.number=number
        cust.city=city
        cust.state=state
        cust.checkbox=checkbox
        cust.save()
        messages.add_message(request,messages.SUCCESS,"edit successfully")
        return redirect('table')

    return render(request,'edit.html',{'title':title,'cust':cust})


def delete(request,id):
    cust=Customer.objects.get(id=id)
    cust.save()
    messages.add_message(request,messages.SUCCESS,'delete successfully')
    return redirect('table')


def free_read(request):
    title='read for free'
    main_image = freeread_db.objects.filter(status=True)
    title=freeread_db.objects.filter(status=True)
    return render(request,'free_read.html',{'title':title,'main_image':main_image})


