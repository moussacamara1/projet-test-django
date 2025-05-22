from django.utils import timezone
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(
        'users.User', on_delete=models.CASCADE, related_name='projects')
    team = models.ManyToManyField('users.User', related_name='team_projects')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    end_at = models.DateTimeField(default=timezone.now)
    objectifs = models.TextField(default='Objectifs du projet')
    status = models.CharField(max_length=20, choices=[
        ('draft', 'Brouillon'),
        ('in_progress', 'En cours'),
        ('completed', 'Terminé'),
        ('archived', 'Archivé')
    ], default='draft')

    def __str__(self):
        return self.name
