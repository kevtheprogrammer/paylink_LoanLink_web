from django.db import models
from django.db import models
import uuid
from account.models import User
from account.models import ClientProfile

class Loan(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('active', 'Active'),
        ('closed', 'Closed'), 
    )

    PAYEE = (

        ('mobile', 'mobile'),
        ('bank account', 'Bank Account'),
        ('credit card', 'Credit Card'),
        ('debit card', 'Debit Card'),
        ('loan', 'Loan'),
    )

    LOAN_TYPE = (

        ('civil servant loans', 'Civil Servant Loans'),
        ('famers loans', 'Famers Loans'),
        ('micro business loans', 'Micro Business Loans'),
    )


    loan_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(ClientProfile, related_name='clients', on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    period = models.IntegerField(null=True)
    purpose = models.CharField(max_length=100)
    balance = models.FloatField(null=True)
    monthly_interest = models.FloatField(null=True)
    total_interest = models.FloatField(null=True)
    monthly_repayment = models.FloatField(null=True)
    total_repayment = models.FloatField(null=True)
    start_date = models.DateField(auto_now_add=True, null=True)
    due_date = models.DateField(auto_now=True, null=True)
    end_date = models.DateField(auto_now_add=True, null=True)
    method_of_payment = models.CharField(max_length=200,choices=PAYEE, null=True)
    loan_type = models.CharField(max_length=200,choices=LOAN_TYPE, null=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, null=True, default='pending')
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    approved_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.loan_id}'



class LoanTransaction(models.Model):
    STATUS_CHOICES = (
        ('active', 'Acctive'),
        ('closed', 'Closed'),
        ('bad debt', 'Bad debt'),
    )

    TRANSCTION_TYPE = (
        ('Disbursement', 'Disbursement,'),
        ('Loan Repayment', 'Loan Repayment'),
        ('Penalty', 'Penalty'),
        ('bad debt', 'Bad Debt')

    )

    loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='loan')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    is_payment_made = models.BooleanField(default=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='active')
    transaction_type = models.CharField(max_length=255, choices=TRANSCTION_TYPE)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    approved_at = models.DateTimeField(blank=True, null=True)
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.loan_id}'



class CreditScore(models.Model):
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    credit_score = models.BigIntegerField(blank=True, null=True)
    crb = models.BigIntegerField(blank=True, null=True)
    number_of_loan = models.BigIntegerField(blank=True, null=True)



class PaymentPosting(models.Model):
    TRANSCTION_TYPE = (
        ('Disbursement', 'Disbursement,'),
        ('Loan Repayment', 'Loan Repayment'),
        ('Penalty', 'Penalty'),
        ('bad debt', 'Bad debt'),
    )

    client = models.ForeignKey(ClientProfile, related_name='client', on_delete=models.CASCADE)
    loan_id = models.ForeignKey(ClientProfile, related_name='loans', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    is_payment_made = models.BooleanField(default=True)
    transaction_type = models.CharField(max_length=255, choices=TRANSCTION_TYPE)

    def __str__(self):
        return f'{self.loan_id}'

