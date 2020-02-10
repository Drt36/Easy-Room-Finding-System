from django import forms
from  .models import UserProfile
# Form To create User Profile using Meta class
class profileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields=('picture','bio')