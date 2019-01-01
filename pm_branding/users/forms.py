# Creates a new form inherinted from jdango : from django import forms
# The new form is a customization with addtional fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.fields import CharField


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    # Next class is used to tell what model is going to be used and what fields
    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email', 'password1',
            'password2'
        ]
