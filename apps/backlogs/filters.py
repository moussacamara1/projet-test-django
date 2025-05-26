import django_filters

from apps.backlogs.models import Backlog


class BacklogsFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Backlog
        fields = {
            'titre': ['exact', 'icontains'],
            'project': ['exact'],
        }
