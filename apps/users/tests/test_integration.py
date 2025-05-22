from django.urls import reverse
import pytest
from rest_framework.test import APIClient

from apps.users.models import User


@pytest.mark.django_db
def test_user_workflow():
    client = APIClient()

    # Create a user
    register_url = reverse('register')
    register_data = {
        'username': 'testuser',
        'email': 'lrv4s@example.com',
        'password': 'testpassword',
        'confirm_password': 'testpassword',
    }
    response = client.post(register_url, register_data, format='json')
    assert response.status_code == 201
    assert User.objects.filter(username='testuser').exists()

    # Login the user
    login_url = reverse('token_obtain_pair')
    login_data = {
        'email': 'lrv4s@example.com',
        'password': 'testpassword',
    }
    response = client.post(login_url, login_data, format='json')
    assert response.status_code == 200
    tokens = response.data
    assert 'access' in tokens and 'refresh' in tokens

    # 3. Verification du token
    verify_url = reverse('token_verify')
    response = client.post(verify_url, {'token': tokens['access']}, format='json')
    assert response.status_code == 200

    # 4. Acces aux details de l'utilisateur connecté
    user = User.objects.get(email='lrv4s@example.com')
    detail_url = reverse('user_detail', kwargs={'pk': user.pk})
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + tokens['access'])
    response = client.get(detail_url)
    assert response.status_code == 200
    assert response.data['email'] == 'lrv4s@example.com'

    # 5. Acces à la liste des utilisateurs si permission accordée
    list_url = reverse('user_list')
    response = client.get(list_url)
    assert response.status_code in [200, 403]
