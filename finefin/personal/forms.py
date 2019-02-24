# -*- coding:utf-8 -*-
from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

from personal.models import PersonalProtection

class PersonalProtectionForm(forms.ModelForm):
    health_insurance = forms.BooleanField(
        label = '¿Cuentas con un seguro médico de gastos mayores?',
        widget = forms.CheckboxInput(
            attrs = {
                'class':'js-switch'
            }
        )
    )
    home_insurance = forms.BooleanField(
        label = '¿Tienes asegurada tu vivienda ante desastres naturales?',
        widget = forms.CheckboxInput(
            attrs = {
                'class':'js-switch'
            }
        )
    )
    monthly_savings = forms.BooleanField(
        label = '¿Ahorras mensualmente para tu retiro en una Afore?',
        widget = forms.CheckboxInput(
            attrs = {
                'class':'js-switch'
            }
        )
    )
    monthly_savings_amount = forms.DecimalField(
        label = '% de ahorro',
        required = False,
        initial = 0,
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control'
            }
        )
    )
    have_credit_cards = forms.BooleanField(
        label = '¿Tienes tarjetas de crédito?',
        widget = forms.CheckboxInput(
            attrs = {
                'class':'js-switch'
            }
        )
    )
    quota_available = forms.DecimalField(
        label = 'Cupo disponible por tarjetas de crédito ',
        required = False,
        initial = 0,
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control'
            }
        )
    )
    investments_assets = forms.BooleanField(
        label = '¿Cuentas con inversiones o activos financieros que te generen beneficios?',
        widget = forms.CheckboxInput(
            attrs = {
                'class':'js-switch'
            }
        )
    )
    value_investment = forms.DecimalField(
        label = 'Valor de la inversión con la que cuenta',
        required = False,
        initial = 0,
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control'
            }
        )
    )
    class Meta:
        model = PersonalProtection
        fields = ('health_insurance','home_insurance','monthly_savings','monthly_savings_amount','have_credit_cards',\
                'quota_available','investments_assets','value_investment')
