from django.db import models
from account.models import ClientProfile, User
from loan.models import Loan


class LoanTransaction(models.Model):
    STATUS_CHOICES = (
        ('pending', 'pending'),
        ('success', 'success'),
        ('declined', 'declined'),
    )

    TRANSCTION_TYPE = (
        ('Disbursement', 'Disbursement,'),
        ('Loan Repayment', 'Loan Repayment'),
        ('Penalty', 'Penalty'),
        ('bad debt', 'Bad Debt')

    )

    loan_obj = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='loan_obj')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    is_payment_made = models.BooleanField(default=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='active')
    transaction_type = models.CharField(max_length=255, choices=TRANSCTION_TYPE)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    approved_at = models.DateTimeField(blank=True, null=True)
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.amount} {self.transaction_type} of {self.loan_obj}'





class BadDebt(models.Model):
    loan_transaction_id = models.ForeignKey(LoanTransaction, verbose_name=("Loan Transactions"), on_delete=models.CASCADE)
    loan_amount = models.FloatField()
    debt_amount = models.FloatField()
    settlement_date = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)

    


