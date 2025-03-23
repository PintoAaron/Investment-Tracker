from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Investment

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class InvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = ['name', 'amount_invested', 'period', 'date_invested', 'url', 'description']  # Include 'period'
        widgets = {
            'date_invested': forms.DateInput(attrs={'type': 'date'}),
        }