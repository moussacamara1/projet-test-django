import logging
from rest_framework import generics
from .filters import UserFilter
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsSelf
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from core.utils.logging import handle_create_view


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        return handle_create_view(self, request, *args, **kwargs)


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter


class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSelf]


def trigger_error(request):
    division_by_zero = 1 / 1
