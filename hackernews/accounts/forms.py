from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    keep_signed = forms.BooleanField(
        widget=forms.CheckboxInput,
        required=False,
    )
