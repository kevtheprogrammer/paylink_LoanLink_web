from django.contrib import admin
from .models import Loan, LoanTransaction, CreditScore

admin.site.register(Loan)
admin.site.register(LoanTransaction)
admin.site.register(CreditScore)
