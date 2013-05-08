# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.forms import ModelForm


class UserCreationForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username',)

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class UserAdmin(admin.ModelAdmin):

    add_form = UserCreationForm

    list_display = ('username', )
    ordering = ('username', )
    fieldsets = (
        (None, {'fields': ('username', 'password', 'user_type', 'reseller')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password')
        }),
    )
    filter_horizontal = ()


admin.site.register(get_user_model(), UserAdmin)