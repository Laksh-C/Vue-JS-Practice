from django import forms

from .models import practice

class ProductCreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput())
    description   = forms.CharField(widget=forms.TextInput())
    price = forms.FloatField(widget = forms.NumberInput())
    

    class Meta:
        model = practice
        fields = ['title', 'description', 'price']

