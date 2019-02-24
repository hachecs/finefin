# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from django.conf import settings
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from core.tokens import account_activation_token

from .models import User
from .forms import SignUp

# Create your views here.
def signup(request):
    context = {}

    if request.method == 'POST':
        context['form'] = SignUp(request.POST)
        if context['form'].is_valid():
           user = context['form'].save(commit=False)
           user.username =  context['form'].cleaned_data['email']
           user.is_active = False
           user.save()

           #-- Send email with activatio instructions
           User.sendmail_activation(request,user)

           return redirect('accounts:signup_done')
    else:
        context['form'] = SignUp()

    return render(request,'accounts/signup.html',context)

def signup_done(request):
    context = {}
    
    return render(request,'accounts/signup_done.html',context)

def signup_activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.email_confirmed = True
        user.save()
        
        return render(request, 'accounts/signup_complete.html')
    else:
        return render(request, 'accounts/signup_expired.html')
