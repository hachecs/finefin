# -*- coding:utf-8 -*-
from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

from accounts.models import User

class SignUp(UserCreationForm):
    email = forms.CharField(
        label = 'Correo',
        error_messages = {'required':'Debe de capturar su correo'},
        help_text = 'Este correo será su usuario para iniciar sesión',
        widget = forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder': 'Correo'
            }
        )
    )
    first_name = forms.CharField(
        label = 'Nombre',
        error_messages = {'required':'Debe de capturar su nombre'},
        widget = forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder': 'Nombre'
            }
        )
    )
    last_name = forms.CharField(
        label = 'Apellidos',
        error_messages = {'required':'Debe de capturar su apellido'},
        widget = forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder': 'Apellidos'
            }
        )
    )
    password1 = forms.CharField(
        label = 'Contraseña',
        error_messages = {'required':'Debe de capturar su contraseña'},
        widget = forms.PasswordInput(
            attrs = {
                'class':'form-control',
                'placeholder': 'Contraseña'
            }
        )
    )
    password2 = forms.CharField(
        label = 'Confirmar contraseña',
        error_messages = {'required':'Debe de confirmar su contraseña'},
        widget = forms.PasswordInput(
            attrs = {
                'class':'form-control',
                'placeholder': 'Confirmar contraseña'
            }
        )
    )
    class Meta:
        model = User
        fields = ('email','first_name','last_name','password1','password2')

    def clean_email(self):
        email = User.objects.filter(email__iexact=self.cleaned_data['email']).exists()
        if email:
            raise forms.ValidationError('Este correo ya ha sido registrado anteriormente')

        return self.cleaned_data['email']

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise forms.ValidationError('Las contraseñas no coinciden')

        return self.cleaned_data['password2']