from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.sprints.views import SprintViewSet

router = DefaultRouter()
router.register(r'', SprintViewSet , basename='backlog')
urlpatterns = [
    path('', include(router.urls)),
]
