from datetime import  timedelta, timezone
from django.db import models
from django.db import models
import uuid
from account.models import User
from account.models import ClientProfile
from django.core.exceptions import ValidationError

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
        ('collatral loans', 'Collatral Loans'),
        ('salary advance', 'Salary Advance'),
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
        return f'{self.id} {self.amount} {self.customer}'

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


 
class LoanProduct(models.Model):
    INTEREST_RATE_METHOD = (
        ('Flate Rate', 'Flate Rate'),
        ('Reducing Balance', 'Reducing Balance'),
        ('Interest Only', 'Interest Only'),
    )
    DURATION_PERIOD = (
        ('weeks', 'Weeks'),
        ('months', 'Months'),
        ('years', 'Years'),
    )
    loan = models.ForeignKey(Loan, related_name='loans', on_delete=models.CASCADE, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    interest_rate_method = models.CharField(max_length=20, choices=INTEREST_RATE_METHOD, default='Flate Rate')
    duration_period = models.CharField(max_length=20, choices=DURATION_PERIOD, null=True)
    duration_length = models.IntegerField(blank=True,null=True)
    minimum_amount = models.DecimalField(max_digits=10, decimal_places=2)
    maximum_amount = models.DecimalField(max_digits=10, decimal_places=2)


    # def getIntrest(self):
    #     calculated_interest = 0
    #     if self.interest_rate_method == 'Flate Rate':
    #         pass
    #     elif self.interest_rate_method == 'Reducing Balance':
    #         pass
    #     elif self.interest_rate_method == 'Interest Only':
    #         pass
    #     return self.interest_rate_method
    

    def __str__(self):
        return f'{self.product_name} {self.interest_rate_method}'

    def clean(self):
        if self.minimum_amount > self.maximum_amount:
            raise ValidationError("Minimum amount cannot be greater than maximum amount.")
        
    
    def validateLoanAmount(self, amount):
        if amount < self.minimum_amount or amount > self.maximum_amount:
           raise ValidationError(f'Loan amount must be between {self.minimum_amount} and {self.maximum_amount}.')
        

        class Meta:
            abstract = False

    def get_duration_in_years(duration_period, duration_length):
        if duration_period == 'weeks':
            return duration_length / 52
        elif duration_period == 'months':
            return duration_length / 12
        return duration_length

    def calculateTotalPayment(self, principle, duration_length, interest_rate_method, client_id):
        if interest_rate_method == 'Flat Rate':
            self.validateLoanAmount(principle)

            total_interest = principle * (self.interest_rate / 100) * duration_length
            total_repayment = principle + total_interest
            
            return total_repayment

        elif interest_rate_method == 'Reducing Balance':
            self.validateLoanAmount(principle)
            total_repayment = 0
            remaining_principle = principle
            annual_rate = self.interest_rate / 100

            for _ in range(duration_length):
                interest_for_year = remaining_principle * annual_rate
                remaining_principle -= (principle / duration_length)
                total_repayment += (principle / duration_length) + interest_for_year

            return total_repayment

        elif interest_rate_method == 'Interest Only':
            self.validateLoanAmount(principle)
            total_repayment = principle * (self.interest_rate / 100) * duration_length
            return total_repayment + principle

        else:
            raise ValueError("Invalid interest rate method provided.")




    # duration_years = get_duration_in_years(self.duration_period, self.duration_length)

    # Example calculation logic (this needs to be specific to the subclass's requirement)
        # total_interest = principle * (self.interest_rate / 100) * duration_years
        # total_repayment = principle + total_interest
        # return total_repayment



#Flat Interest
# class FlatRateProducts(LoanProduct):
#     def calculateTotalPayment(self,principle):
#         self.validateLoanAmount(principle)

#         total_interest = principle * (self.interest_rate / 100) * self.duration_period
#         total_repayment = principle + total_interest
#         return total_repayment
    

# class ReducingBalance(LoanProduct):
#     def calculateTotalPayment(self, principle):
#         self.validateLoanAmount(principle)
#         total_repayment = 0
#         remaining_principle = principle
#         annual_rate = self.interest_rate

#         for year in range(self.duration_length):
#             interest_for_year = remaining_principle * annual_rate
#             remaining_principle -= (principle / self.duration_period)
#             total_repayment += (principle / self.duration_period) + interest_for_year

#         return total_repayment
    
# class InterestOnly(LoanProduct):
#     def calculateTotalPayment(self, principle):
#         self.validateLoanAmount(principle)
    
#         total_repayment = principle * (self.interest_rate / 100) * self.duration_length
#         return total_repayment + principle