import pytest

from apps.users.models import Profile, User


@pytest.mark.django_db
def test_user_model():
    user = User.objects.create_user(
        username='test',
        email='test@test.com',
        password='123456',
        role='developer',
    )

    assert user.email == 'test@test.com'
    assert user.role == 'developer'
    assert user.check_password('123456')


@pytest.mark.django_db
def test_profile_created():
    user = User.objects.create_user(
        username='test',
        email='test@test.com',
        password='123456',

    )
    assert Profile.objects.filter(user=user).exists()
