from django.shortcuts import render,get_object_or_404,redirect
from .models import Chemical,RequestChemical,Request
from account.models import Researcher
from department.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required 
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.models import User
from chemical.forms import AddChemicalForm , Atemp, Mtemp, Ptemp
from . import models
from django.http import HttpResponse
import csv

# from django.http import FileResponse
# import io
# from reportlab.pdfgen import canvas
# from reportlab.lib.units import inch
# from reportlab.lib.pagesizes import letter

import datetime
# Create your views here.

def login(request):
     return render(request,'login.html')


@login_required(login_url='login')
def researcherHomeView (request):    
    pendingOrder = Request.objects.filter(user = request.user, confirmed = False).count()
    acceptedOrder = Request.objects.filter(user = request.user, confirmed = True).count()
    completedOrder = Request.objects.filter(user = request.user, received = True).count()
    context = {'requests':Request.objects.filter(requested=True), 'pendingOrder': pendingOrder,'acceptedOrder':acceptedOrder, 'completedOrder':completedOrder}
    return render(request, 'researcher/researcher_home.html', context)


@login_required(login_url='login')
def custodianHomeView (request):
    pendingOrder = Request.objects.filter(user = request.user, confirmed = False).count()
    acceptedOrder = Request.objects.filter(user = request.user, confirmed = True).count()
    completedOrder = Request.objects.filter(user = request.user, received = True).count()
    context = {'requests':Request.objects.filter(requested=True), 'pendingOrder': pendingOrder,'acceptedOrder':acceptedOrder, 'completedOrder':completedOrder}
    return render(request, 'custodian/custodian_home.html', context)

@login_required(login_url='login')
def departmentHomeView (request):  
    animalChemicals = AnimalStore.objects.all().count()
    plantChemicals = PlantStore.objects.all().count()
    microbialChemicals = MicrobialStore.objects.all().count()
 
    
    animalResearcher = Researcher.objects.filter(researcher__is_active = True, department = 'Animal Biotechnology').count()
    plantResearcher = Researcher.objects.filter(researcher__is_active = True, department = 'Plant Biotechnology').count()
    microbialResearcher = Researcher.objects.filter(researcher__is_active = True, department = 'Microbial Biotechnology').count()
    date = datetime.datetime.now()
    Aexpired = AnimalStore.objects.filter(expireDate__lt= date).count()
    Mexpired = MicrobialStore.objects.filter(expireDate__lt= date).count()
    Pexpired = PlantStore.objects.filter(expireDate__lt= date).count()
    Aavailable = AnimalStore.objects.filter(expireDate__gt= date).count()
    Mavailable = MicrobialStore.objects.filter(expireDate__gt= date).count()
    Pavailable = PlantStore.objects.filter(expireDate__gt= date).count()
    Adesposed = AnimalDesposedChemical.objects.filter(desposed = True).count()
    Pdesposed = PlantDesposedChemical.objects.filter(desposed = True).count()
    Mdesposed = MicrobialDesposedChemical.objects.filter(desposed = True).count()
    context = {
        'animalChemicals': animalChemicals,
        'plantChemicals':plantChemicals,
        'microbialChemicals': microbialChemicals,
        'animalResearcher': animalResearcher,
        'plantResearcher': plantResearcher,
        'microbialResearcher': microbialResearcher,
        'Aexpired': Aexpired,
        'Mexpired': Mexpired,
        'Pexpired': Pexpired,
        'Aavailable': Aavailable,
        'Mavailable': Mavailable,
        'Pavailable': Pavailable,
        'Adesposed': Adesposed,
        'Pdesposed': Pdesposed,
        'Mdesposed': Mdesposed,
         }
    return render(request, 'department/department_home.html', context)

@login_required(login_url='login')
def directorHomeView (request):  
    date = datetime.datetime.now()
    Aexpired = AnimalStore.objects.filter(expireDate__lt= date).count()
    Mexpired = MicrobialStore.objects.filter(expireDate__lt= date).count()
    Pexpired = PlantStore.objects.filter(expireDate__lt= date).count()
    Aavailable = AnimalStore.objects.filter(expireDate__gt= date).count()
    Pavailable = MicrobialStore.objects.filter(expireDate__gt= date).count()
    Mavailable = PlantStore.objects.filter(expireDate__gt= date).count()

    animalResearcher = Researcher.objects.filter(researcher__is_active = True, department = 'Animal Biotechnology').count()
    plantResearcher = Researcher.objects.filter(researcher__is_active = True, department = 'Plant Biotechnology').count()
    microbialResearcher = Researcher.objects.filter(researcher__is_active = True, department = 'Microbial Biotechnology').count()

    Adesposed = AnimalDesposedChemical.objects.filter(desposed = True).count()
    Pdesposed = PlantDesposedChemical.objects.filter(desposed = True).count()
    Mdesposed = MicrobialDesposedChemical.objects.filter(desposed = True).count()
    context = {
        'Aexpired': Aexpired,
        'Mexpired': Mexpired,
        'Pexpired': Pexpired,
        'Aavailable': Aavailable,
        'Mavailable': Mavailable,
        'Pavailable': Pavailable,
        'animalResearcher': animalResearcher,
        'plantResearcher': plantResearcher,
        'microbialResearcher': microbialResearcher,
        'Adesposed': Adesposed,
        'Pdesposed': Pdesposed,
        'Mdesposed': Mdesposed,
    }
    return render(request, 'director/director_home.html', context)

@login_required(login_url='login')
def addUser(request):  
   
    context = {}
    return render(request, 'director/add_user.html', context)


# Custodian Requestochn view miyaregbbet 
@login_required(login_url='login')
def animalRequests (request):
    page = 'animal'
    requests = Request.objects.filter(requested = True, confirmed = True,  department = 'Animal Biotechnology' )

    context = { 'page': page, 'obj': requests}
    return render(request, 'custodian/view_requests.html', context)


@login_required(login_url='login')
def microbialRequests (request):
    page = 'microbial'
    requests = Request.objects.filter(requested= True, confirmed= True, department = 'Microbial Biotechnology' )

    context = { 'page': page, 'obj': requests}
    return render(request, 'custodian/view_requests.html', context)


@login_required(login_url='login')
def plantRequests (request):
    page = 'plant'
    requests = Request.objects.filter(requested= True, confirmed= True, department = 'Plant Biotechnology' )

    context = { 'page': page, 'obj': requests}
    return render(request, 'custodian/view_requests.html', context)

# Departments Requestochn view miyaregbbet 

@login_required(login_url='login')
def animalRequestsOfDepartment (request):
    page = 'animal'
    requests = Request.objects.filter(requested = True,  deptRequest=False, department = 'Animal Biotechnology' )

    context = { 'page': page, 'obj': requests}
    return render(request, 'department/view_requests.html', context)

@login_required(login_url='login')
def microbialRequestsOfDepartment (request):
    page = 'microbial'
    requests = Request.objects.filter(requested= True, deptRequest=False, department = 'Microbial Biotechnology' )

    context = { 'page': page, 'obj': requests}
    return render(request, 'department/view_requests.html', context)

@login_required(login_url='login')
def plantRequestsOfDepartment (request):
    page = 'plant'
    requests = Request.objects.filter(requested= True, deptRequest=False, department = 'Plant Biotechnology' )

    context = { 'page': page, 'obj': requests}
    return render(request, 'department/view_requests.html', context)


# Ye Departments chemical despose Requestochn view miyaregbbet 

@login_required(login_url='login')
def aDesposeRequest (request):
    page = 'animal'
    requests = AnimalDesposedChemical.objects.all()

    context = { 'page': page, 'obj': requests}
    return render(request, 'custodian/view_despose_requests.html', context)

@login_required(login_url='login')
def mDesposeRequest (request):
    page = 'microbial'
    requests = MicrobialDesposedChemical.objects.all()

    context = { 'page': page, 'obj': requests}
    return render(request, 'custodian/view_despose_requests.html', context)


@login_required(login_url='login')
def pDesposeRequest (request):
    page = 'plant'
    requests = PlantDesposedChemical.objects.all()

    context = { 'page': page, 'obj': requests}
    return render(request, 'custodian/view_despose_requests.html', context)


###*************************************************************************************

@login_required(login_url='login')
def animaldepartmentRequest (request):
    page = 'animal'
    req = 'department'
    requests = Request.objects.filter(requested = True, deptRequest=True,  department = 'Animal Biotechnology' )

    context = { 'page': page, 'obj': requests , 'req':req}
    return render(request, 'custodian/view_requests.html', context)


@login_required(login_url='login')
def microbialdepartmentRequest (request):
    page = 'microbial'
    req = 'department'
    requests = Request.objects.filter(requested= True,  deptRequest=True,  department = 'Microbial Biotechnology' )

    context = { 'page': page, 'obj': requests, 'req':req}
    return render(request, 'custodian/view_requests.html', context)

@login_required(login_url='login')
def plantdepartmentRequest (request):
    page = 'plant'
    req = 'department'
    requests = Request.objects.filter(requested= True,  deptRequest=True,  department = 'Plant Biotechnology' )

    context = { 'page': page, 'obj': requests, 'req':req}
    return render(request, 'custodian/view_requests.html', context)
 

# request detail    
@login_required(login_url='login')
def requestDetal(request,pk):
    requests = Request.objects.get(id = pk)
    if request.method == 'POST':
        pin = request.POST.get('pin')
        print(pin)
        print(requests.checked)
        if requests.pin == pin:
            requests.checked = True
            requests.save()
            next = request.POST.get('next', '/')
            return redirect(next)
        else:
            messages.warning(request," invalid Pin ")
            next = request.POST.get('next', '/')
            return redirect(next)

    context = {'obj': requests}
    return render(request, 'custodian/request_detail.html',context)


# request detail    
@login_required(login_url='login')
def removeRequest(request,pk):
    requests = Request.objects.get(id = pk)
    context = {'obj': requests}
    return render(request, 'remove_request.html',context)


@login_required(login_url='login')
def remove(request,pk):
    requests = Request.objects.get(id = pk)
    print(requests.chemicals.all())
    print("adsfas")
    for che in requests.chemicals.all():
        print(che.id)
        chemicals = RequestChemical.objects.get(id=che.id,user=request.user)
        print(chemicals)
        requests.chemicals.remove(chemicals)
        chemicals.delete()
    requests.delete()
    messages.success(request, "You have successfully removed Your Request.")
    return redirect('myRequest')
    

@login_required(login_url='login')
def animaldRequestDetal(request,pk,ck):
    page = 'animal'
    temprature = Atemp()
    requests = Request.objects.get(id = pk)
    requested_chemicals = requests.chemicals.get(id = ck)
    #for chemical in requested_chemicals:
        # print(chemical.chemical.id)
        # print(requests.user.department.department)
        # if requests.user.department.department == 'Animal Biotechnolgy':
    animal = AnimalStore.objects.get(chemical_id = requested_chemicals.chemical.id ) 
    # store = animal[0]   
    # print(chemical.chemical.id)
    context = {'obj': requests,'store':animal , 'che':requested_chemicals, 'page':page , 'temp':temprature}        
    return render(request, 'custodian/d_request_detail.html',context)

@login_required(login_url='login')
def plantdRequestDetal(request,pk,ck):
    page = 'plant'
    temprature = Ptemp()
    requests = Request.objects.get(id = pk)
    requested_chemicals = requests.chemicals.get(id = ck)
    #for chemical in requested_chemicals:
        # print(chemical.chemical.id)
        # print(requests.user.department.department)
        # if requests.user.department.department == 'Animal Biotechnolgy':
    plant = PlantStore.objects.get(chemical_id = requested_chemicals.chemical.id ) 
    # store = animal[0]   
    # print(chemical.chemical.id)
    context = {'obj': requests,'store':plant , 'che':requested_chemicals, 'page':page, 'temp':temprature}        
    return render(request, 'custodian/d_request_detail.html',context)

@login_required(login_url='login')
def microbialdRequestDetal(request,pk,ck):
    page = 'microbial'
    temprature = Mtemp()
    requests = Request.objects.get(id = pk)
    requested_chemicals = requests.chemicals.get(id = ck)
    #for chemical in requested_chemicals:
        # print(chemical.chemical.id)
        # print(requests.user.department.department)
        # if requests.user.department.department == 'Animal Biotechnolgy':
    microbial = MicrobialStore.objects.get(chemical_id = requested_chemicals.chemical.id ) 
    # store = animal[0]   
    # print(chemical.chemical.id)
    context = {'obj': requests,'store':microbial , 'che':requested_chemicals, 'page':page,'temp':temprature}        
    return render(request, 'custodian/d_request_detail.html',context)

@login_required(login_url='login')
def updateStatus(request,pk):
    requests = Request.objects.get( id = pk )
    if request.method =='POST':
        status = request.POST.get('status')
        if status == 'accept':
            requests.confirmed = True
            requests.deny = False
            requests.save()
             #messages.success(request, "You have confirmed the request")
            next = request.POST.get('next', '/')
            return redirect(next)
        elif status == 'deny':
            requests.confirmed = False
            requests.deny = True
            requests.save()
            #messages.success(request, "You have confirmed the request")
            next = request.POST.get('next', '/')
            return redirect(next)

@login_required(login_url='login')
def updateQuantity(request,rk,ck):
    requests = Request.objects.get( id = rk )
    chemical = RequestChemical.objects.get( id = ck )
    #print(chemical.chemical.name)
    if request.method =='POST' and 'issued' in request.POST:
        quantity = request.POST.get('quantity')
        chemical.recieved = True
        chemical.issuedquantity = quantity
        requests.received = True
        #chemical.save()
       
        if requests.department == 'Animal Biotechnology':
            store = AnimalStore.objects.get(chemical_id = chemical.chemical.id)
            print(store.available)
            store.available = int(store.available) - int(quantity)
            store.save()
            chemical.save()
            requests.save()
            next = request.POST.get('next', '/')
            return redirect(next)

        elif requests.department == 'Plant Biotechnology':
            store = PlantStore.objects.get(chemical_id = chemical.chemical.id)
            print(store.available)
            store.available = int(store.available) - int(quantity)
            store.save()
            chemical.save()
            requests.save()
            next = request.POST.get('next', '/')
            return redirect(next)

        elif requests.department == 'Microbial Biotechnology':
            store = MicrobialStore.objects.get(chemical_id = chemical.chemical.id)
            print(store.available)
            store.available = int(store.available) - int(quantity)
            store.save()
            chemical.save()
            requests.save()
            next = request.POST.get('next', '/')
            return redirect(next)
    
    elif request.method =='POST' and 'add' in request.POST:
        quantity = request.POST.get('quantity')
        exdate = request.POST.get('exdate')
        shelf = request.POST.get('shelf')
        cabinate = request.POST.get('cabinate')

        chemical.recieved = True
        chemical.issuedquantity = quantity
        requests.received = True
        #chemical.save()
       
        if requests.department == 'Animal Biotechnology':
            temp = Atemp()
            temp = Atemp(request.POST)
            if temp.is_valid():
                temprature = temp.cleaned_data.get('temprature')
            store = AnimalStore.objects.get(chemical_id = chemical.chemical.id)
            print(store.available)
            store.available = int(store.available) + int(quantity)
            store.expireDate = exdate
            store.cabinate = cabinate
            store.shelf = shelf
            store.temprature = temprature
            store.save()
            chemical.save()
            requests.save()
            next = request.POST.get('next', '/')
            return redirect(next)

        elif requests.department == 'Plant Biotechnology':
            temp = Ptemp()
            temp = Ptemp(request.POST)
            if temp.is_valid():
                temprature = temp.cleaned_data.get('temprature')
            store = PlantStore.objects.get(chemical_id = chemical.chemical.id)
            print(store.available)
            store.available = int(store.available) + int(quantity)
            store.expireDate = exdate
            store.cabinate = cabinate
            store.shelf = shelf
            store.temprature = temprature
            store.save()
            chemical.save()
            requests.save()
            next = request.POST.get('next', '/')
            return redirect(next)

        elif requests.department == 'Microbial Biotechnology':
            
            temp = Atemp()
            temp = Atemp(request.POST)
            if temp.is_valid():
                temprature = temp.cleaned_data.get('temprature')
            store = MicrobialStore.objects.get(chemical_id = chemical.chemical.id)
            print(store.available)
            store.available = int(store.available) + int(quantity)
            store.expireDate = exdate
            store.cabinate = cabinate
            store.shelf = shelf
            store.temprature = temprature
            store.save()
            chemical.save()
            requests.save()
            next = request.POST.get('next', '/')
            return redirect(next)
   
# custidian gar yale chemi
def Chemicals (request):
    chemicals = Chemical.objects.all( )

    context = { 'obj': chemicals}
    return render(request, 'custodian/chemicals.html', context)

def animalChemicals (request):
    page = 'animal'
    date = datetime.datetime.now()
    chemicals = AnimalStore.objects.filter(  expireDate__gt= date )
    date = datetime.datetime.now()
    
    context = { 'page': page, 'obj': chemicals }
    return render(request, 'custodian/chemicals.html', context)

def microbialChemicals (request):
    page = 'microbial'
    date = datetime.datetime.now()
    chemicals = MicrobialStore.objects.filter(  expireDate__gt= date )

    context = { 'page': page, 'obj': chemicals}
    return render(request, 'custodian/chemicals.html', context)

def plantChemicals (request):
    page = 'plant'
    date = datetime.datetime.now()
    chemicals = PlantStore.objects.filter(  expireDate__gt= date )

    context = { 'page': page, 'obj': chemicals}
    return render(request, 'custodian/chemicals.html', context)


#-----------------------------------------------------------------------
# Expired chemicals
def aExpired (request):
    page = 'animal'
    date = datetime.datetime.now()
    chemicals = AnimalStore.objects.filter( expireDate__lt= date)
    
    context = { 'page': page, 'obj': chemicals }
    return render(request, 'custodian/expired_chemical.html', context)

def mExpired (request):
    page = 'microbial'
    date = datetime.datetime.now()
    chemicals = MicrobialStore.objects.filter( expireDate__lt= date)

    context = { 'page': page, 'obj': chemicals}
    return render(request, 'custodian/expired_chemical.html', context)

def pExpired (request):
    page = 'plant'
    date = datetime.datetime.now()
    chemicals = PlantStore.objects.filter( expireDate__lt= date)

    context = { 'page': page, 'obj': chemicals}
    return render(request, 'custodian/expired_chemical.html', context)


# expired detail
def aExpiredDeatil(request,pk):
    page = 'animal'
    expired = AnimalStore.objects.get(id = pk)

    context = {'expired': expired ,'page': page}
    return render(request, 'custodian/expired_detail.html',context )

def pExpiredDeatil(request,pk):
    page = 'plant'
    expired = PlantStore.objects.get(id = pk)

    context = {'expired': expired, 'page': page}
    return render(request, 'custodian/expired_detail.html',context )

def mExpiredDeatil(request,pk):
    page = 'microbial'
    expired = MicrobialStore.objects.get(id = pk)

    context = {'expired': expired, 'page': page}
    return render(request, 'custodian/expired_detail.html',context )
#----------------------------------------------------------------------------------------


# despose view
def adespose(request,pk):
    chemical = AnimalStore.objects.get(id = pk)
    AnimalDesposedChemical.objects.create(
        chemical =chemical.chemical,
        cabinate = chemical.cabinate,
        shelf = chemical.shelf,
        available = chemical.available,
        recievedDate = chemical.recievedDate,
        expireDate = chemical.expireDate,
        )
    chemical.delete()
    return redirect('aRequestDesposedChemical')

def pdespose(request,pk):
    chemical = PlantStore.objects.get(id = pk)
    PlantDesposedChemical.objects.create(
        chemical =chemical.chemical,
        cabinate = chemical.cabinate,
        shelf = chemical.shelf,
        available = chemical.available,
        recievedDate = chemical.recievedDate,
        expireDate = chemical.expireDate,
        )
    chemical.delete()
    return redirect('pRequestDesposedChemical')

def mdespose(request,pk):
    chemical = MicrobialStore.objects.get(id = pk)
    MicrobialDesposedChemical.objects.create(
        chemical =chemical.chemical,
        cabinate = chemical.cabinate,
        shelf = chemical.shelf,
        available = chemical.available,
        recievedDate = chemical.recievedDate,
        expireDate = chemical.expireDate,
        )
    chemical.delete()
    return redirect('mRequestDesposedChemical')

#----------------------------------------------------------------------------------------

#requests for chemical despose
def aRequestDesposedChemical(request):
    page = 'animal'
    che = AnimalDesposedChemical.objects.all()

    context = {'page':page, 'che': che}
    return render(request, 'department/request_to_despose.html',context )

def pRequestDesposedChemical(request):
    page = 'plant'
    che = PlantDesposedChemical.objects.all()

    context = {'page':page, 'che': che}
    return render(request, 'department/request_to_despose.html',context )

def mRequestDesposedChemical(request):
    page = 'microbial'
    che = MicrobialDesposedChemical.objects.all()

    context = {'page':page, 'che': che}
    return render(request, 'department/request_to_despose.html',context )



# Despose request detail
def aDesposeConfirm(request,pk):
    date = datetime.datetime.now()
    chemical = AnimalDesposedChemical.objects.get(id = pk)
    chemical.desposed = True
    chemical.desposedDate = date
    chemical.save()
    return redirect(aDesposeRequest)

def pDesposeConfirm(request,pk):
    date = datetime.datetime.now()
    chemical = PlantDesposedChemical.objects.get(id = pk)
    chemical.desposed = True
    chemical.desposedDate = date
    chemical.save()
    return redirect(pDesposeRequest)

def mDesposeConfirm(request,pk):
    date = datetime.datetime.now()
    chemical = MicrobialDesposedChemical.objects.get(id = pk)
    chemical.desposed = True
    chemical.desposedDate = date
    chemical.save()
    return redirect(mDesposeRequest)
#----------------------------------------------------------------------------------------



#*------------------------------------------------------------------------------------------
#desposed chemicals
def aDesposedChemical(request):
    page = 'animal'
    desposed = AnimalDesposedChemical.objects.filter(desposed = True)

    context = {'page':page, 'desposed': desposed}
    return render(request, 'custodian/desposed_chemical.html',context )

def pDesposedChemical(request):
    page = 'plant'
    desposed = PlantDesposedChemical.objects.filter(desposed = True)

    context = {'page':page, 'desposed': desposed}
    return render(request, 'custodian/desposed_chemical.html',context )

def mDesposedChemical(request):
    page = 'microbial'
    desposed = MicrobialDesposedChemical.objects.filter(desposed = True)

    context = {'page':page, 'desposed': desposed}
    return render(request, 'custodian/desposed_chemical.html',context )



# Chemicallsssss LIstsssss
def chemicalList (request):
    form = AddChemicalForm()
    if request.GET.get('q') != None:
        q = request.GET.get('q')  
    else:
        q = ''
    chemical = Chemical.objects.filter(name__icontains = q)
    if request.method =='POST':
        form = AddChemicalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('chemicalList')
    
    context = {'chemical': chemical, 'form': form }
    return render(request, 'chemical_list.html', context)

    
# chemical search
def animalchemicalList (request):
    page = 'animal'
    date = datetime.datetime.now()
    if request.GET.get('q') != None:
        q = request.GET.get('q')  
    else:
        q = ''
    context = {'page':page ,'chemical': AnimalStore.objects.filter(chemical__name__icontains = q , expireDate__gt = date )}
    return render(request, 'chemical_list.html', context)
def plantchemicalList (request):
    page = 'plant'
    date = datetime.datetime.now()
    if request.GET.get('q') != None:
        q = request.GET.get('q')  
    else:
        q = ''
    context = {'page':page ,'chemical': PlantStore.objects.filter(chemical__name__icontains = q ,  expireDate__gt = date)}
    return render(request, 'chemical_list.html', context)

def microbialchemicalList (request):
    page = 'microbial'
    date = datetime.datetime.now()
    if request.GET.get('q') != None:
        q = request.GET.get('q')  
    else:
        q = '' 
    context = {'page':page ,'chemical': MicrobialStore.objects.filter(chemical__name__icontains = q ,  expireDate__gt = date)}
    return render(request, 'chemical_list.html', context)

def chemicalDetail (request,pk):
    context = {'chemical': Chemical.objects.get(id = pk)}
    return render(request, 'chemical_detail.html', context)


def addQuantity(request, pk):
    chemical = get_object_or_404(Chemical, id = pk)
    request_chemical, created = RequestChemical.objects.get_or_create(chemical=chemical,user=request.user,requested=False)
    if request.method =='POST':
        quantity = request.POST.get('quantity')
        #print(quantity)
        #print(request.user.researcher.department)
        if request.user.groups.filter(name='Researcher').exists():
            if request.user.researcher.department == 'Animal Biotechnology':
                che = AnimalStore.objects.get(chemical_id = chemical.id)
                print(che.available) 
                if int(quantity) > che.available:
                    messages.warning(request, "please reduce your amount")
                    next = request.POST.get('next', '/')
                    return redirect(next)
            elif request.user.researcher.department == 'Plant Biotechnology':
                che = PlantStore.objects.get(chemical_id = chemical.id)
                print(che.available) 
                if int(quantity) > che.available:
                    messages.warning(request, "please reduce your amount")
                    next = request.POST.get('next', '/')
                    return redirect(next)
            elif request.user.researcher.department == 'Microbial Biotechnology':
                che = MicrobialStore.objects.get(chemical_id = chemical.id)
                print(che.available) 
                if int(quantity) > che.available:
                    messages.warning(request, "please reduce your amount")
                    next = request.POST.get('next', '/')
                    return redirect(next) 
           
    request_qs = Request.objects.filter(user=request.user, requested=False)
    print(request_qs)
    if request_qs.exists():
        print('tttttt')
        requests = request_qs[0] 
        print(requests)
        # check if the request chemical is in the request
        if requests.chemicals.filter(chemical__id=chemical.id).exists():
            request_chemical.quantity = int(quantity)
            request_chemical.save()
            
            #messages.info(request, "This chemical quantity was updated.")
            return redirect('requestSummary')
        else:
            requests.chemicals.add(request_chemical)
            request_chemical.quantity = int(quantity)
            request_chemical.save()
            #messages.info(request, "This chemical was added to your cart.")
            return redirect('requestSummary')
    else:
        request = Request.objects.create(user=request.user)
        request.chemicals.add(request_chemical)
        request_chemical.quantity = int(quantity)
        request_chemical.save()
        #messages.info(request, "This chemical was added to your cart.")
        return redirect('requestSummary')



def addToList(request, pk):
    chemical = get_object_or_404(Chemical, id = pk)
   # request_chemical, created = requestchemical.objects.get_or_create(chemical=chemical,user=request.user,requested=False)
    request_chemical, created = RequestChemical.objects.get_or_create(chemical=chemical,user=request.user,requested=False)
    request_qs = Request.objects.filter(user=request.user, requested=False)
    print(request_qs)
    if request_qs.exists():
        request = request_qs[0]
        # check if the request chemical is in the request
        if request.chemicals.filter(chemical__id=chemical.id).exists():
            request_chemical.quantity += 1
            request_chemical.save()
            #messages.info(request, "This chemical quantity was updated.")
            return redirect('requestSummary')
        else:
            request.chemicals.add(request_chemical)
            #messages.info(request, "This chemical was added to your cart.")
            return redirect('requestSummary')
    else:
        request = Request.objects.create(user=request.user)
        request.chemicals.add(request_chemical)
        #messages.info(request, "This chemical was added to your cart.")
        return redirect('requestSummary')


#def requestSummary(request):
class requestSummary(View):
    def get(self, *args, **kwargs):
       
        request = Request.objects.get(user=self.request.user, requested=False)
        context = {'object': request }
        return render(self.request, 'request_summary.html', context)
    
  

def removeSingleChemicalFromList(request, pk):
    chemical = get_object_or_404(Chemical, id = pk)
    request_qs = Request.objects.filter(user=request.user,requested=False)
    if request_qs.exists():
        request = request_qs[0]
        # check if the request chemical is in the request
        if request.chemicals.filter(chemical__id=chemical.id).exists():
            request_chemical = RequestChemical.objects.filter(chemical=chemical,user=request.user,requested=False)[0]
            if request_chemical.quantity > 1:
                request_chemical.quantity -= 1
                request_chemical.save()
            else:
                request.chemicals.remove(request_chemical)
                # request_chemical.delete()
            #messages.info(request, "This chemical quantity was updated.")
            return redirect('requestSummary')
        else:
            #messages.info(request, "This chemical was not in your cart")
            return redirect('chemical', pk = pk)
    else:
        #messages.info(request, "You do not have an active request")
        return redirect('chemical', pk = pk)

def removeFromList(request, pk):
    chemical = get_object_or_404(Chemical, id = pk)
    request_qs = Request.objects.filter(user=request.user,requested=False)
    if request_qs.exists():
        request = request_qs[0]
        # check if the request chemical is in the request
        if request.chemicals.filter(chemical__id=chemical.id).exists():
            request_chemical = RequestChemical.objects.filter(chemical=chemical,user=request.user,requested=False)[0]
            request.chemicals.remove(request_chemical)
            request_chemical.delete()
            #messages.info(request, "This chemical was removed from your cart.")
            return redirect('requestSummary')
        else:
            #messages.info(request, "This chemical was not in your cart")
            return redirect('chemical', pk = pk)
    else:
        #messages.info(request, "You do not have an active request")
        return redirect('chemical', pk = pk)

# def requestConfirm(request):

#     request = Request.objects.get(user=request.user, requested=False)
 
#     context = {'objects': request}
#     return render(request, 'request_confirm.html', context)

class requestConfirm(LoginRequiredMixin,View):
    def get(self, *args, **kwargs):
        request = Request.objects.get(user=self.request.user, requested=False)
       
        context = {'object': request }
        return render(self.request, 'request_confirm.html', context)

def finishRequest(request):
    if request.user.groups.filter(name='Researcher').exists():
        requests = Request.objects.get(user=request.user, requested=False)
        pin = User.objects.make_random_password(length=4,allowed_chars='123456789')
        requested_chemicals = requests.chemicals.all()
        requested_chemicals.update(requested=True)
           
        for chemical in requested_chemicals:
            chemical.save()

        requests.requested = True
        requests.pin = pin
        requests.department = request.user.researcher.department
        requests.save()

        messages.success(request, "Your Request was successful!")
        return redirect('myRequest')    

    elif request.user.groups.filter(name='Department').exists():
 
        requests = Request.objects.get(user=request.user, requested=False)
        requested_chemicals = requests.chemicals.all()
        requested_chemicals.update(requested=True)
        
        for chemical in requested_chemicals:
            chemical.save()
            print(chemical.chemical.id)
            if request.user.department.department == 'Animal Biotechnology':
                AnimalStore.objects.get_or_create(chemical_id = chemical.chemical.id)
            elif request.user.department.department == 'Plant Biotechnology':
                PlantStore.objects.get_or_create(chemical_id = chemical.chemical.id)
            elif request.user.department.department == 'Microbial Biotechnology':
                MicrobialStore.objects.get_or_create(chemical_id = chemical.chemical.id)
        requests.deptRequest = True
        requests.requested = True
        requests.department = request.user.department.department
        requests.save()

        messages.success(request, "Your Request was successful!")
        return redirect('myRequest')    

class myRequest(LoginRequiredMixin,View):
    def get(self, *args, **kwargs):
        request_qs = Request.objects.filter(user=self.request.user, requested=True)
        #print(request_qs)
        if request_qs.exists():
            request = request_qs[0]
        else:
            request = []    
        context = { 'obj': Request.objects.filter(user=self.request.user,requested=True)}
        return render(self.request, 'my_request.html', context)


#all chemical report
def csvChemicalReport(request,dept):
    if dept == 'animal':
        if request.method =='POST' and 'csv' in request.POST: 
            start = request.POST['start']
            to = request.POST['to']
            response = HttpResponse(content_type = 'text/csv')
            response['content-diposition'] = 'attachment; filename = Animalchemicals.csv'

            #create csv writer
            writer = csv.writer(response)
            date = datetime.datetime.now()
            animalChemical = AnimalStore.objects.filter( desposedDate__range=[start,to])
            animalChemical.filter(expireDate__gt= date) 
            writer.writerow([])
            writer.writerow(['','','Animal Bio Technology "Available" Chemicals','','',date])
            writer.writerow([])
            #column of file 
            count = 1
            writer.writerow(['NO',' CHEMICAL NAME ','COMPANY','QUANTITY','UNIT','SHELF','CABINATE','FREEZER','EXPIRE DATE'])
            for chemical in animalChemical:
                writer.writerow([count ,chemical.chemical.name, chemical.chemical.company, chemical.available, chemical.chemical.unit, chemical.shelf, chemical.cabinate, chemical.temprature, chemical.expireDate])
                count+=1
            return response    
        elif request.method =='POST' and 'allcsv' in request.POST: 
            start = request.POST['start']
            to = request.POST['to']
            response = HttpResponse(content_type = 'text/csv')
            response['content-diposition'] = 'attachment; filename = Animalchemicals.csv'

            #create csv writer
            writer = csv.writer(response)
            date = datetime.datetime.now()
            animalChemical = AnimalStore.objects.filter( desposedDate__range=[start,to])
            animalChemical.all() 
            writer.writerow([])
            writer.writerow(['','','Animal Bio Technology "All" Chemicals','','',date])
            writer.writerow([])
            #column of file 
            count = 1
            writer.writerow(['NO',' CHEMICAL NAME ','COMPANY','QUANTITY','UNIT','SHELF','CABINATE','FREEZER','EXPIRE DATE'])
            for chemical in animalChemical:
                writer.writerow([count ,chemical.chemical.name, chemical.chemical.company, chemical.available, chemical.chemical.unit, chemical.shelf, chemical.cabinate, chemical.temprature, chemical.expireDate])
                count+=1
            return response  
    
    elif dept == 'plant':
        response = HttpResponse(content_type = 'text/csv')
        response['content-diposition'] = 'attachment; filename = Plantchemicals.csv'

        #create csv writer
        writer = csv.writer(response)
        date = datetime.datetime.now()
        plantChemical = PlantStore.objects.filter( expireDate__gt= date )
        writer.writerow([])
        writer.writerow(['','','Plant Bio Technology "Available" Chemicals','','',date])
        writer.writerow([])
        #column of file 
        count = 1
        writer.writerow([' CHEMICAL NAME ','COMPANY','QUANTITY','UNIT','SHELF','CABINATE','FREEZER','EXPIRE DATE'])
        for chemical in plantChemical:
            writer.writerow([count,chemical.chemical.name, chemical.chemical.company, chemical.available, chemical.chemical.unit, chemical.shelf, chemical.cabinate, chemical.temprature, chemical.expireDate])
            count+=1
        return response    
    
    elif dept == 'microbial':
        # if request.method =='POST' and 'csv' in request.POST: 
            # start = request.POST['start']
            # to = request.POST['to']
            # response = HttpResponse(content_type = 'text/csv')
            # response['content-diposition'] = 'attachment; filename = Microbialchemicals.csv'

            # #create csv writer
            # writer = csv.writer(response)
            # date = datetime.datetime.now()
            # microbialChemical = MicrobialStore.objects.filter( recievedDate__range=[start,to] )
            # print(microbialChemical)
            # microbialChemical.filter(expireDate__gt= date)
            # print(microbialChemical)
            # writer.writerow([])
            # writer.writerow(['','','Microbial Bio Technology "Available" Chemicals','','',date])
            # writer.writerow([])
            # #column of file
            # count = 1 
            # writer.writerow(['NO',' CHEMICAL NAME ','COMPANY','QUANTITY','UNIT','SHELF','CABINATE','FREEZER','EXPIRE DATE'])
            # for chemical in microbialChemical:
            #     writer.writerow([count,chemical.chemical.name, chemical.chemical.company, chemical.available, chemical.chemical.unit, chemical.shelf, chemical.cabinate, chemical.temprature, chemical.expireDate])
            #     count+=1
            # return response  
        if request.method =='POST' and 'allcsv' in request.POST: 
            start = request.POST['start']
            to = request.POST['to']  
            response = HttpResponse(content_type = 'text/csv')
            response['content-diposition'] = 'attachment; filename = Microbialchemicals.csv'

            #create csv writer
            writer = csv.writer(response)
            date = datetime.datetime.now()
            microbialChemical = MicrobialStore.objects.filter( recievedDate__range=[start,to] )
            microbialChemical.all()
            writer.writerow([])
            writer.writerow(['','','Microbial Bio Technology "All" Chemicals','','',date])
            writer.writerow(['From',start,'-',to])
            writer.writerow([])
            #column of file
            count = 1 
            writer.writerow(['NO',' CHEMICAL NAME ','COMPANY','QUANTITY','UNIT','SHELF','CABINATE','FREEZER','EXPIRE DATE'])
            for chemical in microbialChemical:
                writer.writerow([count,chemical.chemical.name, chemical.chemical.company, chemical.available, chemical.chemical.unit, chemical.shelf, chemical.cabinate, chemical.temprature, chemical.expireDate])
                count+=1
            return response  

# Expired Chemical Report
def csvEChemicalReport(request,dept):
    if dept == 'animal':
        response = HttpResponse(content_type = 'text/csv')
        response['content-diposition'] = 'attachment; filename = AnimalEchemicals.csv'

        #create csv writer
        writer = csv.writer(response)
        
        date = datetime.datetime.now()
    
        animalChemical = AnimalStore.objects.filter( expireDate__lt= date)
        
        writer.writerow([])
        writer.writerow(['','','Animal Bio Technology "EXPIRED" Chemicals','','',''])
        writer.writerow([])
        #column of file 
        count = 1
        writer.writerow(['NO',' CHEMICAL NAME ','COMPANY','QUANTITY','UNIT','SHELF','CABINATE','FREEZER','EXPIRE DATE'])
        for chemical in animalChemical:
            writer.writerow([count,chemical.chemical.name, chemical.chemical.company, chemical.available, chemical.chemical.unit, chemical.shelf, chemical.cabinate, chemical.temprature, chemical.expireDate])
            count+=1
        return response    
    
    elif dept == 'plant':
        response = HttpResponse(content_type = 'text/csv')
        response['content-diposition'] = 'attachment; filename = Plantchemicals.csv'

        #create csv writer
        writer = csv.writer(response)
        date = datetime.datetime.now()
        plantChemical = PlantStore.objects.filter( expireDate__lt= date)
        writer.writerow([])
        writer.writerow(['','','Plant Bio Technology "EXPIRED" Chemicals','','',''])
        writer.writerow([])
        #column of file 
        count = 1
        writer.writerow(['NO',' CHEMICAL NAME ','COMPANY','QUANTITY','UNIT','SHELF','CABINATE','FREEZER','EXPIRE DATE'])
        for chemical in plantChemical:
            writer.writerow([count,chemical.chemical.name, chemical.chemical.company, chemical.available, chemical.chemical.unit, chemical.shelf, chemical.cabinate, chemical.temprature, chemical.expireDate])
            count+=1
        return response    
    
    elif dept == 'microbial':
        response = HttpResponse(content_type = 'text/csv')
        response['content-diposition'] = 'attachment; filename = Microbialchemicals.csv'

        #create csv writer
        writer = csv.writer(response)
        date = datetime.datetime.now()
        microbialChemical = MicrobialStore.objects.filter( expireDate__lt= date)
        writer.writerow([])
        writer.writerow(['','','Microbial Bio Technology "EXPIRED" Chemicals','','',''])
        writer.writerow([])
        #column of file
        count = 1 
        writer.writerow(['No',' CHEMICAL NAME ','COMPANY','QUANTITY','UNIT','SHELF','CABINATE','FREEZER','EXPIRE DATE'])
        for chemical in microbialChemical:
            writer.writerow([count,chemical.chemical.name, chemical.chemical.company, chemical.available, chemical.chemical.unit, chemical.shelf, chemical.cabinate, chemical.temprature, chemical.expireDate])
            count+=1
        return response    


# Desposed Chemical Report
def csvDChemicalReport(request,dept):
    if dept == 'animal':
        if request.method =='POST' and 'csv' in request.POST: 
            start = request.POST['start']
            to = request.POST['to']
            print(start,to)
            response = HttpResponse(content_type = 'text/csv')
            response['content-diposition'] = 'attachment; filename = Animalchemicals.csv'

            #create csv writer
            writer = csv.writer(response)
            
            date = datetime.datetime.now()
        
            animalChemical = AnimalDesposedChemical.objects.filter(  desposedDate__range=[start,to] )
            animalChemical = animalChemical.filter(desposed= True)
            print(animalChemical)
            writer.writerow([])
            writer.writerow(['','','Animal Bio Technology "DESPOSED" Chemicals','','',''])
            writer.writerow([])
            #column of file 
            count = 1
            writer.writerow(['NO',' CHEMICAL NAME ','COMPANY','QUANTITY','UNIT','SHELF','CABINATE','FREEZER','EXPIRE DATE','DESPOSED DATE'])
            for chemical in animalChemical:
                writer.writerow([count,chemical.chemical.name, chemical.chemical.company, chemical.available, chemical.chemical.unit, chemical.shelf, chemical.cabinate, chemical.temprature, chemical.expireDate, chemical.desposedDate])
                count+=1
            return response  

        elif request.method =='POST' and 'pdf' in request.POST:
            # buf = io.BytesID()
            # c = canvas.Canvas(buf, pagesize=letter,bottomup = 0)
            # #text object
            # texttob = c.beginText()
            # textob.setTextOrigion(inch, inch)
            # textob.setFont("Helvetica",14)
            # # add lines of text
            # lines = [
            #     "tesdfsadf"
            # ]
            # for line in lines:
            #     textob.textline(line)
            
            # d.drawText(textob)
            # c.showPage()
            # c.save()
            # buf.seek(0)

            # #return
            # return FileResponse(buf, as_attachment=True , filename = 'animalsdesposed.pdf')
          
            # # response = HttpResponse(content_type = 'text/csv')
            # # response['content-diposition'] = 'attachment; filename = Animalchemicals.csv'

            # # #create csv writer
            # # writer = csv.writer(response)
            
            # # date = datetime.datetime.now()
        
            # # animalChemical = AnimalDesposedChemical.objects.filter( desposed= True)
            
            # # writer.writerow([])
            # # writer.writerow(['','','Animal Bio Technology "DESPOSED" Chemicals','','',''])
            # # writer.writerow([])
            # # #column of file 
            # # count = 1
            # # writer.writerow(['NO',' CHEMICAL NAME ','COMPANY','QUANTITY','UNIT','SHELF','CABINATE','FREEZER','EXPIRE DATE','DESPOSED DATE'])
            # # for chemical in animalChemical:
            # #     writer.writerow([count,chemical.chemical.name, chemical.chemical.company, chemical.available, chemical.chemical.unit, chemical.shelf, chemical.cabinate, chemical.temprature, chemical.expireDate, chemical.desposedDate])
            # #     count+=1
            # # return response  
            return redirect('aDesposedChemical') 
    
    elif dept == 'plant':
        if request.method =='POST' and 'csv' in request.POST: 
            start = request.POST['start']
            to = request.POST['to']
            response = HttpResponse(content_type = 'text/csv')
            response['content-diposition'] = 'attachment; filename = Plantchemicals.csv'

            #create csv writer
            writer = csv.writer(response)
            date = datetime.datetime.now()
            plantChemical = PlantDesposedChemical.objects.filter( desposedDate__range=[start,to])
            plantChemical=plantChemical.filter(desposed= True)
            writer.writerow([])
            writer.writerow(['','','Plant Bio Technology "DESPOSED" Chemicals','','',''])
            writer.writerow([])
            #column of file 
            count = 1
            writer.writerow(['NO',' CHEMICAL NAME ','COMPANY','QUANTITY','UNIT','SHELF','CABINATE','FREEZER','EXPIRE DATE','DESPOSED DATE'])
            for chemical in plantChemical:
                writer.writerow([count,chemical.chemical.name, chemical.chemical.company, chemical.available, chemical.chemical.unit, chemical.shelf, chemical.cabinate, chemical.temprature, chemical.expireDate, chemical.desposedDate])
                count+=1
            return response    
    
    elif dept == 'microbial':
         if request.method =='POST' and 'csv' in request.POST: 
            start = request.POST['start']
            to = request.POST['to']
            response = HttpResponse(content_type = 'text/csv')
            response['content-diposition'] = 'attachment; filename = Microbialchemicals.csv'

            #create csv writer
            writer = csv.writer(response)
            date = datetime.datetime.now()
            microbialChemical = MicrobialDesposedChemical.objects.filter( desposedDate__range=[start,to])
            microbialChemical.filter(desposed = True)
            writer.writerow([])
            writer.writerow(['','','Microbial Bio Technology "DESPOSED" Chemicals','','',''])
            writer.writerow([])
            #column of file
            count = 1 
            writer.writerow(['No',' CHEMICAL NAME ','COMPANY','QUANTITY','UNIT','SHELF','CABINATE','FREEZER','EXPIRE DATE','DESPOSED DATE'])
            for chemical in microbialChemical:
                writer.writerow([count,chemical.chemical.name, chemical.chemical.company, chemical.available, chemical.chemical.unit, chemical.shelf, chemical.cabinate, chemical.temprature, chemical.expireDate, chemical.desposedDate])
                count+=1
            return response    
