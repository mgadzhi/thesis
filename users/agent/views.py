# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from users.agent import forms


User = get_user_model()


def index(request):
    return agent_details(request)


def agents_list(request):
    #TODO: Права
    actor = request.user
    if not any((
        actor.is_superuser,
        actor.is_admin,
        actor.is_reseller
    )):
        messages.error(request, "Looks like you're not allowed to see this page")
        return redirect('/')
    agents = User.objects.filter(user_type=User.AGENT)
    if actor.is_reseller:
        agents = agents.filter(reseller=actor)
    return render(request, 'agent/agents_list.html', {
        'agents': agents,
    })


def agent_edit(request):
    actor = request.user
    if not actor.is_agent:
        messages.error(request, "Looks like you're not allowed to see this page")
        return redirect('/')

    if request.method == 'POST':
        agent_form = forms.AgentForm(request.POST, instance=actor)
        if agent_form.is_valid():
            agent_form.save()
            return redirect('.')
        else:
            messages.error(request, 'Form is not valid')
            for error in agent_form.errors:
                messages.error(request, error)
            return redirect('.')
    else:
        agent_form = forms.AgentForm(instance=actor)
        return render(request, 'agent/agent_edit.html', {
            'agent_form': agent_form,
        })


def agent_details(request):
    actor = request.user
    if not actor.is_agent:
        messages.error(request, "Looks like you're not allowed to see this page")
        return redirect('/')

    return render(request, 'agent/agent_details.html', {
        'agent': actor,
    })
