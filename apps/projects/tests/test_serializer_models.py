import pytest

from apps.projects.models import Project
from apps.projects.serializers import ProjectSerializer


@pytest.mark.django_db
def test_project_model():
    data = {
        "name": "EduConnectSD",
        "description": "Réseau FJ social éducatif pour les étudiants et enseignants afin de partager des ressources et collaborer.",
        "owner_id": 1,
        "team_ids": [1, 2, 3],
        "end_at": "2026-03-02T00:00:00Z",
        "objectifs": "Créer un espace sécurisé pour l’apprentissage collaboratif, le partage de cours, et les discussions pédagogiques.",
        "status": "draft"
    }
    serializer = ProjectSerializer(data=data)
    assert serializer.is_valid(), serializer.errors

    project = serializer.save()
    # Vérifications
    assert Project.objects.filter(name='EduConnect').exists()
