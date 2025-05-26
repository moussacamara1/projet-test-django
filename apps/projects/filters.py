import django_filters
from apps.projects.models import Project


class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = {
            'status': ['exact'],
            'owner': ['exact'],
        }
