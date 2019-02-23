# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from django.conf import settings
from accounts.forms import SignUp

# Create your views here.
def signup(request):
    context = {}

    if request.method == 'POST':
        context['form'] = SignUp(request.POST)
        if context['form'].is_valid():
           user = context['form'].save(commit=False)
           user.username =  context['form'].cleaned_data['email']
           user.save()

           return redirect('accounts:signup_done')
    else:
        context['form'] = SignUp()

    return render(request,'accounts/signup.html',context)

def signup_done(request):
    context = {}
    
    return render(request,'accounts/signup_done.html',context)
