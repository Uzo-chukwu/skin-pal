from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets, permissions
from rest_framework import generics

from .models import SkinAnalysis, SkincareProgress, SkincareRoutine, SkincareReminder, SkinProfile
from .serializers import (
    SkinAnalysisSerializer,
    SkincareProgressSerializer,
    SkincareRoutineSerializer,
    SkincareReminderSerializer,
    SkinProfileSerializer
)





class SkinAnalysisView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        operation_description="Upload a skin image for analysis",
        request_body=SkinAnalysisSerializer,
        responses={201: SkinAnalysisSerializer, 400: "Bad Request"}
    )
    def post(self, request):
        serializer = SkinAnalysisSerializer(data=request.data)
        if serializer.is_valid():
            # Mock AI logic
            mock_result = {
                "skin_type": "Oily",
                "concerns": ["Acne", "Blackheads"],
                "recommendations": ["Cleanser with salicylic acid", "Oil-free moisturizer"]
            }
            serializer.save(user=request.user, analysis_result=mock_result)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class SkincareRoutineViewSet(viewsets.ModelViewSet):
    serializer_class = SkincareRoutineSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return SkincareRoutine.objects.none()
        return SkincareRoutine.objects.filter(user=self.request.user)


class SkincareReminderViewSet(viewsets.ModelViewSet):
    serializer_class = SkincareReminderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return SkincareReminder.objects.none()
        return SkincareReminder.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SkincareProgressViewSet(viewsets.ModelViewSet):
    serializer_class = SkincareProgressSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return SkincareProgress.objects.none()
        return SkincareProgress.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SkinProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SkinProfileSerializer

    def get_object(self):
        profile, _ = SkinProfile.objects.get_or_create(user=self.request.user)
        return profile
