from django.shortcuts import render
from account.models import *
from loan.models import *
from account.models import *
from payment.models import *
from rest_framework import viewsets, status
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def Dashboard(request):
    return render(request, 'theme/admin_2.html')

def AllClients(request):
    return render(request, 'theme/clients.html')


def ClientDetails(request):
    return render(request, 'theme/client_details.html')

def Reports(request):
    return render(request, 'theme/reports.html')

def Loans(request):
    return render(request, 'theme/loans.html')


def ClosedLoans(request):
    return render(request, 'theme/closed_loans.html')


def ActiveLoans(request):
    return render(request, 'theme/active_loans.html')

def PendingLoans(request):
    return render(request, 'theme/pending_loans.html')



