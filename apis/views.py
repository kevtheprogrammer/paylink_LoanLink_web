from django.http import HttpResponse
from django.shortcuts import render, redirect
# from inventory.models import Category
# from kycs.models import PersonalInfo
# from todos.models import Todo
from .serializers import *
from rest_framework import viewsets
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
# from sales_market.models import Customer, Sale
# from product.models import Company, Invoice, Product, Quotation
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

from accounts.models import User
from tickets.models import Ticket


# User Api Viewsets
  
class UserViewSet(viewsets.ViewSet):

    
	def list(self, request):
		user = User.objects.all()
		serializer = UserProfileSerializer(user, many=True)
		return Response(serializer.data)
	
    
	def create(self, request):
		serializer = UserProfileSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
	
    
	def retrieve(self, request, pk=None):
		user = User.objects.get(pk=pk)
		serializer = UserProfileSerializer(user)
		return Response(serializer.data)

	def update(self, request, pk=None):
		user = User.objects.get(pk=pk)
		serializer = UserProfileSerializer(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
	def destroy(self, request, pk=None):
		user = User.objects.get(pk=pk)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)




# @authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated]) 
class TicketViewSet(viewsets.ViewSet):
    
    @authentication_classes([JWTAuthentication])
    @permission_classes([IsAuthenticated])
    def list(self, request):
        ticket = Ticket.objects.all()
        serializer = TicketSerializer(ticket, many=True)
        return Response(serializer.data)
    
    @authentication_classes([JWTAuthentication])
    @permission_classes([IsAuthenticated])
    def create(self, request):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            ticket_data = serializer.validated_data
            ticket = serializer.save(**ticket_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @authentication_classes([JWTAuthentication])
    @permission_classes([IsAuthenticated])
    def retrieve(self, request, pk=None):
        ticket = Ticket.objects.get(pk=pk)
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)
    @authentication_classes([JWTAuthentication])
    @permission_classes([IsAuthenticated])
    def update(self, request, pk=None):
        ticket = Ticket.objects.get(pk=pk)
        serializer = TicketSerializer(ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return  Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    @authentication_classes([JWTAuthentication])
    @permission_classes([IsAuthenticated])
    def destroy(self, request, pk=None):
        ticket = Ticket.objects.get(pk=pk)
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
  





# # product api viewsets
# class ProductViewSet(viewsets.ViewSet):
	
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def list(self, request):
#         product = Product.objects.all()
#         serializer = ProductSerializer(product, many=True)
#         return Response(serializer.data)
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def create(self, request):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, stutus=status.HTTP_201_CREATED)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def retrieve(self, request, pk=None):
#         product = Product.objects.get(pk=pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)

#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def update(self, request, pk=None):
#          product = Product.objects.get(pk=pk)
#          serializer = ProductSerializer(product, data=request.data)
#          if serializer.is_valid():
#              serializer.save()
#              return Response(serializer.data)
#          return  Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def destroy(self, request, pk=None):
#         product = Product.objects.get(pk=pk)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# # @authentication_classes([TokenAuthentication, SessionAuthentication])
# # @permission_classes([IsAuthenticated]) 
# class InvoiceViewSet(viewsets.ViewSet):
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def list(self, request):
#         invoice = Invoice.objects.all()
#         serializer = InvoiceSerializer(invoice, many=True)
#         return Response(serializer.data)
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def create(self, request):
#         serializer = InvoiceSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, stutus=status.HTTP_201_CREATED)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def retrieve(self, request, pk=None):
#         invoice = Invoice.objects.get(pk=pk)
#         serializer = InvoiceSerializer(invoice)
#         return Response(serializer.data)
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def update(self, request, pk=None):
#         invoice = Invoice.objects.get(pk=pk)
#         serializer = InvoiceSerializer(invoice, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return  Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def destroy(self, request, pk=None):
#         invoice = Invoice.objects.get(pk=pk)
#         invoice.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# # @authentication_classes([TokenAuthentication, SessionAuthentication])

# @permission_classes([IsAuthenticated]) 

# class CompanyViewSet(viewsets.ViewSet):
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def list(self, request):
#         company = Company.objects.all()
#         serializer = CompanySerializer(company, many=True)
#         return Response(serializer.data)
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def create(self, request):
#         serializer = CompanySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, stutus=status.HTTP_201_CREATED)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def retrieve(self, request, pk=None):
#         company = Company.objects.get(pk=pk)
#         serializer = CompanySerializer(company)
#         return Response(serializer.data)
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def update(self, request, pk=None):
#         company = Company.objects.get(pk=pk)
#         serializer = CompanySerializer(company, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return  Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def destroy(self, request, pk=None):
#         company = Company.objects.get(pk=pk)
#         company.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# # @authentication_classes([TokenAuthentication, SessionAuthentication])
# # @permission_classes([IsAuthenticated]) 
# class CategoryViewSet(viewsets.ViewSet):
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def list(self, request):
#         category = Category.objects.all()
#         serializer = CompanySerializer(category, many=True)
#         return Response(serializer.data)
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def create(self, request):
#         serializer = CompanySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, stutus=status.HTTP_201_CREATED)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def retrieve(self, request, pk=None):
#         category = Category.objects.get(pk=pk)
#         serializer = CompanySerializer(category)
#         return Response(serializer.data)
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def update(self, request, pk=None):
#         category = Category.objects.get(pk=pk)
#         serializer = CompanySerializer(category, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return  Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def destroy(self, request, pk=None):
#         category = Category.objects.get(pk=pk)
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
    
 

# # sales and markets
# # @authentication_classes([TokenAuthentication, SessionAuthentication])
# @permission_classes([IsAuthenticated]) 
# class CustomerViewSet(viewsets.ViewSet):
    
#         def list(self, request):
#             customers = Customer.objects.all()
#             serializer = CustomerSerializer(customers, many=True)
#             return Response(serializer.data)
        
#         def create(self, request):
#             serializer = CustomerSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         def retrieve(self, request, pk=None):
#             customer = Customer.objects.get(pk=pk)
#             serializer = CustomerSerializer(customer)
#             return Response(serializer.data)
        
#         def update(self, request, pk=None):
#             customer = Customer.objects.get(pk=pk)
#             serializer = CustomerSerializer(customer, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         def destroy(self, request, pk=None):
#             customer = Customer.objects.get(pk=pk)
#             customer.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
# # @authentication_classes([TokenAuthentication, SessionAuthentication])
# @permission_classes([IsAuthenticated])         
# class SaleViewSet(viewsets.ViewSet):
    
#         def list(self, request):
#             sale = Sale.objects.all()
#             serializer = SaleSerializers(sale, many=True)
#             return Response(serializer.data)
        
#         def create(self, request):
#             serializer = SaleSerializers(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         def retrieve(self, request, pk=None):
#             sale = Sale.objects.get(pk=pk)
#             serializer = SaleSerializers(sale)
#             return Response(serializer.data)
        
#         def update(self, request, pk=None):
#             sale = Sale.objects.get(pk=pk)
#             serializer = SaleSerializers(sale, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         def destroy(self, request, pk=None):
#             sale = Sale.objects.get(pk=pk)
#             sale.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)

# #ticket

  
# class CategoryViewSet(viewsets.ViewSet):
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def list(self, request):
#         category = Category.objects.all()
#         serializer = CategorySerializer(category, many=True)
#         return Response(serializer.data)
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def create(self, request):
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def retrieve(self, request, pk=None):
#         category = Category.objects.get(pk=pk)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def update(self, request, pk=None):
#         category = Category.objects.get(pk=pk)
#         serializer = CategorySerializer(category, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def destroy(self, request, pk=None):
#         category = Category.objects.get(pk=pk)
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

# # Todo APIs
# # @authentication_classes([TokenAuthentication, SessionAuthentication])
# # @permission_classes([IsAuthenticated]) 
# class TodoViewSet(viewsets.ViewSet):

#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def list(self, request):
#         todo = Todo.objects.all()
#         serializer = TodoSerializer(todo, many=True)
#         return Response(serializer.data)
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def create(self, request):
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def retrieve(self, request, pk=None):
#         todo = Todo.objects.get(pk=pk)
#         serializer = TodoSerializer(todo)
#         return Response(serializer.data)
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def partial_update(self, request, pk=None):
#         todo = Todo.objects.get(pk=pk)
#         serializer = TodoSerializer(todo, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def update(self, request, pk=None):
#         todo = Todo.objects.get(pk=pk)
#         serializer = TodoSerializer(todo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def destroy(self, request, pk=None):
#         todo = Todo.objects.get(pk=pk)
#         todo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# # @authentication_classes([TokenAuthentication, SessionAuthentication])
# class PersonalInfoViewSet(viewsets.ViewSet):
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated]) 
#     def list(self, request):
#           person = PersonalInfo.objects.all()
#           serializer = PersonalInfoSerializer(person, many=True)
#           return Response(serializer.data)
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def create(self, request):
#           serializer = PersonalInfoSerializer(data=request.data)
#           if serializer.is_valid():
#               serializer.save()
#               return Response(serializer.data, status=status.HTTP_201_CREATED)
#           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated]) 
#     def retrieve(self, request, pk=None):
#         person = PersonalInfo.objects.get(pk=pk)
#         serializer = PersonalInfoSerializer(person)
#         return Response(serializer.data)
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def partial_update(self, request, pk=None):
#           person = PersonalInfo.objects.get(pk=pk)
#           serializer = PersonalInfoSerializer(person, data=request.data, partial=True)
#           if serializer.is_valid():
#               serializer.save()
#               return Response(serializer.data)
#           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def update(self, request, pk=None):
#           person = PersonalInfo.objects.get(pk=pk)
#           serializer = PersonalInfoSerializer(person, data=request.data)
#           if serializer.is_valid():
#               serializer.save()
#               return Response(serializer.data)
#           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def destroy(self, request, pk=None):
#           person = PersonalInfo.objects.get(pk=pk)
#           person.delete()
#           return Response(status=status.HTTP_204_NO_CONTENT)
    

# class QoutationViewset(viewsets.ViewSet):

#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated]) 
#     def list(self, request):
#         qoutation = Quotation.objects.all()
#         serializer = QoatationSerializer(qoutation, many=True)
#         return Response(serializer.data)
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated]) 
#     def create(self, request):
#         serializer = QoatationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def retrieve(self, request, pk=None):
#         qoutation = Quotation.objects.get(pk=pk)
#         serializer = QoatationSerializer(qoutation)
#         return Response(serializer.data)
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def partial_update(self, request, pk=None):
#         qoutation = Quotation.objects.get(pk=pk)
#         serializer = QoatationSerializer(qoutation, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def update(self, request, pk=None):
#         qoutation = Quotation.objects.get(pk=pk)
#         serializer = QoatationSerializer(qoutation, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     @authentication_classes([JWTAuthentication])
#     @permission_classes([IsAuthenticated])
#     def destroy(self, request, pk=None):
#         qoutation = Quotation.objects.get(pk=pk)
#         qoutation.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
     