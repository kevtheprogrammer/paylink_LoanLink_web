from django import forms

class BulkClientUploadForm(forms.Form):
    file = forms.FileField()
