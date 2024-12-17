from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[
    # path('', admin.site.urls),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('add_product/',views.add_product,name='add_product'),
    path('productlist/',views.product_list,name='product_list'),
    path('freeread/',views.freeread,name='freeread'),
    path('delt_freeread/<id>',views.del_freeread,name='delt_freeread'),
    path('add_carasoul/',views.add_carasoulVv,name='add_carasoul'),
    path('card_mng/',views.card_mng,name='card_mng'),
    path('del_cardmng/<id>',views.del_cardmng,name='del_cardmng'),

    
      
    
]
