# -*- coding: utf-8 -*-
import json
import datetime
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.response import TemplateResponse
from vrp.forms import OrderForm, StationForm, VehicleForm
from vrp.models import Station, Order, Vehicle, TaskOrdersMap
from vrp.tasks import execute_orders_task


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


def vehicles_list(request):
    actor = request.user
    if not actor.is_admin:
        messages.error(request, 'Only admins are allowed to see this page')
        return render(request, 'vehicles_list.html')
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles_list.html', {
        'vehicles': vehicles,
    })


def vehicle_create(request):
    actor = request.user
    if not actor.is_admin:
        messages.error(request, 'Only admins may add new vehicles')
        return render(request, 'base.html')
    if request.method == 'POST':
        vehicle_form = VehicleForm(request.POST)
        if vehicle_form.is_valid():
            vehicle_form.save()
            messages.success(request, 'New vehicle added')
        else:
            for error in vehicle_form.errors:
                messages.error(request, error)
        return redirect(reverse('vehicles_list'))
    vehicle_form = VehicleForm()
    return render(request, 'vehicle_create.html', {
        'vehicle_form': vehicle_form,
    })


def active_orders(request):
    actor = request.user
    if not actor.is_admin:
        messages.error(request, 'Only admins can see this page')
        return render(request, 'base.html')
    orders = Order.objects.filter(status=Order.STATUS_CREATED)
    return render(request, 'active_orders.html', {
        'orders': orders,
    })


def tasks_list(request):
    actor = request.user
    if not actor.is_admin:
        messages.error(request, 'Only admins can see this page')
        return render(request, 'base.html')
    task_orders = TaskOrdersMap.objects.all()
    return render(request, 'tasks_list.html', {
        'task_orders': task_orders,
    })


def do_execute_active_orders(request):
    orders = Order.objects.filter(status=Order.STATUS_CREATED)
    if not orders.all():
        messages.error(request, 'There are no orders to execute')
        return redirect('.')
    async_result = execute_orders_task.delay(orders)
    task_orders_map = TaskOrdersMap(
        task_id=async_result.task_id,
        orders=json.dumps([x.id for x in orders]),
        started=datetime.datetime.now()
    )
    task_orders_map.save()
    return redirect(reverse('tasks_list'))

