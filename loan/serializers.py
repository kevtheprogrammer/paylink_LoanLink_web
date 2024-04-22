from rest_framework import serializers
from .models import Loan, CreditScore, LoanTransaction
from userProfile.models import ClientProfile,AgentProfile



class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProfile
        fields = '__all__'


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentProfile
        fields = '__all__'


class LoanSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Loan
        fields = '__all__'


class LoanListSerializer(serializers.ModelSerializer):
     client = ClientSerializer()

     class Meta:
        model = Loan
        fields = '__all__'



class CreditScoreSerializer(serializers. ModelSerializer):
    class Meta:
        model = CreditScore
        fields = ['id','credit_score','crb','number_of_loan']
        read_only = ['id', ]    


class CreditScoreListSerializer(serializers. ModelSerializer):
    client = ClientSerializer()
    class Meta:
        model = CreditScore
        fields = ['id','credit_score','crb','number_of_loan']
        read_only = ['id', ] 

class LoanUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ['loan_id', 'status']
        read_only = ['loan_id']


class LoanTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanTransaction
        fields = ['id','loan_id', 'amount', 'is_payment_made', 'status', 'transaction_type', 'approved_by', 'approved_at', 'date']
        read_only = ['id']