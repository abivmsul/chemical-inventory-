from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='Researcher').exists():
            return redirect('researcherhome')
        elif request.user.groups.filter(name='Custodian').exists():
                return redirect('custodianhome')
        elif request.user.groups.filter(name='Department').exists():
                return redirect('departmenthome')        
        elif request.user.groups.filter(name='Director').exists():
                return redirect('directorhome')  
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func



