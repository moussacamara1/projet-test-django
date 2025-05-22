from django.urls import reverse
import pytest
from rest_framework.test import APIClient

from apps.users.models import User


@pytest.mark.django_db
def test_register_view():
    client = APIClient()
    url = reverse('register')
    data = {
        'username': 'testuser',
        'email': 'lrv4s@example.com',
        'password': 'testpassword',
    }
    response = client.post(url, data)
    assert response.status_code == 201
    assert User.objects.filter(email="lrv4s@example.com").exists()


@pytest.mark.django_db
def test_detail_detail_permission_is_self():
    user1 = User.objects.create_user(
        username='a',
        email='a@example.com',
        password='testpassword',
    )
    user2 = User.objects.create_user(
        username='b',
        email='b@example.com',
        password='testpassword',
    )
    client = APIClient()
    # Authentification de user1
    client.force_authenticate(user=user1)

    # cas 1 : user1 essaie de voir le profile de user2
    url_other = reverse('user_detail', args=[user2.id])
    res = client.get(url_other)
    assert res.status_code == 403

    # cas 2 : user1 essaie de voir son propre profile
    url_self = reverse('user_detail', args=[user1.id])
    res = client.get(url_self)
