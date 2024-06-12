from django.urls import path,include
from .views import ClientRegistrationView,AgentRegistrationView,UserLoginView, ClientListViewset, UserListViewset

urlpatterns = [
	path('signup/client/', ClientRegistrationView.as_view(),name='signup_client'),
	path('signup/agent/', AgentRegistrationView.as_view(),name='signup_agent'),
	path('signin/', UserLoginView.as_view(), name='signin'),
	path('clientlist/', ClientListViewset.as_view({'get': 'list'}), name='client-list'),
	path('userlist/', UserListViewset.as_view({'get': 'list'}), name='client-list'),
]
