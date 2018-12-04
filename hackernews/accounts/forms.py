from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UsernameField
)


User = get_user_model()


class UserLoginForm(AuthenticationForm):
    keep_signed = forms.BooleanField(
        widget=forms.CheckboxInput,
        required=False,
    )


class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email",)
        field_classes = {'username': UsernameField}
