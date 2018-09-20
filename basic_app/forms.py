from django import forms
from django.contrib.auth.models import User 
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ("username","first_name","last_name","email","password")


class UserProfileInfoForm(forms.ModelForm):
    """Form definition for UserProfileInfo."""

    class Meta:
        """Meta definition for UserProfileInfoform."""

        model = UserProfileInfo
        fields = ('gender','age')
