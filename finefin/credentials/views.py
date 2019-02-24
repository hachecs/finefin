# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

from hsbc.api_hsbc import accountProfile,clientProfile
from .models import BankCredentialsInfo
from .forms import BankCredentialsForm

# Create your views here.
@login_required
def banks_begin_add(request):
    context = {}

    if request.method == 'POST':
        context['form'] = BankCredentialsForm(request.POST)
        if context['form'].is_valid():
            #-- Check account number from the bank credentials
            bank_account = accountProfile(context['form'].cleaned_data['account_number'])
            if bank_account:     
                #-- Save account information
                credential = context['form'].save(commit=False)
                credential.user = request.user
                credential.save()

                client_number = bank_account['firstHolder']['clientNumber']
                bank_profile = clientProfile(client_number)
                #-- Save profile information
                profile = BankCredentialsInfo.objects.create(
                        credential = credential,
                        name = bank_profile['name'],
                        rfc = bank_profile['rfc'],
                        nacionality = bank_profile['nationality'],
                        civilstatus = bank_profile['civilStatus'],
                        phone = bank_profile['homePhone'],
                        )

                return redirect('login:dashboard')
            else:
                context['message'] = 'Hay un problema con su no. de cuenta. Favor de verificarla'
    else:
        context['form'] = BankCredentialsForm()
    
    return render(request,'credentials/credentials_bank_begin.html',context)