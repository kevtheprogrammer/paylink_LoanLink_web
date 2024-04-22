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
    
    # path('loans/', LoanListView.as_view({'get': 'list', 'post': 'create'})),
    # path('loans/<int:id>/', LoanListView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    # path('loans/approve-loan/<uuid:pk>/', LoanUpdateViewSet.as_view({'post': 'update'})),

    # path('loans/disbursement-of-funds/<uuid:loan_id>/', DisbursementOfFunds.as_view({'post': 'loan_disbursement'}), name='disbursement-of-funds'),

    # path('loans/active/', ActiveLoanListViewset.as_view({'get': 'list'})),
    # path('loans/<str:loan_id>', ActiveLoanListViewset.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy' })),

    # path('loans/pending/', PendingLoanListViewset.as_view({'get': 'list'})),
    # path('loans/<str:loan_id>', PendingLoanListViewset.as_view({'get': 'retrieve', 'put': 'update','delete': 'destroy'})),

    # path('loans/closed/', ClosedLoanListViewset.as_view({'get': 'list'}), name='closeloans'),
    # path('loans/<str:loan_id>', ClosedLoanListViewset.as_view({'get': 'retreive', 'put': 'update', 'delete': 'destroy'}), name='closeloans'),

    # path('loans/rejected/', RejectedLoanListViewest.as_view({'get': 'list'}), name='rejectedloan'),
    # path('loans/<str:loan_id>', RejectedLoanListViewest.as_view({'get': 'retreive', 'put': 'update', 'delete': 'destroy'}), name='rejectedloansid'),

    # path('loans/approved/', ApprovedLoanListView.as_view({'get': 'list'}), name='approvedloans'),
    # path('loans/<str:loan_id>', ApprovedLoanListView.as_view({'get': 'retreive', 'put': 'update', 'delete': 'destroy'}), name='approvedloansid'),

    # path('creditscore/', CreditScoreSerializerViewset.as_view({'get': 'list', 'post': 'create'}), name='creditscore'), 
    # path('creditscore/<str:client_id>/', CreditScoreSerializerViewset.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='creditscoreid'),

    # path('transaction/',  LoanTransactionSerializerView.as_view({'get': 'list', 'post': 'create'})),
    # path('transaction/<str:loan_id>', LoanTransactionSerializerView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='loan-transactions'),

]
