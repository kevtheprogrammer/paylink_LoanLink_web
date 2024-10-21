from django import forms

class BulkClientUploadForm(forms.Form):
    file = forms.FileField()


class LoanProductForm(forms.Form):
    file = forms.FileField()
    