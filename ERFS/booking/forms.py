from django import forms
from .models import Asset

class UploadForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ('asset_Title', 'asset_Type', 'asset_Price', 'asset_purpose', 'asset_Location', 'asset_Image')
