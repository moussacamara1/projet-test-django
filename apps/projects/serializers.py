from rest_framework import serializers
from apps.projects.models import Project
from apps.users.models import User
from apps.users.serializers import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    owner_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='owner',
        write_only=True
    )
    team = UserSerializer(read_only=True, many=True)
    team_ids = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        many=True,
        source='team',
        write_only=True
    )

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'owner', 'owner_id',
                  'team', 'team_ids', 'dated', 'datef', 'objectifs', 'status']

    """def create(self, validated_data):
        team_data = validated_data.pop('team', [])
        project = Project.objects.create(**validated_data)
        project.team.set(team_data)
        return project

    def update(self, instance, validated_data):
        team_data = validated_data.pop('team', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if team_data is not None:
            instance.team.set(team_data)
        return instance
"""
