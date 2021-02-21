from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class DonerRegister(UserCreationForm):
    """Forms for doner registration"""
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileUpdate(forms.ModelForm):
    """Forms for profile Update"""
    class Meta:
        model = Profile
        fields = ['full_name', 'blood_group', 'gender', 'Location', 'birthdate', 'contact_no', 'img']
