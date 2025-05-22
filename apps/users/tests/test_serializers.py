import pytest
from apps.users.serializers import UserSerializer


@pytest.mark.django_db
def test_user_serializer_valid_data():
    data = {
        'username': 'testuser',
        'email': 'lrv4s@example.com',
        'password': 'testpassword',
        'role': 'developer',
    }
    serializer = UserSerializer(data=data)
    assert serializer.is_valid()
    user = serializer.save()
    assert user.email == "lrv4s@example.com"
    assert user.role == 'developer'
    assert user.check_password('testpassword')


@pytest.mark.django_db
def test_user_serializer_missing_email():
    data = {
        'username': 'testuser',
        'password': 'testpassword',

    }
    serializer = UserSerializer(data=data)
    assert not serializer.is_valid()
    assert 'email' in serializer.errors
