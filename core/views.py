from django.shortcuts import render
from account.models import *
from django.http import HttpResponse

def ClientListView(request):
    clients = User.objects.all()
    print(clients)
    return render(request, 'core/clients.html', {'clients': clients})
