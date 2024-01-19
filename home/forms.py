from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class updateuserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'input_box'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'input_box'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'id': 'input_box'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'input_box'}),
        }