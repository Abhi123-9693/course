from django.db import models

# Create your models here.
class Product_db(models.Model):
    pname=models.CharField(max_length=225)
    pbrand=models.CharField(max_length=225)
    pprice=models.IntegerField(max_length=225)
    psellprice=models.IntegerField(max_length=225)
    pdiscount=models.IntegerField(max_length=225)
    pimage=models.ImageField(default=None,null=True,blank=True,upload_to='img')
    status=models.BooleanField(default=True)

class freeread_db(models.Model):
    img=models.ImageField(upload_to='main_image',default='')
    title=models.CharField(max_length=50,default='')
    des=models.CharField(max_length=50,default='')
    status=models.BooleanField(default=True)

# carasoul database
class carasoul_DB(models.Model):
    img1=models.ImageField(upload_to='carasoul',default='')
    # img2=models.ImageField(upload_to='carasoul',default='')
    # img3=models.ImageField(upload_to='carasoul',default='')
    # img4=models.ImageField(upload_to='carasoul',default='')
    status=models.BooleanField(default=True)

    # card management database

class Cardmng_DB(models.Model):
    Cimg=models.ImageField(upload_to='caimg',default='')
    Ctitle=models.CharField(max_length=50,default='')
    Cdesc=models.CharField(max_length=150,default='')
    status=models.BooleanField(default=True)


