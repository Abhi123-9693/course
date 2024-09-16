from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[
    # path('', admin.site.urls),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('widgets/',views.widgets,name='widgets'),
    path('header/',views.header,name='header'),

    
      
    
]
