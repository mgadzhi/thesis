# -*- coding: utf-8 -*-
from rest_framework import permissions


class IsUsersReseller(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        actor = request.user
        return actor.is_superuser


class CanAccessAgent(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        actor = request.user
        if request.method in permissions.SAFE_METHODS:
            return any((
                actor.is_superuser,
                actor.is_admin,
                actor.is_reseller and actor == obj.reseller,
                actor.is_agent and actor == obj
            ))
        return actor.is_reseller


class CanAccessReseller(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        actor = request.user
        if request.method in permissions.SAFE_METHODS:
            return actor.is_admin or actor == obj
        return actor.is_admin


class CanAccessAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        actor = request.user
        if request.method in permissions.SAFE_METHODS:
            return actor.is_superuser or actor.is_admin
        return actor.is_admin
