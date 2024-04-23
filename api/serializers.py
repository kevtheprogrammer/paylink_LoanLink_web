from rest_framework import serializers
from account.models import ClientProfile, AgentProfile
from account.models import User
from loan.models import *
from payment.models import *

class BasicUserAccountSerializer(serializers.ModelSerializer):
    queryset = User.objects.all()
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name','phone_number']
        read_only = ['id']

class CreateBasicUserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']
        read_only = ['id']
        extra_kwargs = {'password': {'write_only': True}}

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [  "id", "last_login", "is_superuser", "user_type", "profile_pic", "email",  "first_name", "last_name", "phone_number", "dob", "id_type", "id_number", "location", "id_front", "id_back", "gender", "city", "address" , "is_staff" , "is_supervisor" , "is_manager" , "date_joined" , "is_active" , "is_verified" , ]
        read_only = ['id','last_login',]
        
class CreateClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProfile
        fields =["id",'empolyee_number', 'bank','bank_acc', 'user']
        read_only = ['id',]

class CreditScoreSerializer(serializers. ModelSerializer):
    class Meta:
        model = CreditScore
        fields = ['id', 'number_of_loan', 'credit_score', 'crb','client', ]
        read_only = ['id', ] 

class ClientSerializer(serializers.ModelSerializer):
    user = BasicUserAccountSerializer(read_only=True)
    credit_score = CreditScoreSerializer(read_only=True)

    class Meta:
        model = ClientProfile
        fields = ["id", 'empolyee_number',  'bank', 'bank_acc', 'user', 'credit_score']
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