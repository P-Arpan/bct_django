from django import forms 
from .models import *

class userdataform(forms.ModelForm):
    address = forms.CharField(required=False)
    class Meta:
        model = user_data
        fields = ['name', 'email', 'phone_no', 'address','status']

class bookdataform(forms.ModelForm):
    class Meta:
        model = book_data
        fields = ['book_name', 'author', 'types', 'stock','status']