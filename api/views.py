from account.models import ClientProfile
from loan.models import Loan
from account.models import ClientProfile
from account.models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets, status
from loan.models import Loan, CreditScore, LoanTransaction
from datetime import datetime
from django.core.mail import send_mail
from .serializers import *
from rest_framework.response import Response
from django.core.management.base import BaseCommand
from django.http import Http404, HttpResponse
from rest_framework.permissions import IsAuthenticated,AllowAny


 
class UserViewSet(viewsets.ViewSet):
    serializer = Userserializer
    model = User
    
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        
    def list(self, request):
        obj = self.model.objects.all()
        serializer = self.serializer(obj, many=True)
        return Response(serializer.data)
	
    def create(self, request):
        serializer = CreateBasicUserAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
    
    def retrieve(self, request, id=None):
        try:
            user = self.get_object(id)  # Use id instead of pk for consistency
        except User.DoesNotExist:
            return Response("User does not exist", status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer(user)  # Pass user instance to serializer
        return Response(serializer.data)
    
    def partial_update(self, request, id=None):
        try:
            user = self.get_object(id)
        except self.model.DoesNotExist:
            return Response("User does not exist", status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer(user, data=request.data, partial=True)  # Set partial=True for partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


 
    def update(self, request, id=None):
        try:
            user = self.get_object(id)
        except self.model.DoesNotExist:
            return Response("User does not exist", status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def destroy(self, request, id=None):
        try:
            user = self.get_object(id)
        except self.model.DoesNotExist:
            return Response("User does not exist", status=status.HTTP_404_NOT_FOUND)
        
        user.delete()
        user = self.model.objects.all()
        serializer = self.serializer(user, many=True)
        return Response({
            "message": "Deleted user object with success",
            "data": serializer.data,
        }, status=status.HTTP_204_NO_CONTENT)
    
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['list','create', 'retrieve', 'update']:
            permission_classes = [AllowAny,] # IsAuthenticated]
        elif self.action == 'destroy':
            permission_classes = [AllowAny,] #  IsAuthenticated,] #CustomPermission   
        else:
            permission_classes = [AllowAny,] # [IsAdminUser]
        return [permission() for permission in permission_classes]


class CleintUserViewSet(viewsets.ViewSet):
    serializer = ClientSerializer
    model = ClientProfile
    
    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        
    def list(self, request):
        obj = self.model.objects.all()
        serializer = self.serializer(obj, many=True)
        return Response(serializer.data)
	
	
    def create(self, request):
        serializer = CreateClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
    def retrieve(self, request, id=None):
        try:
            client = self.get_object(id)  # Use id instead of pk for consistency
        except User.DoesNotExist:
            return Response("Client does not exist", status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer(client)  # Pass user instance to serializer
        return Response(serializer.data)
    
    def partial_update(self, request, id=None):
        try:
            user = self.get_object(id)
        except self.model.DoesNotExist:
            return Response("User does not exist", status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer(user, data=request.data, partial=True)  # Set partial=True for partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, id=None):
        try:
            user = self.get_object(id)
        except self.model.DoesNotExist:
            return Response("User does not exist", status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def destroy(self, request, id=None):
        try:
            user = self.get_object(id)
        except self.model.DoesNotExist:
            return Response("User does not exist", status=status.HTTP_404_NOT_FOUND)
        
        user.delete()
        user = self.model.objects.all()
        serializer = self.serializer(user, many=True)
        return Response({
            "message": "Deleted client object with success",
            "data": serializer.data,
        }, status=status.HTTP_204_NO_CONTENT)
    
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['list','create', 'retrieve', 'update']:
            permission_classes = [AllowAny,] # IsAuthenticated]
        elif self.action == 'destroy':
            permission_classes = [AllowAny,] #  IsAuthenticated,] #CustomPermission   
        else:
            permission_classes = [AllowAny,] # [IsAdminUser]
        return [permission() for permission in permission_classes]











# List all the loans
class LoanListView(viewsets.ViewSet):
    def list(self, request):
        queryset = Loan.objects.all()
        serializer_class = LoanListSerializer
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = LoanSerializer(data=request.data)
        serializer_class = serializer
        serializer_class.is_valid(raise_exception=True)
        amount = serializer_class.validated_data.get('amount')
        status = serializer_class.validated_data.get('status')
        
       

        if amount < 1000 and status == 'pending':
            
            loan_instance = serializer_class.save()
            
            status == loan_instance.status
            status = 'active'
            loan_id = loan_instance.loan_id
            print(status)
            transaction_type = 'Disbursement'

            LoanTransaction = {
                        'loan_id': loan_id,
                        'amount': amount,
                        'status': status,
                        'transaction_type': transaction_type,
    
                    }
                    
            transactionSerializer = LoanTransactionSerializer
            transaction = transactionSerializer(data=LoanTransaction)
            if transaction.is_valid():
                    transaction.save()
                    return Response({'message': 'Your loan of successfully disbursed'})
            else:
                return Response ({'message': 'System failed to disburse the loan'}, status=status.HTTP_400_BAD_REQUEST)
                  

        elif amount > 1000 and status =='pending':
             serializer_class.save()    
             return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.data, status=status.HTTP_400_BAD_REQUEST)
        

    def retrieve(self, request, loan_id=None):

        def retrieve(self, request, pk=None):
            queryset = Loan.objects.filter(loan__loan_id=loan_id)
            serializer_class = LoanSerializer
            serializer = serializer_class(queryset)
            return Response(serializer.data)

    def update(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Individual loan details
class LoanDetailView(viewsets.ViewSet):
    def list(self, request):
        queryset = Loan.objects.all()
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = LoanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# Listing all activaate loans
class ActiveLoanListViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Loan.objects.filter(status='active')
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# List all closed loans
class ClosedLoanListViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Loan.objects.filter(status='closed')
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrive(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        queryset = Loan.objects.get(pk=pk)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# List all pending loans
class PendingLoanListViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Loan.objects.filter(status='pending')
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrive(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# List all rejected loans
class RejectedLoanListViewest(viewsets.ViewSet):
    def list(self, request):
        queryset = Loan.objects.filter(status='rejected')
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrive(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# List all approved loans
class ApprovedLoanListView(viewsets.ViewSet):
    def list(self, request):
        queryset = Loan.objects.filter(status='approved')
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrive(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Loan.objects.get(pk=pk)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Credit score list 
class CreditScoreSerializerViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = CreditScore.objects.all()
        serializer_class = CreditScoreSerializer
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def create(self, request):
        serializer_class = CreditScoreSerializer
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, client_id=None):
        queryset = CreditScore.objects.filter(client__id=client_id).first()
        serializer_class = CreditScoreSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = CreditScoreSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = CreditScoreSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanUpdateViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanUpdateSerializer
    def approve_loan(self, request, loan_id=None):
        try:
            loan = Loan.objects.get(loan__loan_id=loan_id)
            loan.status = 'approved'
            loan.save()

            loan_id = loan.loan_id
            amount = loan.amount
            status = 'active'
            transaction_type = 'Disbursement'

            # if amount < 1000:
            #         #automated  disbursement loan transaction
            #         LoanTransaction = {
            #             'loan_id': loan_id,
            #             'amount': amount,
            #             'loan': loan,
            #             'status': status,
            #             'transaction_type': transaction_type,
                       

            #         }
                    
            #         transactionSerializer = LoanTransactionSerializer
            #         transaction = transactionSerializer(data=request.data)
            #         if transaction.is_valid(raise_exception=True):
            #             transaction.save()
            #             return Response({'message': 'Your loan of successfully disbursed'},transaction.data, status=status.HTTP_201_CREATED)
            #             return Response ({'message': 'System failed to disburse the loan'}, status=status.HTTP_404)
                
            return Response({'status': 'Loan approved successfully'})
        except Loan.DoesNotExist:
            return Response({'status': 'Loan not found'}, status=404)

class LoanTransactionSerializerView(viewsets.ViewSet):
    def list(self, request):
        queryset = LoanTransaction.objects.all()
        serializer_class = LoanTransactionSerializer
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def create(self, request):
        serializer_class = LoanTransactionSerializer
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, loan_id=None):
        queryset = LoanTransaction.objects.get(loan_id=loan_id)
        serializer_class = LoanTransactionSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, loan_id=None):
        queryset = LoanTransaction.objects.filter(loan_id=loan_id)
        serializer_class = LoanTransactionSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, loan_id=None):
        queryset = LoanTransaction.objects.filter(loan_id=loan_id)
        serializer_class = LoanTransactionSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DisbursementOfFunds(viewsets.ViewSet):
    def loan_disbursement(self, request, loan_id=None):
        loan = Loan.objects.get(loan_id=loan_id)
        status = loan.status
        amount = loan.amount
        loan_id = loan.loan_id
        
        if status == "approved":
            status = "active"
            transaction_type = 'Disbursement'
            LoanTransaction = {
                    'loan_id': loan_id,
                    'amount': amount,
                    'status': status,
                    'transaction_type': transaction_type,

                }
                
            transactionSerializer = LoanTransactionSerializer
            transaction = transactionSerializer(data=LoanTransaction)
            if transaction.is_valid():
                transaction.save()
                return Response({'message': 'Your loan is successfully disbursed'}, status=status.HTTP_201_CREATED)

        else:
            return Response({'Message': 'Disbursement of funds not failed'}, status=status.HTTP_400_BAD_REQUEST)



# check payment app 
# Create your views here.
class Command(BaseCommand):
    help = 'Check for due loan payments and send notifications'

    def handle(self, *args, **options):
        today = datetime.now().date()
        due_loans = Loan.objects.filter(due_date=today)

        for loan in due_loans:
            client_email = loan.client.email
            monthly_repayment = loan.monthly_repayment 
            message = f"Dear customer, your loan payment of ${monthly_repayment} is due today. Please make the payment as soon as possible."

            send_mail(
                'Loan Payment Due Notification',
                message,
                'client_email', 
                [client_email],
                fail_silently=False,
            )

            