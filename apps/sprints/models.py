from django.db import models


class Sprint(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    goal = models.TextField()
    estimated_hours = models.IntegerField()
    project = models.ForeignKey(
        'projects.Project', on_delete=models.CASCADE, related_name='sprints')

    def __str__(self):
        return self.name
