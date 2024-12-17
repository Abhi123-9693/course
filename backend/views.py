from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from django.contrib import messages

# Create your views here.
def dashboard(request):
    return render(request,'superadmin/index.html')

def add_product(request):
    title='add product'
    main_product =Product_db.objects.filter(status=True)
    if request.method=="POST":
        pname=request.POST['pname']
        pbrand=request.POST['pbrand']
        pprice=request.POST['pprice']
        psellprice=request.POST['psellprice']
        pdiscount=request.POST['pdiscount']
        pimage=request.FILES['pimage']
        Product_db.objects.create(pname=pname,pbrand=pbrand,pprice=pprice,psellprice=psellprice,pdiscount=pdiscount,pimage=pimage)
        messages.success(request,'image saved successfull')


    return render(request,'superadmin/add_product.html',{'title':title,'main_product':main_product})

def product_list(request):
    return render(request,'superadmin/product_list.html')

def freeread(request):
    main_image =freeread_db.objects.filter(status=True)
    title=freeread_db.objects.filter(status=True)

    if request.method =="POST":
        img=request.FILES['img']
        title=request.POST['title']
        des=request.POST['des']
        freeread_db.objects.create(img=img,des=des,title=title)
        # return HttpResponse('image added successfull')
        messages.success(request,'image saved successfull')

    return render(request,'superadmin/freeread.html',{'main_image':main_image,'title':title})

def del_freeread(request,id):
    freeread_db.objects.filter(id=id).update(status=False)
    messages.success(request,'card delete successfull')
    return render(request,'superadmin/freeread.html')

def add_carasoulVv(request):
    carasoul =carasoul_DB.objects.filter(status=True)

    if request.method =="POST":
        img1=request.FILES['img1']

        carasoul_DB.objects.create(img1=img1)

        messages.success(request,'image saved successfull')

    return render(request,'superadmin/add_carasoul.html',{"carasoul":carasoul})



# card management
def card_mng(request):
    cardmng =Cardmng_DB.objects.filter(status=True)
    title='card management'
    if request.method =="POST":
        Cimg=request.FILES['Cimg']
        Ctitle=request.POST['Ctitle']
        Cdesc=request.POST['Cdesc']

        Cardmng_DB.objects.create(Cimg=Cimg,Ctitle=Ctitle,Cdesc=Cdesc)

        messages.success(request,'image saved successfull')

    return render(request,'superadmin/card_mng.html',{'cardmng':cardmng,'title':title})


# delete card management

def del_cardmng(request,id):
    Cardmng_DB.objects.filter(id=id).update(status=False)
    messages.success(request,'card delete successfull')
    return render(request,'superadmin/card_mng.html')


