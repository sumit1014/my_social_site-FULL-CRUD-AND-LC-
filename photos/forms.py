from django import forms
from photos.models import Postphotos
from django.forms import ModelForm

class photopostform(forms.ModelForm):
    class Meta:
        model = Postphotos
        fields = ["caption","image"]
      
class updatephotopostform(forms.ModelForm):
    class Meta:
        model = Postphotos
        fields = ["caption"]
        widgets = {
            'caption': forms.TextInput(attrs={'class': 'form-control', 'id': 'title_box'})
        }