from apps.sprints.models import Sprint
from rest_framework import serializers


class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = '__all__'
