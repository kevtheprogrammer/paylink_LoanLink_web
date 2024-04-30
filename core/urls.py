from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
     path('admin-dashboard/', TemplateView.as_view(template_name='core/admin_dashboard.html'), name='admin-dashboard'),
     path('clients', views.ClientListView, name='clients'),
]
