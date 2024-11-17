from django.db import models

# Create your models here.
class Product(models.Model):
    pname=models.CharField(max_length=225)
    pbrand=models.CharField(max_length=225)
    pprice=models.IntegerField(max_length=225)
    psellprice=models.IntegerField(max_length=225)
    pdiscount=models.IntegerField(max_length=225)
    pimage=models.ImageField(default=None,null=True,blank=True,upload_to='img')

class freeread_db(models.Model):
    img=models.ImageField(upload_to='main_image',default='')
    title=models.CharField(max_length=50,default='')
    des=models.CharField(max_length=50,default='')
    status=models.BooleanField(default=True)