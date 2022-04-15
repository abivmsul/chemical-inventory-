from django.urls import path
from . import views
from .views import (requestSummary, requestConfirm, myRequest)

urlpatterns = [
       
    path('researcher',views.researcherHomeView, name= "researcherhome"),
    path('custodian/',views.custodianHomeView, name= "custodianhome"),
    path('deparment/',views.departmentHomeView, name= "departmenthome"),
    path('director/',views.directorHomeView, name= "directorhome"),

path('chemicalList/',views.chemicalList, name= "chemicalList"),
path('animalchemicalList/',views.animalchemicalList, name= "animalchemicalList"),
path('plantchemicalList/',views.plantchemicalList, name= "plantchemicalList"),
path('microbialchemicalList/',views.microbialchemicalList, name= "microbialchemicalList"),

    path('aExpired/',views.aExpired, name= "aExpired"),
    path('pExpired/',views.pExpired, name= "pExpired"),
    path('mExpired/',views.mExpired, name= "mExpired"),

path('aExpiredDeatil/<int:pk>/', views.aExpiredDeatil, name='aExpiredDeatil'),
path('pExpiredDeatil/<int:pk>/', views.pExpiredDeatil, name='pExpiredDeatil'),
path('m ExpiredDeatil/<int:pk>/', views.mExpiredDeatil, name='mExpiredDeatil'),

    path('adespose/<int:pk>/', views.adespose, name='adespose'),
    path('pdespose/<int:pk>/', views.pdespose, name='pdespose'),
    path('mdespose/<int:pk>/', views.mdespose, name='mdespose'),

path('aRequestDesposedChemical/',views.aRequestDesposedChemical, name= "aRequestDesposedChemical"),
path('pRequestDesposedChemical/',views.pRequestDesposedChemical, name= "pRequestDesposedChemical"),
path('mRequestDesposedChemical/',views.mRequestDesposedChemical, name= "mRequestDesposedChemical"),

#despose request for custodian
    path('aDesposeRequest/',views.aDesposeRequest, name= "aDesposeRequest"),
    path('pDesposeRequest/',views.pDesposeRequest, name= "pDesposeRequest"),
    path('mDesposeRequest/',views.mDesposeRequest, name= "mDesposeRequest"),
   
#despose condirm for custodian
path('aDesposeConfirm/<int:pk>/',views.aDesposeConfirm, name= "aDesposeConfirm"),
path('pDesposeConfirm/<int:pk>/',views.pDesposeConfirm, name= "pDesposeConfirm"),
path('mDesposeConfirm/<int:pk>/',views.mDesposeConfirm, name= "mDesposeConfirm"),


     path('aDesposedChemical/',views.aDesposedChemical, name= "aDesposedChemical"),
     path('pDesposedChemical/',views.pDesposedChemical, name= "pDesposedChemical"),
     path('mDesposedChemical/',views.mDesposedChemical, name= "mDesposedChemical"),

path('animalrequests/',views.animalRequests, name= "animalrequests"),
path('micobialrequests/',views.microbialRequests, name= "microbialrequests"),
path('plantrequests/',views.plantRequests, name= "plantrequests"),


    path('animalrequestsofdepartment/',views.animalRequestsOfDepartment, name= "animalrequestsofdpartment"),
    path('plantrequestsofdepartment/',views.plantRequestsOfDepartment, name= "plantrequestsofdpartment"),
    path('microbialrequestsofdepartments/',views.microbialRequestsOfDepartment, name= "microbialrequestsofdpartment"),


path('animaldepartmentRequest/',views.animaldepartmentRequest, name= "animaldepartmentRequest"),
path('plantdepartmentRequest/',views.plantdepartmentRequest, name= "plantdepartmentRequest"),
path('microbialdepartmentRequest/',views.microbialdepartmentRequest, name= "microbialdepartmentRequest"),


    path('requestDetal/<int:pk>/', views.requestDetal, name='requestDetal'), 

path('removeRequest/<int:pk>/', views.removeRequest, name='removeRequest'), 
path('remove/<int:pk>/', views.remove, name='remove'), 

    path('animaldRequestDetal/<int:pk>/<int:ck>/', views.animaldRequestDetal, name='animaldRequestDetal'), 
    path('plantdRequestDetal/<int:pk>/<int:ck>/', views.plantdRequestDetal, name='plantdRequestDetal'), 
    path('microbialdRequestDetal/<int:pk>/<int:ck>/', views.microbialdRequestDetal, name='microbialdRequestDetal'), 
  
    path('updateStatus/<int:pk>/', views.updateStatus, name='updateStatus'),
    path('updatequantity/<int:rk>/<int:ck>/', views.updateQuantity, name='updatequantity'),


path('chemicals/',views.Chemicals, name= "chemicals"),
path('animalchemicals/',views.animalChemicals, name= "animalchemicals"),
path('microbialchemicals/',views.microbialChemicals, name= "microbialchemicals"),
path('plantchemicals/',views.plantChemicals, name= "plantchemicals"),

    path('chemical/<int:pk>',views.chemicalDetail, name= "chemical"),
    path('addToList/<int:pk>/', views.addToList, name='addToList'),  
    path('addQuantity/<int:pk>/', views.addQuantity, name='addQuantity'),
    
    path('requestSummary/', requestSummary.as_view(), name='requestSummary'),
    path('removeSingleChemicalFromList/<int:pk>/', views.removeSingleChemicalFromList, name='removeSingleChemicalFromList'),
    path('removeFromList/<int:pk>/', views.removeFromList, name='removeFromList'),
    path('requestConfirm/', requestConfirm.as_view(), name='requestConfirm'),
    path('finishRequest/',views.finishRequest, name= 'finishRequest'),
    path('myRequest/',myRequest.as_view(), name= "myRequest"),
    # path('register/',views.register, name= "register"),
    # path('request/',views.requestChemical, name= "request"),
    

# report 
path('csvChemicalReport/<str:dept>/', views.csvChemicalReport, name='csvChemicalReport'),
path('csvEChemicalReport/<str:dept>/', views.csvEChemicalReport, name='csvEChemicalReport'),
path('csvDChemicalReport/<str:dept>/', views.csvDChemicalReport, name='csvDChemicalReport'),

]