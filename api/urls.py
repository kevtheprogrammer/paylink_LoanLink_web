from django.urls import path, include
from .views import *
from .views import *
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('clientview',CleintUserViewSet, basename='clientview')


urlpatterns = [
    # path('/', include(router.urls)),
    path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('user/<int:id>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    
    path('clients/', CleintUserViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('client/<int:id>/', CleintUserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    
    path('creditscore/', CreditScoreSerializerViewset.as_view({'get': 'list', 'post': 'create'}), name='creditscore'), 
    path('creditscore/<int:id>/', CreditScoreSerializerViewset.as_view({ 'get': 'retrieve_base', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='creditscoreid'),
    path('creditscore/<int:client_employee_number>/employee/', CreditScoreSerializerViewset.as_view({'get': 'retrieve', }), name='creditscoreid'),

    path('loans/', LoanListView.as_view({'get': 'list', 'post': 'create'})),
    path('loans/<int:id>/', LoanListView.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('loans/<str:loan_status>/', FilterLoansByStatus.as_view({'get': 'list',    })),

    path('loan/approve/<int:id>/', LoacActionViewSet.as_view({'get': 'approve_loan'    })),
    path('loan/activate/<int:id>/', LoacActionViewSet.as_view({'get': 'activate_loan'    })),

    # path('loans/approve-loan/<uuid:pk>/', LoanUpdateViewSet.as_view({'post': 'update'})),

    # path('loans/disbursement-of-funds/<uuid:loan_id>/', DisbursementOfFunds.as_view({'post': 'loan_disbursement'}), name='disbursement-of-funds'),

   

    path('txns/',  LoanTransactionSerializerView.as_view({'get': 'list', 'post': 'create'})),
    path('txns/<int:id>', LoanTransactionSerializerView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='loan-transactions'),

]
