from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200)

    class Meta:
        model = Account
        fields = ('email', 'password1', 'password2')