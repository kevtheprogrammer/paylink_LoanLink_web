from django import forms
from loan .models import LoanProduct

class BulkClientUploadForm(forms.Form):
    file = forms.FileField()


class LoanProductForm(forms.Form):
     class Meta:
        model = LoanProduct
        fields = ['name', 'description', 'interest_rate']
    