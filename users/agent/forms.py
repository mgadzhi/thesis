# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class AgentForm(forms.ModelForm):

    raw_password = forms.CharField(
        required=False,
        max_length=16,
        widget=forms.PasswordInput,
        label='Password'
    )

    class Meta:
        model = User
        fields = ['username', 'raw_password', 'email', 'first_name', 'last_name']

    def save(self, commit=True):
        instance = super(AgentForm, self).save(commit=False)
        pwd = self.cleaned_data['raw_password']
        if pwd:
            instance.set_password(pwd)
            instance.save()
        return instance.save()
