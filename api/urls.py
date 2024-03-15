from django.urls import path
from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from account.views import *

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='signup'),
    path('sign-in/', SignInView.as_view(), name='signin'),
    path('user-details/', UserDetailsView.as_view(), name='user-details'),
    path('user-update/', UserUpdateView.as_view(), name='user-update'),
    path('get-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('get-token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
