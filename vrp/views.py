# -*- coding: utf-8 -*-
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.response import TemplateResponse
from vrp.forms import OrderForm, StationForm
from vrp.models import Station, Order


def index(request):
    return TemplateResponse(request, 'index.html')


def orders_list(request):
    actor = request.user
    if not any((
        actor.is_reseller,
        actor.is_agent,
    )):
        messages.error(request, 'Only resellers and their agents can see this page')
        return render(request, 'base.html')
    reseller = actor if actor.is_reseller else actor.agent_reseller
    orders = Order.objects.filter(reseller=reseller)
    print actor.is_agent
    return render(request, 'orders/orders_list.html', {
        'actor': actor,
        'orders': orders,
    })


def order_create(request):
    actor = request.user
    if not actor.is_agent:
        messages.error('Only agents are supposed to create new orders')
        return render(request, 'base.html')
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        order_form.set_agent(actor.as_agent())
        if order_form.is_valid():
            order_form.save()
            messages.success(request, 'Order successfully created')
            return redirect(reverse('orders_list'))
        else:
            for error in order_form.errors:
                messages.error(request, error)
                return redirect('.')
    order_form = OrderForm()
    return render(request, 'orders/order_create.html', {
        'agent': actor,
        'order_form': order_form,
    })


def stations_list(request):
    actor = request.user
    if not actor.is_admin:
        messages.error('Only admins are allowed to see this page')
        return render(request, 'base.html')
    stations = Station.objects.all()
    return render(request, 'stations_list.html', {
        'stations': stations,
    })


def station_create(request):
    actor = request.user
    if not actor.is_admin:
        messages.error('Only admins may add new stations')
    else:
        if request.method == 'POST':
            station_form = StationForm(request.POST)
            if station_form.is_valid():
                messages.success(request, 'New station added')
                station_form.save()
                return redirect('..')
        else:
            station_form = StationForm()
    return render(request, 'station_create.html', {
        'station_form': station_form,
    })