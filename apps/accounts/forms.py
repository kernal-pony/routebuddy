from django import forms
from django.contrib.auth.forms import UserCreationForm  ##user registration

from django.contrib.auth.forms import AuthenticationForm ## user login

from .models import User


class UserRegistrationForm(UserCreationForm):

    class Meta:

        model = User

        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]

class UserLoginForm(AuthenticationForm):
    pass