from django.shortcuts import render

# Create your views here.
    
@login_required(login_url='login')
def animalRequests (request):
    page = 'animal'
    requests = Request.objects.filter(requested = True, confirmed = True,  department = 'Animal Biotechnology' )
    
    context = { 'page': page, 'obj': requests}
    return render(request, 'custodian/view_requests.html', context)

