from django import forms
from django.utils.http import urlencode

class ConvertURLForm(forms.Form):
    to_convert = forms.CharField(max_length=255)

    
