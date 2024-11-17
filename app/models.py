from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=225)
    last_name=models.CharField(max_length=225)
    email=models.EmailField(max_length=225)
    password=models.CharField(max_length=225)
    permanent_address=models.CharField(max_length=225)
    residincial_address=models.CharField(max_length=225)
    city=models.CharField(max_length=225)
    state=models.CharField(max_length=225)
    number=models.IntegerField(max_length=12,default=0)
    checkbox=models.CharField(max_length=225,default=1)
    image=models.ImageField(default=None,null=True,blank=True,upload_to='img')
    

# class Customerlogin(models.Model):
#     email_address=models.EmailField(max_length=225)  
#     password=models.IntegerField(max_length=50)
#     checkbox=models.CharField(max_length=250)  

# class Customeredit(models.Model):
#     first_name=models.CharField(max_length=225)
#     last_name=models.CharField(max_length=225)
#     email=models.EmailField(max_length=225)
#     password=models.CharField(max_length=225)
#     permanent_address=models.CharField(max_length=225)
#     residincial_address=models.CharField(max_length=225)
#     city=models.CharField(max_length=225)
#     state=models.CharField(max_length=225)
#     number=models.IntegerField(max_length=12,default=0)
#     checkbox=models.CharField(max_length=225,default=1)




