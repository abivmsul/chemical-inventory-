from django.urls import path
from . import views
urlpatterns = [  
      path('', views.login, name='login'), 
     path('logout', views.logout, name='logout'), 
    path('login', views.login, name='login'),
     path('register', views.registerPage, name='register'),
        
path('addUser/',views.addUser, name= "addUser"),

]
 