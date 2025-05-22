from apps.backlogs.models import Backlog
from rest_framework import serializers


class BacklogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Backlog
        fields = '__all__'
