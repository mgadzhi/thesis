# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    agents = serializers.PrimaryKeyRelatedField(many=True)

    test_id = serializers.IntegerField()

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'password',
            'email',
            'user_type',
            'agents',
        )
