from django import forms
from django.contrib.auth.models import User
# Using Meta To create Registration Form
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password')

       

       
