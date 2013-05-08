# -*- coding: utf-8 -*-
from rest_framework import permissions


class IsUsersReseller(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        actor = request.user
        if actor.is_admin:
            return True
        if actor.is_reseller:
            return obj == actor or obj.reseller == actor
        if actor.is_agent:
            return obj == actor

