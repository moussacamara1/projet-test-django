import django_filters
from apps.users.models import User


class UserFilter(django_filters.FilterSet):
    role = django_filters.CharFilter(method='filter_roles')

    class Meta:
        model = User
        fields = {
            'email': ['exact', 'icontains'],
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'icontains'],
            'is_active': ['exact'],
            'is_staff': ['exact'],
            'role': ['exact', 'in']
        }

    def filter_roles(self, queryset, name, value):
        roles = value.split(',')
        return queryset.filter(role__in=roles)
