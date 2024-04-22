from django.urls import path
from .views import *
 
# from accounts.views import UploadCSVViewSet
from accounts.auth import CustomLoginView
from accounts.views import *


urlpatterns = [
    #user Urls,
    path('login/', CustomLoginView.as_view(), name='login'),
  
    # new 
    path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('user/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    
    path('tickets/', TicketViewSet.as_view({'get': 'list', 'post' : 'create'})),
    path('ticket/<int:pk>/', TicketViewSet.as_view({'get':'retrieve', 'put' : 'update', 'delete' : 'destroy'})),
    
    # path('upload/', UploadCSVViewSet.as_view, name='upload'),
    # path('upload_csv/', import_csv, name='upload_csv'),

    # path('products/', ProductViewSet.as_view({'get': 'list', 'post' : 'create'})),
    # path('product/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve', 'put' : 'update', 'delete' : 'destroy'})),
    
    # path('invoices/', InvoiceViewSet.as_view({'get': 'list', 'post' : 'create'})),
    # path('invoice/<int:pk>/', InvoiceViewSet.as_view({'get': 'retrieve', 'put' : 'update', 'delete' : 'destroy'})),
    
    # path('companies/', CompanyViewSet.as_view({'get': 'list', 'post' : 'create'})),
    # path('company/<int:pk>/', CompanyViewSet.as_view({'get': 'retrieve', 'put' : 'update', 'delete' : 'destroy'})),
    
    # path('categories/', CategoryViewSet.as_view({'get': 'list', 'post' : 'create'})),
    # path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put' : 'update', 'delete' : 'destroy'})),

 
    # path('customers/', CustomerViewSet.as_view({'get': 'list', 'post' : 'create'})),
    # path('customer/<int:pk>/', CustomerViewSet.as_view({'get':'retrieve', 'put' : 'update', 'delete' : 'destroy'})),
    
    # path('sales/', SaleViewSet.as_view({'get': 'list', 'post' : 'create'})),
    # path('sale/<int:pk>/', SaleViewSet.as_view({'get':'retrieve', 'put' : 'update', 'delete' : 'destroy'})),

    # path('categories/', CategoryViewSet.as_view({'get': 'list', 'post' : 'create'})),
    # path('category/<int:pk>/', CategoryViewSet.as_view({'get':'retrieve', 'put' : 'update', 'delete' : 'destroy'})),

    # path('todos/', TodoViewSet.as_view({'get': 'list', 'post' : 'create'})),
    # path('todo/<int:pk>/', TodoViewSet.as_view({'get':'retrieve', 'put' : 'update', 'patch': 'update', 'delete' : 'destroy'})),

    # path('personslinfos/', PersonalInfoViewSet.as_view({'get': 'list', 'post' : 'create'})),
    # path('personInfo/<int:pk>/', PersonalInfoViewSet.as_view({'get':'retrieve', 'put' : 'update', 'patch': 'update', 'delete' : 'destroy'})),

    # path('qoatations/', PersonalInfoViewSet.as_view({'get': 'list', 'post' : 'create'})),
    # path('qoatations/<int:pk>/', PersonalInfoViewSet.as_view({'get':'retrieve', 'put' : 'update', 'patch': 'update', 'delete' : 'destroy'})),

     
]
