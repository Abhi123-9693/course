from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from django.contrib import messages

# Create your views here.
def dashboard(request):
    return render(request,'superadmin/index.html')

def add_product(request):
    title='add product'
    if request.method=="POST":
        pname=request.POST['pname']
        pbrand=request.POST['pbrand']
        pprice=request.POST['pprice']
        psellprice=request.POST['psellprice']
        pdiscount=request.POST['pdiscount']
        pimage=request.FILES['pimage']
        Product.objects.create(pname=pname,pbrand=pbrand,pprice=pprice,psellprice=psellprice,pdiscount=pdiscount,pimage=pimage,)


    return render(request,'superadmin/add_product.html',{'title':title})

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
        return HttpResponse('image added successfull')

    return render(request,'superadmin/freeread.html',{'main_image':main_image,'title':title})

def del_freeread(request,id):
    freeread_db.objects.filter(id=id).update(status=False)
    messages.success(request,'card delete successfull')
    return render(request,'superadmin/freeread.html')


