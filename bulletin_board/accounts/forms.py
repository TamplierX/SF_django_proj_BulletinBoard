from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )


class ActivationCodeForm(forms.ModelForm):
    first_name = forms.CharField(min_length=18, max_length=21, label='Код подтверждения')

    class Meta:
        model = User
        fields = (
            'first_name',
        )
