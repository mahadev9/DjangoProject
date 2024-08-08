
from django import forms
from .models import UserDetails


# class LoginForm(forms.ModelForm):
    # class Meta:
    #     model = UserDetails
    #     fields = ['email', 'password']

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()


class SignupForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['username', 'name', 'email', 'password']
