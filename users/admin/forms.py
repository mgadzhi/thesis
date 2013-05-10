# -*- coding: utf-8 -*-
import datetime
from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class UserForm(forms.ModelForm):
    pass


class AdminForm(forms.ModelForm):
    # username = forms.CharField(max_length=30),
    # password = forms.CharField(max_length=16, widget=forms.PasswordInput)
    # password_confirm = forms.CharField(max_length=16, widget=forms.PasswordInput)
    # email = forms.EmailField(initial='')
    # first_name = forms.CharField(max_length=30, initial='')
    # last_name = forms.CharField(max_length=30, initial='')
    # date_joined = forms.DateTimeField(initial=datetime.datetime.now())

    password = forms.CharField(max_length=16, widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=16, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm', 'email',
                  'first_name', 'last_name', 'date_joined']