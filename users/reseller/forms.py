# -*- coding: utf-8 -*-
import datetime
from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class ResellerForm(forms.ModelForm):

    password = forms.CharField(max_length=16, widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=16, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm', 'email',
                  'first_name', 'last_name', 'date_joined']