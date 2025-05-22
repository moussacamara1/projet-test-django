from apps.backlogs.views import BacklogViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', BacklogViewSet , basename='backlog')
urlpatterns = [
    path('', include(router.urls)),
]
