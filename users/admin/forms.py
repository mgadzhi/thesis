# -*- coding: utf-8 -*-
import datetime
from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from users.models import Admin


User = get_user_model()


class UserForm(forms.ModelForm):
    pass


class AdminForm(forms.ModelForm):

    password_input = forms.CharField(max_length=16, widget=forms.PasswordInput, required=False)
    password_confirm = forms.CharField(max_length=16, widget=forms.PasswordInput, required=False)

    class Meta:
        model = Admin
        fields = ['username', 'password_input', 'password_confirm', 'email',
                  'first_name', 'last_name', 'date_joined']

    def clean(self):
        cleaned_data = super(AdminForm, self).clean()
        pwd1 = cleaned_data['password_input']
        pwd2 = cleaned_data['password_confirm']
        cleaned_data['password'] = ''
        if pwd1 or pwd2:
            print '1: {}'.format(pwd1)
            print '2: {}'.format(pwd2)
            if pwd1 != pwd2:
                raise ValidationError('Passwords do not match')
            else:
                cleaned_data['password'] = pwd1
        return cleaned_data

    def save(self, commit=True):
        instance = super(AdminForm, self).save(commit=False)
        password = self.cleaned_data['password']
        if password:
            instance.set_password(password)
        return instance.save()