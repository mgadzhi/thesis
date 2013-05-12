# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from users.admin import forms


User = get_user_model()


def index(request):
    return admin_details(request)


def admins_list(request):
    #TODO: Права
    actor = request.user
    if not any((
        actor.is_superuser,
        actor.is_admin,
    )):
        messages.error(request, "Looks like you're not allowed to see this page")
        return render(request, 'base.html')
    admins = User.objects.filter(user_type=User.ADMIN)
    return render(request, 'admin/admins_list.html', {
        'admins': sorted(admins, key=lambda x: x.id),
    })


def admin_edit(request, admin_pk=None):
    actor = request.user
    admin = actor if admin_pk is None else User.objects.get(pk=admin_pk)
    if not any((
        actor.is_superuser,
        actor.is_admin,
    )):
        messages.error(request, "Looks like you're not allowed to see this page")
        return render(request, 'base.html')
    if request.method == 'POST':
        admin_form = forms.AdminForm(request.POST)
        if admin_form.is_valid():
            return redirect('.')
    else:
        admin_form = forms.AdminForm(instance=admin)
        return render(request, 'admin/admin_edit.html', {
            'admin_form': admin_form,
        })


def admin_details(request, admin_pk=None):
    actor = request.user
    admin = actor if admin_pk is None else User.objects.get(pk=admin_pk)
    if not any((
        actor.is_superuser,
        actor.is_admin,
    )):
        messages.error(request, "Looks like you're not allowed to see this page")
        # return redirect('/')
        return render(request, 'base.html')
    return render(request, 'admin/admin_details.html', {
        'admin': admin,
    })
