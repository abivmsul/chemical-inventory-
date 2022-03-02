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
