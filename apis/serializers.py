from rest_framework import serializers
 
from accounts.models import User
from tickets.models import Ticket
# from sales_market.models import Customer, Sale
# from product.models import Product, Invoice, Company, Category, Quotation
# from kycs.models import PersonalInfo


# user serializers

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['profile_pic', 'user_type', 'email', 'first_name', 'last_name', 'dob', 'id_type', 'id_number', 'phone', 'location']

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['title', 'description',  'status', 'client_phonenumber' ,'priority','created_by']


# class UploadCSVSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['users_csv']

# # Product Users
               
# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['thumb', 'name', 'description', 'price', 'discount', 'is_pub', 'favourite', 'category', 'img']
        
# class InvoiceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Invoice
#         fields = ['customer', 'company_name', 'product', 'invoice_number','total_amount', 'location']

# class QoatationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Quotation
#         fields = ['product', 'customer', 'quantity', 'unity_price', 'expiration_date']
        
# class CompanySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Company
#         fields = ['business_name', 'business_email', 'business_phone_number']
        
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['cover', 'title']


# class CustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = ['first_name', 'last_name', 'email', 'phonenumber', 'address']
        
# class SaleSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Sale
#         fields = ['product', 'customer', 'quantity', 'unity_price', 'total_amount']

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['cover', 'title']

# class TodoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Todo
#         fields = ['title', 'description']       

# class PersonalInfoSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = PersonalInfo
    #     fields = ['user', 'first_name', 'middle_name', 'last_name', 'husband_name', 'father_name', 'mother_name', 
    #               'witness_name', 'witness_relation', 'dob', 'age', 'gender', 'marital_status', 'religion', 
    #               'nationality', 'id_type', 'idNo', 'email', 'medication', 'medication_type', 'occupation', 
    #               'home_address', 'childrens', 'boys', 'girls', 'banks', 'family_type', 'date_joined']