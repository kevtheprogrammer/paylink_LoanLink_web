from account.models import ClientProfile
from loan.models import Loan
from account.models import ClientProfile
from account.models import *
 
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets, status
from loan.models import *
from payment.models import *
from datetime import datetime
from django.core.mail import send_mail
from rest_framework.response import Response
from django.core.management.base import BaseCommand
from django.http import Http404, HttpResponse
from rest_framework.permissions import IsAuthenticated,AllowAny

from .serializers import *


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

# Credit score list 
class CreditScoreSerializerViewset(viewsets.ViewSet):
    serializer = CreditScoreSerializer
    model = CreditScore
    
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
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
    def retrieve(self, request, client_employee_number=None):
        try:
            # Retrieve the CreditScore instance based on the client employee number
            credit_score = CreditScore.objects.get(client__empolyee_number=client_employee_number)
            
            # Serialize the CreditScore instance
            serializer = CreditScoreSerializer(credit_score)
            return Response(serializer.data)
        
        except CreditScore.DoesNotExist:
            # Handle the case where no CreditScore with the given employee number is found
            return Response({'detail': 'CreditScore not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def retrieve_base(self, request, id=None):
        try:
            obj = self.get_object(id)  # Use id instead of pk for consistency
        except self.model.DoesNotExist:
            return Response("Credit Score does not exist", status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer(obj)  # Pass user instance to serializer
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
    serializer = LoanSerializer
    model = Loan
    
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
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
    def retrieve(self, request, id=None):
        try:
            obj = self.get_object(id)  # Use id instead of pk for consistency
        except self.model.DoesNotExist:
            return Response("Loan does not exist", status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer(obj)  # Pass user instance to serializer
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

class LoanTransactionSerializerView(viewsets.ViewSet):
    serializer = CreateLoanTransactionSerializer
    model = LoanTransaction
    
    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        
    def list(self, request):
        obj = self.model.objects.all()
        serializer = ListLoanTransactionSerializer(obj, many=True)
        return Response(serializer.data)
	
    def create(self, request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
    def retrieve(self, request, id=None):
        try:
            obj = self.get_object(id)  # Use id instead of pk for consistency
        except User.DoesNotExist:
            return Response("Client does not exist", status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer(obj)  # Pass user instance to serializer
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

# List all pending loans
class FilterLoansByStatus(viewsets.ViewSet):
    serializer = FilterLoanSerializer
    model = Loan

    def list(self, request, loan_status):
        # Filter loans by status
        if loan_status in [choice[0] for choice in Loan.STATUS_CHOICES]:
            filtered_loans = self.model.objects.filter(status=loan_status)
            serializer = self.serializer(filtered_loans, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "Invalid status provided"},status=status.HTTP_400_BAD_REQUEST)
       
class LoacActionViewSet(viewsets.ViewSet):
    serializer = LoanSerializer
    model = Loan

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def create_txn(self, loan_id):
        loan = self.get_object(loan_id)
        loan_transaction = LoanTransaction(
            loan_obj=loan,
            amount=loan.amount,  # Provide the amount
            is_payment_made=True,  # Set the payment status
            status='pending',  # Set the status
            transaction_type='Disbursement',  # Set the transaction type
            client=loan.customer,
            # approved_at=datetime.datetime.now(),  # Set the approval date/time
        )
        txn = loan_transaction.save()
        return txn

    def approve_loan(self, request, id=None):
        try:
            loan = self.get_object(id)
            loan.status = 'approved'
            # loan.approved_at = datetime.datetime.now()
            loan.save()
            generate_txn = self.create_txn(loan.id)
            loan_serializer = self.serializer(generate_txn)
            txn_serializer = ListLoanTransactionSerializer(generate_txn)
            
            return Response({
                "message": "transaction approved",
                "data": loan_serializer.data,
                "transaction": txn_serializer.data,
            }, status=status.HTTP_204_NO_CONTENT)
        except self.model.DoesNotExist:
            return Response("Loan does not exist", status=status.HTTP_404_NOT_FOUND)
        

    def activate_loan(self, id):
        pass

    def disburse_loan(self, id):
        pass





  
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

            