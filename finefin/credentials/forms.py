# -*- coding:utf-8 -*-
from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

from credentials.models import BankCredentials

class BankCredentialsForm(forms.ModelForm):
    account_number = forms.CharField(
        label = 'No. de cuenta',
        error_messages = {'required':'Debe de capturar su no. de cuenta'},
        widget = forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder': 'No. de cuenta'
            }
        )
    )

    class Meta:
        model = BankCredentials
        fields = ('account_number',)

