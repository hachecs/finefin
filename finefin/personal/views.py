# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse
from django.http import JsonResponse

from .forms import PersonalProtectionForm

@login_required
def personal_add(request):
    context = {}
    data = {}

    context['url_post'] = reverse('personal:personal_add')

    if request.is_ajax and request.method == 'POST':
        
        context['form'] = PersonalProtectionForm(request.POST)

        if context['form'].is_valid():

            personal = context['form'].save(commit=False)
            personal.user = request.user
            personal.save()
              
            data['form_is_valid'] = True

        else:
            data['form_is_valid'] = False

    else:
        context['form'] = PersonalProtectionForm()

    data['html_personal'] = render_to_string('personal/personal_form.html', context, request=request)

    return JsonResponse(data) 