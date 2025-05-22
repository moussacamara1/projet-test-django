# from django.shortcuts import render
from rest_framework import viewsets
from apps.projects.models import Project
from apps.projects.serializers import ProjectSerializer
from core.permissions import IsProductOwner
# from rest_framework.permissions import AllowAny, SAFE_METHODS


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsProductOwner()]
        return super().get_permissions()
