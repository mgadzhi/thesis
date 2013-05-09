# Create your views here.
import datetime
from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
from users import permissions as users_permissions, serializers


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        users_permissions.IsUsersReseller,
    )


class AgentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.filter(user_type=User.AGENT)
    serializer_class = serializers.AgentSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        users_permissions.CanAccessAgent,
    )


class ResellerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.filter(user_type=User.RESELLER)
    serializer_class = serializers.ResellerSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        users_permissions.CanAccessReseller,
    )


class AdminViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.filter(user_type=User.ADMIN)
    serializer_class = serializers.AdminSerializer
    permissions = (
        permissions.IsAuthenticated,
        users_permissions.CanAccessAdmin,
    )
