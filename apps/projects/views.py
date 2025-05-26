# from django.shortcuts import render
from rest_framework import viewsets
from apps.projects.filters import ProjectFilter
from apps.projects.models import Project
from apps.projects.serializers import ProjectSerializer
from core.permissions import IsProductOwner
from django_filters.rest_framework import DjangoFilterBackend


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProjectFilter

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsProductOwner()]
        return super().get_permissions()
