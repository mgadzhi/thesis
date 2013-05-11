# -*- coding: utf-8 -*-
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.response import TemplateResponse
from vrp.forms import OrderForm


def index(request):
    return TemplateResponse(request, 'index.html')


def orders_list(request):
    return HttpResponse('Under development')


def order_create(request):
    actor = request.user
    if not actor.is_agent:
        messages.error('Only agents are supposed to create new orders')
        return redirect(reverse('orders_list'))
    order_form = OrderForm(actor)
    return render(request, 'orders/order_create.html', {
        'agent': actor,
        'order_form': order_form,
    })
