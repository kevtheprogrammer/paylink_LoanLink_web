from datetime import  timedelta, timezone
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

    customer = models.ForeignKey(ClientProfile, related_name='customer', on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    period = models.IntegerField(null=True, help_text='in months', default=1)
    purpose = models.CharField(max_length=100)    
    total_interest = models.FloatField(null=True)
    payable_amount = models.FloatField(null=True)
    approved_date = models.DateField(blank=True, null=True)
    method_of_payment = models.CharField(max_length=200,choices=PAYEE, null=True)
    loan_type = models.CharField(max_length=200,choices=LOAN_TYPE, null=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, null=True, default='pending')
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    approved_at_branch = models.CharField(max_length=900,blank=True, null=True)

    def __str__(self):
        return f'{self.loan_id}'

    def get_due_date(self):
        if self.approved_date and self.period:
            due_date = self.approved_date + timedelta(days=30 * self.period)
            return due_date
        return None

    def get_remaining_days(self):
        due_date = self.get_due_date()
        if due_date:
            remaining_days = (due_date - timezone.now().date()).days
            return remaining_days if remaining_days > 0 else 0
        return None

    def get_monthly_interest(self):
        return self.total_interest / self.period


    def get_monthly_payable(self):
        return self.payable_amount / self.period

class CreditScore(models.Model):
    client = models.ForeignKey(ClientProfile, related_name='client',on_delete=models.CASCADE)
    credit_score = models.BigIntegerField(blank=True, null=True)
    crb = models.BigIntegerField(blank=True, null=True)
    number_of_loan = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return f'credist score no. {self.id}'


# class PaymentPosting(models.Model):
#     TRANSCTION_TYPE = (
#         ('Disbursement', 'Disbursement,'),
#         ('Loan Repayment', 'Loan Repayment'),
#         ('Penalty', 'Penalty'),
#         ('bad debt', 'Bad debt'),
#     )
#     TRANSCTION_STATUS = (
#         ('success', 'success,'),
#         ('pending', 'pending'),
#         ('declined', 'declined'),
#     )
#     client_user = models.ForeignKey(ClientProfile, related_name='client_user', on_delete=models.CASCADE)
#     loan = models.ForeignKey(Loan, related_name='loans', on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     date = models.DateField(auto_now_add=True)
#     transaction_type = models.CharField(max_length=255, choices=TRANSCTION_TYPE)
#     status = models.CharField(max_length=255, choices=TRANSCTION_STATUS)
#     is_payment_made = models.BooleanField(default=True)
#     timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
#     l_upfates = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

#     def __str__(self):
#         return f'{self.loan_id}'

