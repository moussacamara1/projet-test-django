import django_filters
from apps.sprints.models import Sprint


class SprintsFilter(django_filters.FilterSet):
    class Meta:
        model = Sprint
        fields = {
            'name': ['exact', 'icontains'],
            'project': ['exact'],
        }
