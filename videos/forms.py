from django import forms
from videos.models import Postvideos
from django.forms import ModelForm

class videopostform(forms.ModelForm):
    class Meta:
        model = Postvideos
        fields = ["about_video","video"]

class updatevideopostform(forms.ModelForm):
    class Meta:
        model = Postvideos
        fields = ["about_video"]
        widgets = {
            'about_video': forms.TextInput(attrs={'class': 'form-control', 'id': 'title_box'})
        }