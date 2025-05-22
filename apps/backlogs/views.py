from apps.backlogs.models import Backlog
from apps.backlogs.serializers import BacklogsSerializer
from core.permissions import IsProductOwner
from rest_framework import viewsets


class BacklogViewSet(viewsets.ModelViewSet):
    queryset = Backlog.objects.all()
    serializer_class = BacklogsSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsProductOwner()]
        return super().get_permissions()
