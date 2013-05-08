# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms


User = get_user_model()


class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        # fields = ('username', )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    # user_type = forms.ChoiceField(choices=User.USER_TYPES)

    class Meta:
        model = User

    def clean_password(self):
        return self.initial["password"]

    def save(self, commit=True):
        user = super(UserChangeForm, self).save(commit=False)
        user.set_password(self.clean_password())
        if commit:
            user.save()
        return user


class UserAdmin(admin.ModelAdmin):

    form = UserChangeForm

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'password1', 'password2')
        }),
    )

    fieldsets = (
        (None, {'fields': ('username', 'password', 'user_type', 'email')}),
    )

    list_display = (
        'username',
        'email',
        'user_type',
        'reseller',
        'is_superuser',
        'is_staff',
        'is_active',
    )

    # exclude = (
    #     'password',
    #     'first_name',
    #     'last_name',
    #     'last_login',
    #     'date_joined',
    # )

admin.site.register(get_user_model(), UserAdmin)