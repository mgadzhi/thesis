# -*- coding: utf-8 -*-
import datetime
from django import forms
from django.core.exceptions import ValidationError
from vrp.models import Order, Station


class OrderForm(forms.ModelForm):

    _agent = None
    _reseller = None

    class Meta:
        model = Order
        fields = ['station', 'capacity']
        widgets = {
            'agent': forms.HiddenInput(),
            'agent_reseller': forms.HiddenInput(),
        }

    def set_agent(self, agent):
        print agent, agent.agent_reseller
        self._agent = agent
        self._reseller = agent.get_reseller()

    def clean(self):
        cleaned_data = super(OrderForm, self).clean()
        print cleaned_data
        if self._agent is None:
            raise ValidationError('Invalid Agent for order form')
        cleaned_data['agent'] = self._agent
        cleaned_data['reseller'] = self._reseller
        return cleaned_data

    def save(self, commit=True):
        order = super(OrderForm, self).save(commit=False)
        order.agent = self._agent
        order.reseller = self._reseller
        order.status = Order.STATUS_CREATED
        order.creation_date = datetime.datetime.now()
        return order.save()


class StationForm(forms.ModelForm):

    class Meta:
        model = Station