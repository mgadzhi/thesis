# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class AgentForm(forms.ModelForm):

    password = forms.CharField(required=False, max_length=16, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
