from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [  
      path('', views.login, name='login'), 
      path('logout', views.logout, name='logout'), 
      path('login', views.login, name='login'),
      path('register', views.registerPage, name='register'),
        
path('addUser/',views.addUser, name= "addUser"),

       path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name = "reset_password"),
       path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name = "password_reset_done"),
       path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name = "password_reset_confirm"),
       path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name = "password_reset_complete"),
      
path('animalResearcher/',views.animalResearcher, name= "animalResearcher"),
path('plantResearcher/',views.plantResearcher, name= "plantResearcher"),
path('microbialResearcher/',views.microbialResearcher, name= "microbialResearcher"),      

path('programCoordinator/',views.programCoordinator, name= "programCoordinator"),
path('programCoordinatorDetail/<int:pk>/', views.programCoordinatorDetail, name='programCoordinatorDetail'),
      
path('custodian/',views.custodian, name= "custodian"),
path('custodianDetail/<int:pk>/', views.custodianDetail, name='custodianDetail'),
      

       path('researcherDetail/<int:pk>/', views.researcherDetail, name='researcherDetail'),
            path('give/<int:pk>/', views.give, name='give'),
            path('revoke/<int:pk>/', views.revoke, name='revoke'),
            path('disableresearcher/<int:pk>/', views.disableresearcher, name='disableresearcher'),
            path('enableresearcher/<int:pk>/', views.enableresearcher, name='enableresearcher'),
            path('disabledepartment/<int:pk>/', views.disabledepartment, name='disabledepartment'),
            path('enabledepartment/<int:pk>/', views.enabledepartment, name='enabledepartment'),
            path('disablecustodian/<int:pk>/', views.disablecustodian, name='disablecustodian'),
            path('enablecustodian/<int:pk>/', views.enablecustodian, name='enablecustodian'),
      

]
 