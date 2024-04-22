from django.urls import path, include
from .views import  homepage, upload_users_csv
# from .views import process_csv
from rest_framework.routers import DefaultRouter
from django.contrib.auth.views import LogoutView
from accounts.views import logout_view, SignUpView, UserListView, UserDetailView, register_user, user_login


urlpatterns = [
    
    path('', homepage, name="homepage"),
    
    path('upload_csv/', upload_users_csv, name='upload_csv' ),
    path('logout/', logout_view, name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),

    path('users-list/', UserListView.as_view(), name='users-list'),
    path('user-detail/<int:pk>/', UserDetailView.as_view(), name='user'),
    path('user/<int:pk>/delete/', UserDetailView.as_view(), name='delete-user'),

    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),








    
]
