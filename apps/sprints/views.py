# from django.shortcuts import render

from apps.sprints.models import Sprint
from apps.sprints.serializers import SprintSerializer
from core.permissions import IsProductOwner
from rest_framework import viewsets


class SprintViewSet(viewsets.ModelViewSet):
    queryset = Sprint.objects.all()
    serializer_class = SprintSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsProductOwner()]
        return super().get_permissions()
