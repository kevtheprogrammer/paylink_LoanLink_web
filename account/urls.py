from django.urls import path, include
from django.contrib.auth.decorators import login_required

from .views import *

app_name = 'account'

urlpatterns = [

    path('', login_required(DashboardView.as_view()), name='dashboard'),
    path('users-list/', login_required(UserListView.as_view()), name='users'),
    path('user_detail/<int:pk>/',
         login_required(UserDetailView.as_view()), name='user-details'),
    path('verify-user/<int:pk>/',
         login_required(togleVerifyUser), name='togle-verify')
]
