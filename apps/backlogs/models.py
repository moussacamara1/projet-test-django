from django.db import models


class Backlog(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    end_at = models.DateTimeField(null=True, blank=True)
    project = models.ForeignKey(
        'projects.Project', on_delete=models.CASCADE, related_name='backlogs')

    def __str__(self):
        return self.name
