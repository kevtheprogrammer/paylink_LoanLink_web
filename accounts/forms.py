from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import forms
from .models import User


class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("email",)


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("email",)
        
 
class UploadUsersCSVForm(forms.Form):
    csv_file = forms.FileField()
   
 
        
# class UploadUserCSV(forms.Form):
#     class Meta:
#         model = User
#         fields = ['users_csv']
        