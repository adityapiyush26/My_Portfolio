from django import forms
from Portfolio.models import User
from django.core import validators


class ContactForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'
