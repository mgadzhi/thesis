# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from users.admin import forms


User = get_user_model()


def admins_list(request):
    #TODO: Права
    actor = request.user
    if not any((
        actor.is_superuser,
        actor.is_admin,
    )):
        raise Exception('Permission denied')
    admins = User.objects.filter(user_type=User.ADMIN)
    return render(request, 'admin/admins_list.html', {
        'admins': admins,
        })


def admin_edit(request, pk):
    actor = request.user
    if not any((
        actor.is_superuser,
        actor.is_admin,
    )):
        raise Exception('Permission denied')

    if request.method == 'POST':
        admin_form = forms.AdminForm(request.POST)
        if admin_form.is_valid():
            return redirect('.')
    else:
        admin = User.objects.get(pk=pk)
        admin_form = forms.AdminForm(instance=admin)
        return render(request, 'admin/admin_edit.html', {
            'admin_form': admin_form,
        })


def admin_details(request, pk):
    actor = request.user
    if not any((
        actor.is_superuser,
        actor.is_admin,
    )):
        raise Exception('Permission denied')

    admin = User.objects.get(pk=pk)
    resellers = User.objects.filter(user_type=User.RESELLER)
    agents = User.objects.filter(user_type=User.AGENT)
    print resellers
    print
    print agents
    return render(request, 'admin/admin_details.html', {
        'admin': admin,
        'resellers': resellers,
        'agents': agents,
    })
