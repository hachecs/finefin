# -*- coding:utf-8 -*-
from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(
        label = 'Correo',
        error_messages = {'required':'Debe de capturar su correo'},
        widget = forms.EmailInput(
            attrs = {
                'class':'form-control',
                'placeholder': 'Correo'
            }
        )
    )
    password = forms.CharField(
        label = 'Contraseña',
        error_messages = {'required':'Debe de capturar su contraseña'},
        widget = forms.PasswordInput(
            attrs = {
                'class':'form-control',
                'placeholder': 'Correo'
            }
        )
    )
    