# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.
class PersonalProtection(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,related_name='personal_protection',verbose_name='Usuario')
    health_insurance = models.BooleanField(verbose_name='¿Cuentas con un seguro médico de gastos mayores?',default=False)
    home_insurance = models.BooleanField(verbose_name='¿Tienes asegurada tu vivienda ante desastres naturales?',default=False)
    monthly_savings = models.BooleanField(verbose_name='¿Ahorras mensualmente para tu retiro en una Afore?',default=False)
    monthly_savings_amount = models.PositiveSmallIntegerField(verbose_name='% de ahorro',null=True,blank=True)
    have_credit_cards = models.BooleanField(verbose_name='¿Tienes tarjetas de crédito? ',default=False)
    quota_available = models.DecimalField(max_digits=12,decimal_places=2,verbose_name='Cupo disponible en total',null=True,blank=True)
    investments_assets = models.BooleanField(verbose_name='¿Cuentas con inversiones o activos financieros que te generen beneficios?',default=False)
    value_investment = models.DecimalField(max_digits=12,decimal_places=2,verbose_name='Valor de la inversión con la que cuenta',null=True,blank=True)

    class Meta:
        db_table = 'personal protection'
        verbose_name = 'Protección personal'

    def __str__(self):
        return '%s %s' % (self.user.first_name,self.user.last_name)