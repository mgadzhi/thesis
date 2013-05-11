# -*- coding: utf-8 -*-
import datetime
from django import forms
from vrp.models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['station', 'capacity']

    def __init__(self, agent):
        super(OrderForm, self).__init__()
        self._agent = agent

    def save(self, commit=True):
        order = super(OrderForm, self).save(commit=False)
        order.agent = self._agent
        order.status = Order.STATUS_CREATED
        order.creation_date = datetime.datetime.now()
        return order.save()