# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth import get_user_model


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username'
        'email',
        'user_type',
        'reseller',
        'is_superuser',
        'is_staff',
        'is_active',
    )

    exclude = (
        'password',
        'first_name',
        'last_name',
        'last_login',
        'date_joined',
    )

admin.site.register(get_user_model())