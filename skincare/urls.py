from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SkinAnalysisView,
    SkincareRoutineViewSet,
    SkincareReminderViewSet,
    SkincareProgressViewSet,
    SkinProfileView
)


router = DefaultRouter()
router.register(r'routines', SkincareRoutineViewSet, basename='skincare-routine')
router.register(r'reminders', SkincareReminderViewSet, basename='skincare-reminder')
router.register(r'progress', SkincareProgressViewSet, basename='skincare-progress')  # <-- added

urlpatterns = [
    path('analyze/', SkinAnalysisView.as_view(), name='skin-analyze'),
    path('', include(router.urls)),
    path('profile/', SkinProfileView.as_view(), name='skin-profile'),
]
