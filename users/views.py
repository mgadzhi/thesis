# Create your views here.
from django.contrib.auth import get_user_model
from django.http import Http404
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import UserSerializer


User = get_user_model()


class UserList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def pre_save(self, obj):
        obj.reseller = self.request.user


class UserDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def pre_save(self, obj):
        obj.reseller = self.request.user