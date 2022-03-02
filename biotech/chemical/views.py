from django.shortcuts import render,get_object_or_404,redirect
from .models import Chemical,RequestChemical,Request
from account.models import Researcher
from department.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required 
from django.views.generic import View
from django.contrib import messages
from chemical.forms import AddChemicalForm
from . import models
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
   
    context = {}
    return render(request, 'department/department_home.html', context)

@login_required(login_url='login')
def directorHomeView (request):  
   
    context = {}
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
    requests = Request.objects.filter(requested= True, deptRequest=True, department = 'Microbial Biotechnology' )

    context = { 'page': page, 'obj': requests}
    return render(request, 'department/view_requests.html', context)

@login_required(login_url='login')
def plantRequestsOfDepartment (request):
    page = 'plant'
    requests = Request.objects.filter(requested= True, deptRequest=False, department = 'Plant Biotechnology' )

    context = { 'page': page, 'obj': requests}
    return render(request, 'department/view_requests.html', context)


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
    requests = Request.objects.get(id = pk)
    requested_chemicals = requests.chemicals.get(id = ck)
    #for chemical in requested_chemicals:
        # print(chemical.chemical.id)
        # print(requests.user.department.department)
        # if requests.user.department.department == 'Animal Biotechnolgy':
    animal = AnimalStore.objects.get(chemical_id = requested_chemicals.chemical.id ) 
    # store = animal[0]   
    # print(chemical.chemical.id)
    context = {'obj': requests,'store':animal , 'che':requested_chemicals, 'page':page}        
    return render(request, 'custodian/d_request_detail.html',context)

@login_required(login_url='login')
def plantdRequestDetal(request,pk,ck):
    page = 'plant'
    requests = Request.objects.get(id = pk)
    requested_chemicals = requests.chemicals.get(id = ck)
    #for chemical in requested_chemicals:
        # print(chemical.chemical.id)
        # print(requests.user.department.department)
        # if requests.user.department.department == 'Animal Biotechnolgy':
    plant = PlantStore.objects.get(chemical_id = requested_chemicals.chemical.id ) 
    # store = animal[0]   
    # print(chemical.chemical.id)
    context = {'obj': requests,'store':plant , 'che':requested_chemicals, 'page':page}        
    return render(request, 'custodian/d_request_detail.html',context)

@login_required(login_url='login')
def microbialdRequestDetal(request,pk,ck):
    page = 'microbial'
    requests = Request.objects.get(id = pk)
    requested_chemicals = requests.chemicals.get(id = ck)
    #for chemical in requested_chemicals:
        # print(chemical.chemical.id)
        # print(requests.user.department.department)
        # if requests.user.department.department == 'Animal Biotechnolgy':
    microbial = MicrobialStore.objects.get(chemical_id = requested_chemicals.chemical.id ) 
    # store = animal[0]   
    # print(chemical.chemical.id)
    context = {'obj': requests,'store':microbial , 'che':requested_chemicals, 'page':page}        
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
            store = AnimalStore.objects.get(chemical_id = chemical.chemical.id)
            print(store.available)
            store.available = int(store.available) + int(quantity)
            store.expireDate = exdate
            store.cabinate = cabinate
            store.shelf = shelf
            store.save()
            chemical.save()
            requests.save()
            next = request.POST.get('next', '/')
            return redirect(next)

        elif requests.department == 'Plant Biotechnology':
            store = PlantStore.objects.get(chemical_id = chemical.chemical.id)
            print(store.available)
            store.available = int(store.available) + int(quantity)
            store.expireDate = exdate
            store.cabinate = cabinate
            store.shelf = shelf
            store.save()
            chemical.save()
            requests.save()
            next = request.POST.get('next', '/')
            return redirect(next)

        elif requests.department == 'Microbial Biotechnology':
            store = MicrobialStore.objects.get(chemical_id = chemical.chemical.id)
            print(store.available)
            store.available = int(store.available) + int(quantity)
            store.expireDate = exdate
            store.cabinate = cabinate
            store.shelf = shelf
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
    chemicals = AnimalStore.objects.all( )

    context = { 'page': page, 'obj': chemicals}
    return render(request, 'custodian/chemicals.html', context)

def microbialChemicals (request):
    page = 'microbial'
    chemicals = MicrobialStore.objects.all( )

    context = { 'page': page, 'obj': chemicals}
    return render(request, 'custodian/chemicals.html', context)

def plantChemicals (request):
    page = 'plant'
    chemicals = PlantStore.objects.all( )

    context = { 'page': page, 'obj': chemicals}
    return render(request, 'custodian/chemicals.html', context)

# Chemicallsssss LIstsssss
def chemicalList (request):
    form = AddChemicalForm()
    if request.method =='POST':
        form = AddChemicalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('chemicalList')
    context = {'chemical': Chemical.objects.all, 'form': form }
    return render(request, 'chemical_list.html', context)

def animalchemicalList (request):
    page = 'animal'
    context = {'page':page ,'chemical': AnimalStore.objects.all}
    return render(request, 'chemical_list.html', context)
def plantchemicalList (request):
    page = 'plant'
    context = {'page':page ,'chemical': PlantStore.objects.all}
    return render(request, 'chemical_list.html', context)
def microbialchemicalList (request):
    page = 'microbial'
    context = {'page':page ,'chemical': MicrobialStore.objects.all}
    return render(request, 'chemical_list.html', context)

def chemicalDetail (request,pk):
    context = {'chemical': Chemical.objects.get(id = pk)}
    return render(request, 'chemical_detail.html', context)


def addQuantity(request, pk):
    chemical = get_object_or_404(Chemical, id = pk)
   # request_chemical, created = requestchemical.objects.get_or_create(chemical=chemical,user=request.user,requested=False)
    request_chemical, created = RequestChemical.objects.get_or_create(chemical=chemical,user=request.user,requested=False)
    if request.method =='POST':
        quantity = request.POST.get('quantity')
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
        requested_chemicals = requests.chemicals.all()
        requested_chemicals.update(requested=True)
        for chemical in requested_chemicals:
            chemical.save()

        requests.requested = True
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
