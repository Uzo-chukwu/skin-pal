from django.urls import path
from .views import SkinAnalysisView

urlpatterns = [
    path('upload/', SkinAnalysisView.as_view(), name='skin-analysis'),
]
