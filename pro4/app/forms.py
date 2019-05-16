from django import forms
from .models import user_profile
from django.contrib.auth.models import User

class user_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields =('username','first_name','last_name','email','password')

class user_profile_form(forms.ModelForm):
    class Meta():
        model=user_profile
        fields=('profile_pic','portfolio')
