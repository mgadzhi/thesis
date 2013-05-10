# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from users.reseller import forms


User = get_user_model()


def resellers_list(request):
    #TODO: Права
    actor = request.user
    if not any((
        actor.is_superuser,
        actor.is_admin,
    )):
        raise Exception('Permission denied')
    resellers = User.objects.filter(user_type=User.RESELLER)
    print resellers
    return render(request, 'reseller/resellers_list.html', {
        'resellers': resellers,
    })


def reseller_edit(request, reseller_pk):
    actor = request.user
    reseller = User.objects.get(pk=reseller_pk)
    if not any((
        actor.is_superuser,
        actor.is_admin,
        actor.is_reseller and actor == reseller
    )):
        raise Exception('Permission denied')

    if request.method == 'POST':
        reseller_form = forms.ResellerForm(request.POST)
        if reseller_form.is_valid():
            return redirect('.')
    else:
        reseller_form = forms.ResellerForm(instance=reseller)
        return render(request, 'reseller/reseller_edit.html', {
            'reseller_form': reseller_form,
        })


def reseller_details(request, reseller_pk):
    actor = request.user
    reseller = User.objects.get(pk=reseller_pk)
    if not any((
        actor.is_superuser,
        actor.is_admin,
        actor.is_reseller and actor == reseller,
    )):
        raise Exception('Permission denied')

    agents = User.objects.filter(user_type=User.AGENT)
    return render(request, 'reseller/reseller_details.html', {
        'agents': agents,
    })
