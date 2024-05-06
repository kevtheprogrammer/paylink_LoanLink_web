from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
     path('login/', views.LoginView, name='login'),
     path('admin-dashboard/', views.AdminDasboard, name='admin-dashboard'),
     path('clients', views.ClientListView, name='clients'),
     path('active_loans', views.ActiveClientListView, name='active_loans'),
     path('pending_loans', views.PendingLoansView, name='pending_loans'),
     path('pending_loans/<int:client_id>/', views.ApproveLoan, name='pending_loans'),
     path('reject_loans/<int:client_id>/', views.RejectLoan, name='reject_loans'),
     path('closed_loans', views.ClosedLoansView, name='closed_loans'),
     path('rejected_loans', views.RejectedLoansView, name='rejected_loans'),
     path('client_details', views.ClientDetailsView, name='client_details'),
     path('client_details/<int:client_id>/', views.ClientDetailsView, name='client_details'),
     path('client/<int:client_id>/verify/', views.verify_user, name='verify_user'),
     path('loan_details/<int:client_id>/', views.LoanDetailsView, name='loan_details'),
     path('search_client', views.SearchClient, name='search_client'),
     
]
