from datetime import datetime
from rest_framework import serializers
from account.models import ClientProfile, AgentProfile
from account.models import User, Notification
from loan.models import *
from payment.models import *
from django.contrib.auth.hashers import make_password
from django.conf import settings
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


class BasicUserAccountSerializer(serializers.ModelSerializer):
    queryset = User.objects.all()
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name','phone_number']
        read_only = ['id']

class CreateBasicUserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password','phone_number']
        read_only = ['id']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Hash the password before saving
        hashed_password = make_password(validated_data['password'])
        validated_data['password'] = hashed_password
        return super().create(validated_data)

class BasicCreditScoreSerializer(serializers. ModelSerializer):
    time_fetched = serializers.DateTimeField(source='credit_score.time_fetched')
    class Meta:
        model = CreditScore
        fields = ['id', 'number_of_loan', 'credit_score', 'crb','client','time_fetched' ]
        read_only = ['id', ] 


class BasicClientSerializer(serializers.ModelSerializer):
    # credit_score = BasicCreditScoreSerializer(source='client__credit_score')  # Access time_fetched through related CreditScore model
    credit_score = serializers.SerializerMethodField()
    
    class Meta:
        model = ClientProfile
        fields = ["id", 'empolyee_number', 'balance',  'bank', 'bank_acc', 'pin','credit_score']
        read_only_fields = ['id', 'credit_score'] 
    def get_credit_score(self, obj):
        # Filter the associated credit score
        credit_score_instance = CreditScore.objects.filter(client=obj).first()
        
        if credit_score_instance:
            # Serialize the credit score instance
            serializer = CreditScoreSerializer(credit_score_instance)
            return serializer.data
        else:
            return None

 
class UserSerializer(serializers.ModelSerializer):
    client_profile = BasicClientSerializer()
    time_fetched = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = [
            "id", "last_login", "is_superuser", "user_type", "profile_pic",
            "email", "first_name", "last_name", "phone_number", "dob", "id_type", "id_number",
            "location", "id_front",  "id_back", "gender",
            "city", "address", "is_staff", "is_supervisor", "is_manager", "date_joined",
            "is_active", "is_verified",   'time_fetched','client_profile'
        ]
        read_only_fields = ['id', 'last_login', 'profile_pic_url', 'id_front_url', 'id_back_url']
    
    def get_time_fetched(self, obj):
        return datetime.now()  
 


class CreateClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProfile
        fields =["id",'empolyee_number', 'bank','bank_acc', 'user','pin']
        read_only = ['id',]
        extra_kwargs = {'pin': {'write_only': True}}

class CreditScoreSerializer(serializers. ModelSerializer):
    class Meta:
        model = CreditScore
        fields = ['id', 'number_of_loan', 'credit_score', 'crb','client', ]
        read_only = ['id', ] 

class UserUpdateForClientSerializer(serializers. ModelSerializer):
    profile_pic = serializers.ImageField(required=False, allow_null=True)
    nrc_front = serializers.ImageField(required=False, allow_null=True)
    nrc_back = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = User
        fields = [
            "nrc", "nrc_back", "nrc_front","profile_pic","dob"
        ]
        read_only = ['id',   ]
    
    def update(self, instance, validated_data):
        # Update the user instance with the validated data
        instance.nrc = validated_data.get(
            'nrc', instance.nrc)

        # Update the avatar field only if it's provided
        profile_pic = validated_data.get('profile_pic', None)
        nrc_back = validated_data.get('nrc_back', None)
        nrc_front = validated_data.get('nrc_front', None)

        if profile_pic:
            instance.profile_pic = profile_pic

        if nrc_front:
            instance.nrc_front = nrc_front

        if nrc_back:
            instance.nrc_back = nrc_back

        # Save the changes to the user instance
        instance.save()

        return instance

class ClientUpdateForClientSerializer(serializers. ModelSerializer):
    class Meta:
        model = ClientProfile
        fields = [
            'id', 'empolyee_number', 'balance',  'bank', 'bank_acc', 'pin'    
        ]
        read_only_fields = ['id', ]  
        # Ensure credit_score is read-only
        # extra_kwargs = {'pin': {'write_only': True}}
    
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user_serializer = self.fields['user']
            user_instance = instance.user
            user_serializer.update(user_instance, user_data)
        return super().update(instance, validated_data)

class ClientSerializer(serializers.ModelSerializer):
    user = BasicUserAccountSerializer(read_only=True)
    credit_score = CreditScoreSerializer(read_only=True)

    class Meta:
        model = ClientProfile
        fields = ["id", 'empolyee_number', 'balance',  'bank', 'bank_acc', 'user', 'credit_score']
        read_only_fields = ['id', 'credit_score']  # Ensure credit_score is read-only

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user_representation = {
            'email': instance.user.email,
            'first_name': instance.user.first_name,
            'last_name': instance.user.last_name,
            'phone_number': instance.user.phone_number
        }
        representation['user'] = user_representation
        return representation

class LoanSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Loan
        fields =  [
            'id', 'customer', 'amount', 'period',  'purpose',    
            'total_interest',   'payable_amount', 'approved_date', 
            'method_of_payment', 'loan_type', 'status',    
            'approved_by', 'approved_at_branch', 
        ]
        read_only = [ 'id', ]

class ListLoanSerializer(serializers.ModelSerializer):
    customer = ClientSerializer(read_only=True)
    class Meta:
        model = Loan
        fields =  [
            'id', 'amount', 'period',  'purpose',    
            'total_interest',   'payable_amount', 'approved_date', 
            'method_of_payment', 'loan_type', 'status',    
            'approved_by', 'approved_at_branch', 'customer', 
        ]
        read_only = [ 'id', ]

class CreateLoanTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanTransaction
        fields = [ "id","date", "loan_obj","amount","is_payment_made","status","transaction_type","approved_by","approved_at","client"  ]
        read_only = [ "id","date"]

class ListLoanTransactionSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    class Meta:
        model = LoanTransaction
        fields = [ "id","date", "loan_obj","amount","is_payment_made","status","transaction_type","approved_by","approved_at","client"  ]
        read_only = [ "id","date"]

class FilterLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentProfile
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


# class LoanListSerializer(serializers.ModelSerializer):
#      client = ClientSerializer()

#      class Meta:
#         model = Loan
#         fields = '__all__'

# class CreditScoreSerializer(serializers. ModelSerializer):
#     class Meta:
#         model = CreditScore
#         fields = ['id','credit_score','crb','number_of_loan']
#         read_only = ['id', ]    

# class CreditScoreListSerializer(serializers. ModelSerializer):
#     client = ClientSerializer()
#     class Meta:
#         model = CreditScore
#         fields = ['id','credit_score','crb','number_of_loan']
#         read_only = ['id', ] 

class LoanUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ['loan_id', 'status']
        read_only = ['loan_id']

# class LoanTransactionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LoanTransaction
#         fields = ['id','loan_id', 'amount', 'is_payment_made', 'status', 'transaction_type', 'approved_by', 'approved_at', 'date']
#         read_only = ['id']