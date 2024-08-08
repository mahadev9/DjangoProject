
from django import forms
from .models import UserDetails


class LoginForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['username', 'password']


class SignupForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['username', 'email', 'password']
