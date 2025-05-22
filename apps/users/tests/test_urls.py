from django.urls import resolve
from apps.users.views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView


def test_register_url_resolved():
    assert resolve('/api/users/register').func.view_class == RegisterView


def test_login_url_resolved():
    assert resolve('/api/users/login/').func.view_class == TokenObtainPairView


def test_user_detail_url_resolved():
    match = resolve('/api/users/1/')
    assert match.func.view_class.__name__ == 'UserDetailView'
    assert match.kwargs['pk'] == 1
