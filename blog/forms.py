# forms.py
from django import forms
from .models import PostForm

class MyForm(forms.ModelForm):
    class Meta:
        model = PostForm
        fields = ['name', 'email', 'message']
