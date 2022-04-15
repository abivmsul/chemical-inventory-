from django.shortcuts import render, redirect
from django.contrib import messages, auth
from account.decorators import unauthenticated_user
from django.contrib.auth.models import Group
from account.forms import CreateUserForm,ResearcherForm,DeptForm
from account.models import Researcher,Department,Custodian
from django.contrib.auth.models import User
from django.core.mail import send_mail
# Create your views here.

@unauthenticated_user
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            if request.user.groups.filter(name='Researcher').exists():
                return redirect('researcherhome')
            elif request.user.groups.filter(name='Custodian').exists():
                return redirect('custodianhome')
            elif request.user.groups.filter(name='Department').exists():
                return redirect('departmenthome')
            elif request.user.groups.filter(name='Director').exists():
                return redirect('directorhome')
            else:
                messages.warning(request, 'Invalid credentials')
                return redirect('login')

            
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def registerPage(request):
    rform = ResearcherForm()
    if request.method =='POST':
        rform = ResearcherForm(request.POST)
        form = CreateUserForm(request.POST)
        
        if rform.is_valid():
            print("sad")
            username = request.POST['username']
            email = request.POST['email']
            password = User.objects.make_random_password(length=8,allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789')
            print(password)
            user = User.objects.create_user(username=username, password=password, email=email)    
            user.save()
            department = rform.cleaned_data.get('department')
            group = Group.objects.get(name = 'Researcher')
            user.groups.add(group)
            Researcher.objects.create( researcher = user , name = user.username, department = department)
            messages.success(request, 'Account was created for ' + username)
            # send_mail(
            #     'Login details',
            #     'Here is your login details \n username : ' + username + '\n password : ' + password,
            #     from_email=None,
            #     recipient_list=[email],
            #     fail_silently=False,
            # )
            # messages.success(message="Email has been sent to " + email + ".")
            return redirect('login')

            # user = form.save()
            # #researcher = rform.save()
            # username = form.cleaned_data.get('username')
            # department = rform.cleaned_data.get('department')
            # print(request.POST)
            # print(department)
            # group = Group.objects.get(name = 'Researcher')
            # user.groups.add(group)
            # Researcher.objects.create( researcher = user , name = user.username, department = department)
            # messages.success(request, 'Account was created for ' + username)
            # return redirect ('login')
    context = {'rform':rform}
    return render(request, 'register.html', context)

def addUser(request):
    dform = DeptForm()
    if request.method =='POST' and 'dept' in request.POST: 
        dform = DeptForm(request.POST)        
        if dform.is_valid():
            print("sad")
            username = request.POST['username']
            email = request.POST['email']
            password = User.objects.make_random_password(length=8,allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789')
            print(password)
            user = User.objects.create_user(username=username, password=password, email=email)    
            user.save()
            department = dform.cleaned_data.get('department')
            group = Group.objects.get(name = 'Department')
            user.groups.add(group)
            Department.objects.create( departments = user , name = user.username, department = department)
            messages.success(request, 'Account was created for ' + username)
            send_mail(
                'Login details',
                'Here is your login details \n username : ' + username + '\n password : ' + password,
                'abivmsul24@gmail.com',
                recipient_list=[email],
                fail_silently=False,
            )
            messages.success(request,"Email has been sent to " + email + ".")
            next = request.POST.get('next', '/')
            return redirect(next)
   
    elif request.method =='POST' and 'res' in request.POST: 
            print("sad")
            print(request.user.department.department)
            username = request.POST['username']
            email = request.POST['email']
            password = User.objects.make_random_password(length=8,allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789')
            print(password)
            user = User.objects.create_user(username=username, password=password, email=email)    
            user.save()
            group = Group.objects.get(name = 'Researcher')
            user.groups.add(group)
            Researcher.objects.create( researcher = user , name = user.username, department = request.user.department.department)
            
            messages.success(request, 'Account was created for ' + username)
            send_mail(
                'Login details',
                'Here is your login details \n username : ' + username + '\n password : ' + password,
                'abivmsul24@gmail.com',
                recipient_list=[email],
                fail_silently=False,
            )
            messages.success(request,"Email has been sent to " + email + ".")
            next = request.POST.get('next', '/')
            return redirect(next)
    
    elif request.method =='POST' and 'custodian' in request.POST:       
        
            print("sad")
            username = request.POST['username']
            email = request.POST['email']
            password = User.objects.make_random_password(length=8,allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789')
            print(password)
            user = User.objects.create_user(username=username, password=password, email=email)    
            user.save()
            group = Group.objects.get(name = 'Custodian')
            user.groups.add(group)
            Custodian.objects.create( custodian = user , name = user.username)
            messages.success(request, 'Account was created for ' + username)
            # send_mail(
            #     'Login details',
            #     'Here is your login details \n username : ' + username + '\n password : ' + password,
            #     from_email=None,
            #     recipient_list=[email],
            #     fail_silently=False,
            # )
            # messages.success(message="Email has been sent to " + email + ".")
            next = request.POST.get('next', '/')
            return redirect(next)
    context = {'dform':dform }
    return render(request,'director/add_user.html', context)


def logout(request):
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return render(request, 'login.html')

def animalResearcher(request):
    page = 'animal'
    animalResearcher = Researcher.objects.filter(department = 'Animal Biotechnology')

    context = { 'page': page , 'animalResearcher': animalResearcher}
    return render(request, 'department/researchers.html',context )

def plantResearcher(request):
    page = 'plant'
    plantResearcher = Researcher.objects.filter(department = 'Plant Biotechnology')

    context = { 'page': page , 'plantResearcher': plantResearcher}
    return render(request, 'department/researchers.html',context )

def microbialResearcher(request):
    page = 'microbial'
    microbialResearcher = Researcher.objects.filter(department = 'Microbial Biotechnology')

    context = { 'page': page , 'microbialResearcher': microbialResearcher}
    return render(request, 'department/researchers.html',context )

def programCoordinator(request):
    dform = DeptForm()
    departments = Department.objects.all()
    print(departments)
    context = { 'department':departments,'dform':dform }
    return render(request, 'director/program_coordinators.html', context)

def programCoordinatorDetail(request,pk):
    programCoordinator = Department.objects.get(id = pk)

    context = {'programCoordinator': programCoordinator}
    return render(request, 'director/program_coordinator_detail.html',context )

def researcherDetail(request,pk):
    researcher = Researcher.objects.get(id = pk)

    context = {'researcher': researcher}
    return render(request, 'department/researcher_detail.html',context )

def custodian(request):
    custodian = Custodian.objects.all()
    # print(departments)
    context = { 'custodians':custodian }
    return render(request, 'director/custodians.html', context)

def custodianDetail(request,pk):
    custodian =Custodian.objects.get(id = pk)

    context = {'custodian': custodian}
    return render(request, 'director/custodian_detail.html',context )


def give(request,pk):
    researcher = Researcher.objects.get(id = pk)
    researcher.permission = True
    researcher.save()
    next = request.GET.get('next', '/')
    return redirect(next)

def revoke(request,pk):
    researcher = Researcher.objects.get(id = pk)
    researcher.permission = False
    researcher.save()
    next = request.GET.get('next', '/')
    return redirect(next)
    
def disableresearcher(request,pk):
    researcher = Researcher.objects.get(id = pk)
    researcher.researcher.is_active = False
    researcher.researcher.save()
    next = request.GET.get('next', '/')
    return redirect(next)

def disabledepartment(request,pk):
    pLeader = Department.objects.get(id = pk)
    pLeader.departments.is_active = False
    pLeader.departments.save()
    next = request.GET.get('next', '/')
    return redirect(next)
   
def disablecustodian(request,pk):
    custodian = Custodian.objects.get(id = pk)
    custodian.custodian.is_active = False
    custodian.custodian.save()
    next = request.GET.get('next', '/')
    return redirect(next)
   

def enableresearcher(request,pk):
    researcher = Researcher.objects.get(id = pk)
    researcher.researcher.is_active = True
    researcher.researcher.save()
    next = request.GET.get('next', '/')
    return redirect(next)

def enabledepartment(request,pk):
    pLeader = Department.objects.get(id = pk)
    pLeader.departments.is_active = True
    pLeader.departments.save()
    next = request.GET.get('next', '/')
    return redirect(next)
        
def enablecustodian(request,pk):
    custodian = Custodian.objects.get(id = pk)
    custodian.custodian.is_active = True
    custodian.custodian.save()
    next = request.GET.get('next', '/')
    return redirect(next)






##dsfsfdfsdfsdf--------------------
# def registerPage(request):
#     rform = ResearcherForm()
#     form = CreateUserForm()
#     if request.method =='POST':
#         rform = ResearcherForm(request.POST)
#         form = CreateUserForm(request.POST)
        
#         if rform.is_valid() and form.is_valid():
#             print("sad")
#             username = form.cleaned_data.get('username')
#             email = form.cleaned_data.get('email')
#             password = User.objects.make_random_password(length=8,
#                                                          allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789')
#             form.save()
#             user = User.objects.filter(username=username)
#             user.set_password(password)
#             user.save()
#             department = rform.cleaned_data.get('department')
#             print(request.POST)
#             print(department)
#             group = Group.objects.get(name = 'Researcher')
#             user.groups.add(group)
#             Researcher.objects.create( researcher = user , name = user.username, department = department)
#             messages.success(request, 'Account was created for ' + username)
#             # send_mail(
#             #     'Login details',
#             #     'Here is your login details \n username : ' + username + '\n password : ' + password,
#             #     from_email=None,
#             #     recipient_list=[email],
#             #     fail_silently=False,
#             # )
#             # messages.success(message="Email has been sent to " + email + ".")
#             return redirect('login')

#             # user = form.save()
#             # #researcher = rform.save()
#             # username = form.cleaned_data.get('username')
#             # department = rform.cleaned_data.get('department')
#             # print(request.POST)
#             # print(department)
#             # group = Group.objects.get(name = 'Researcher')
#             # user.groups.add(group)
#             # Researcher.objects.create( researcher = user , name = user.username, department = department)
#             # messages.success(request, 'Account was created for ' + username)
#             # return redirect ('login')
#     context = { 'form': form , 'rform':rform}
#     return render(request, 'register.html', context)
