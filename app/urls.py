from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    # path('', admin.site.urls),
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('about',views.about,name='about'),
    path('signup',views.signup,name='signup'),

    
      
    
]
