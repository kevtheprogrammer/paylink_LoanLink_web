from django.urls import path
from . import views

urlpatterns = [
    path('login', views.Login, name='login'),
    path('staff', views.Dashboard, name='staff' ),
    path('clients',views.AllClients, name='clients'),
    path('client_details/<int:client_id>/', views.ClientDetails, name='client_details'),
    path('reports', views.Reports, name='reports'),
    path('loans', views.Loans, name='loans'),
    path('closed-loans', views.ClosedLoans, name='closed-loans'),
    path('active-loans', views.ActiveLoans, name='active-loans'),
    path('pending-loans', views.PendingLoans, name='pending-loans'),
    path('create-client', views.CreatClient, name='create-client'),
    path('attach-client', views.AttachClient, name='attach-client'),
    path('created-client', views.CreateClientView, name='created-client'),
    path('client-attachement/<int:client_id>/', views.ClientAttachement, name='client-attachement'),
    path('create-loan', views.CreateLoan, name="create-loan"),
    path('pass-clientID/<int:client_id>/', views.passIDToAddLoan, name="pass-clientID"),
    path('get-loan-product', views.ListLoanProducts, name="get-loan-product"),
    path('profile', views.Profile, name="profile"),
    path('upload-clients', views.UploadBulkClientTemplate, name='upload-clients'),
    path('bulk-client-template', views.CreateExcelTemplate, name="bulk-client-template"),
    path('bulk-client-view', views.BulkClientUploadView, name='bulk-client-view'),
    path('create-loan-product', views.CreateLoanProduct, name='create-loan-product'),
    path('new-loan-product', views.NewLoanProduct, name='new-loan-product')
]
