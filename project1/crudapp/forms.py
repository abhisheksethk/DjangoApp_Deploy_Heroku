from django import forms
from .models import Product

class CrudForm(forms.ModelForm):
    class Meta:  #must be Meta in capital format
        model=Product
        #fields = "--all--" 
        fields=("description","price","quantity")
    