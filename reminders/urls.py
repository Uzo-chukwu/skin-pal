from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReminderViewSet

router = DefaultRouter()
router.register(r'', ReminderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
