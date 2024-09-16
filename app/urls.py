from django.contrib import admin
from django.urls import path
from . import views


urlpatterns =[
    # path('', admin.site.urls),
    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('course',views.course,name='course'),
    path('table',views.table,name='table'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('about',views.about,name='about'),
    path('signup',views.signup,name='signup'),
    path('edit/<id>',views.edit, name='edit'),
    path('delete/<id>',views.delete, name='delete'),

    
      
    
]