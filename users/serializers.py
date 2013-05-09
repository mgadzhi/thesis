# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from django.forms import widgets
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    agents = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'password',
            'email',
            'user_type',
            'reseller',
            'agents',
        )


class AgentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'user_type',
            'username',
            'email',
            'first_name',
            'last_name',
            'reseller',
        )


class ResellerSerializer(serializers.HyperlinkedModelSerializer):
    agents = serializers.HyperlinkedRelatedField(many=True, view_name='user-detail')
    # agents = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = get_user_model()
        fields = (
            'user_type',
            'username',
            'email',
            'first_name',
            'last_name',
            'agents',
        )


class AdminSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = [
            'user_type',
            'username',
            'email',
            'first_name',
            'last_name',
            'last_login',
            'date_joined',
        ]


class UserCreator(serializers.ModelSerializer):

    password1 = serializers.CharField(max_length=128, widget=widgets.PasswordInput)
    password2 = serializers.CharField(max_length=128, widget=widgets.PasswordInput)

    def to_native(self, obj):
        del self.fields['password1']
        del self.fields['password2']
        return super(UserCreator, self).to_native(obj)

    def restore_object(self, attrs, instance=None):
        attrs['password'] = attrs['password1']
        del attrs['password1']
        del attrs['password2']
        return super(UserCreator, self).restore_object(attrs, instance)

    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
            'email',
            'first_name',
            'last_name',
        )
