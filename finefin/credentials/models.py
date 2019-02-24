# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.
class BankCredentials(TimeStampedModel):
    HSBC = 'HSBC'
    VISA = 'VISA'
    BANK_NAMES = (
        (HSBC,'HSBC'),
        (VISA,'VISA')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='bank_accounts',verbose_name='Usuario')
    account_number = models.CharField(max_length=15,verbose_name='No. de cuenta',blank=True)
    card_number = models.CharField(max_length=20,verbose_name='No. de tarjeta',blank=True)
    bank_name = models.CharField(max_length=10,choices=BANK_NAMES,verbose_name='Nombre de la institución',default=HSBC)
    status = models.BooleanField(verbose_name='Status',default=True)

    class Meta:
        db_table = 'credentials_banks'
        verbose_name = 'Cuenta de banco'
        verbose_name_plural = 'Cuentas de bancos'

    def __str__(self):
        return self.bank_name

class BankCredentialsInfo(models.Model):
    credential = models.OneToOneField(BankCredentials,related_name='information',verbose_name='Credencial')
    name = models.CharField(max_length=80,verbose_name='Nombre')
    rfc = models.CharField(max_length=15,verbose_name='RFC')
    nacionality = models.CharField(max_length=2,verbose_name='Nacionalidad')
    civilstatus = models.CharField(max_length=1,verbose_name='Edo. civil',blank=True)
    phone = models.CharField(max_length=10,verbose_name='Teléfono',blank=True)

    class Meta:
        db_table = 'credentials_banks_info'
        verbose_name = 'Información cuenta de banco'
        verbose_name_plural = 'Información cuentas de bancos'

    def __str__(self):
        return self.name