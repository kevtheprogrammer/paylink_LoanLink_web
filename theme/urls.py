from django.urls import path
from . import views

urlpatterns = [
    path('staff', views.Dashboard, name='staff' ),
    path('clients',views.AllClients, name='clients'),
    path('client_details', views.ClientDetails, name='client_details'),
    path('reports', views.Reports, name='reports'),
    path('loans', views.Loans, name='loans'),
    path('closed-loans', views.ClosedLoans, name='closed-loans'),
    path('active-loans', views.ActiveLoans, name='active-loans'),
    path('pending-loans', views.PendingLoans, name='pending-loans'),
]