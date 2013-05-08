# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from tastypie import fields
from tastypie.authentication import SessionAuthentication
from tastypie.resources import ModelResource
from users.authorization import Authorization


User = get_user_model()


class UserResource(ModelResource):

    class Meta:
        queryset = User.objects.all()
        authentication = SessionAuthentication()
        authorization = Authorization()

    reseller = fields.ForeignKey('self', 'reseller', null=True)