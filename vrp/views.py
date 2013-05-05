# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.template.response import TemplateResponse


@login_required
def index(request):
    return TemplateResponse(request, 'index.html')


def sign_in(request):
    errors = []
    link = ''
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if user.is_superuser:
                    return redirect('/admin/')
                else:
                    return redirect('/')
            else:
                errors.append('Sorry, this user is blocked')
        else:
            errors.append('Authentication failed. Try again.')
    return TemplateResponse(request, 'login.html', {
        'errors': errors
    })


def sign_out(request):
    logout(request)
    return redirect('/signin/')