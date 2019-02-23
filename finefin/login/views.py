# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

from login.forms import LoginForm

# Create your views here.
def authorization(request):
    context = {}
    if request.user.is_authenticated():
        return redirect('login:dashboard')
    
    if request.method == 'POST':
        context['form'] = LoginForm(request.POST)
        if context['form'].is_valid():
            user = authenticate(email=context['form'].cleaned_data['email'],password=context['form'].cleaned_data['password'])
            if user:
                login(request,user)

                return redirect('login:dashboard')
            else:
                context['message'] = 'Usuario o contraseña incorrectos'
        else:
            context['message'] = 'Usuario o contraseña incorrectos'
    else:
        context['form'] = LoginForm()

    return render(request,'login/login.html',context)

@login_required
def dashboard(request):    
    context = {}

    return render(request,'login/dashboard.html',context)

def authorization_logout(request):
    logout(request)

    return redirect('login:login')