# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string

from core.tokens import account_activation_token

# Create your models here.
class User(AbstractUser):
    bio = models.TextField(verbose_name='Biografía',blank=True)
    email_confirmed = models.BooleanField(default=False)

    class Meta:
        db_table = 'users'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return '%s %s' % (self.first_name,self.last_name)

    #-- Sendmail activation
    @staticmethod
    def sendmail_activation(request,user):
        subject = 'FineFine :: Activación de cuenta'
        current_site = get_current_site(request)
        message = render_to_string('accounts/signup_email.html',{
            'domain': current_site.domain,
            'user': user,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
            }
        )
        #-- sendmail
        user.email_user(subject,message)

        return True
        
