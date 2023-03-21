from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TileViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'tiles', TileViewSet)

urlpatterns = router.urls
