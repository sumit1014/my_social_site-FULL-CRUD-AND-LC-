from django import forms
from blog.models import Post
from django.forms import ModelForm

class updateBlogpostform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["blog_title","blog_content"]
        widgets = {
            'blog_title': forms.TextInput(attrs={'class': 'form-control', 'id': 'title_box'}),
            'blog_content': forms.Textarea(attrs={'class': 'form-control', 'id': 'content_box'}),
        }